---
sidebar_position: 2
---

# Protocolos de Comunicação

## Visão Geral

A arquitetura AMIAU utiliza uma stack de comunicação em 4 camadas, projetada para balancear latência, consumo energético e resiliência em redes adversas.

## Stack de Protocolos

### Camada 1: Dispositivo → Gateway (Curto Alcance)

#### BLE 5.3 (Preferencial)
- **Uso**: Sincronização de dados, comandos, OTA updates
- **Throughput**: 2 Mbps
- **Consumo**: <10mA ativo, <5μA standby
- **Alcance**: 100m LOS, 30m indoor
- **Segurança**: AES-128, pairing com MITM protection

#### LoRa (Fallback Rural)
- **Uso**: Áreas sem cobertura celular/WiFi
- **Throughput**: 0,3-50 kbps (depende SF)
- **Consumo**: ~40mA TX, <1μA sleep
- **Alcance**: 2km urbano, 15km rural
- **Frequência**: 915MHz (Américas), 868MHz (Europa), 923MHz (Ásia)

### Camada 2: Gateway → Cloud (Longo Alcance)

#### MQTT over TLS
- **Broker**: Mosquitto / AWS IoT Core / Azure IoT Hub
- **QoS**: 1 (at least once) para telemetry; 0 para heartbeat
- **Tópicos**:
  ```
  amiau/{collar_id}/telemetry
  amiau/{collar_id}/alerts
  amiau/{collar_id}/config
  amiau/{collar_id}/ota
  ```
- **Keepalive**: 60s
- **Payload**: Protocol Buffers (compacto, esquema rígido)

#### HTTP/REST (Configuração)
- **Uso**: Configuração inicial, registro, updates de firmware
- **Auth**: Bearer JWT
- **Formato**: JSON

### Camada 3: Cloud → Processamento

#### Apache Kafka / AWS Kinesis
- **Streams**: telemetry-raw, telemetry-processed, alerts, ml-inference
- **Particionamento**: por collar_id (garante ordenamento por dispositivo)
- **Retenção**: 7 dias hot, 90 dias warm, 1 ano cold (S3)

#### gRPC (Microserviços Internos)
- **Serviços**: behavior-analysis, health-monitor, communication-engine
- **Formato**: Protocol Buffers v3
- **Latência**: <10ms intra-cluster

### Camada 4: Cloud → Cliente

#### WebSocket (Real-time)
- **Uso**: Dashboard ao vivo, alertas instantâneos
- **Heartbeat**: 30s
- **Reconexão**: Exponential backoff (1s, 2s, 4s, 8s, max 60s)

#### Server-Sent Events (SSE)
- **Uso**: Notificações push para mobile (fallback quando WebSocket indisponível)

## Formato de Dados

### Protocol Buffers (Telemetry)
```protobuf
message TelemetryPacket {
  string collar_id = 1;
  int64 timestamp_ms = 2;
  
  message Location {
    double latitude = 1;
    double longitude = 2;
    float accuracy_m = 3;
    float altitude_m = 4;
  }
  Location location = 3;
  
  message IMU {
    float accel_x = 1;
    float accel_y = 2;
    float accel_z = 3;
    float gyro_x = 4;
    float gyro_y = 5;
    float gyro_z = 6;
  }
  IMU imu = 4;
  
  float heart_rate_bpm = 5;
  float temperature_c = 6;
  float battery_pct = 7;
  
  message Environment {
    float ambient_temp_c = 1;
    float humidity_pct = 2;
    uint32 lux = 3;
  }
  Environment env = 8;
}
```

### Tamanho Médio do Pacote
- **Raw**: ~120 bytes (Protobuf)
- **MQTT overhead**: +20 bytes header
- **Total**: ~140 bytes / pacote
- **Frequência**: 1Hz em atividade, 0,1Hz em repouso
- **Dia típico**: ~2MB/dia ativo, ~200KB/dia inativo

## Segurança

### Criptografia
| Camada | Método | Chave |
|--------|--------|-------|
| BLE | AES-128-CCM | Gerada no pairing (ECDH P-256) |
| MQTT | TLS 1.3 | Certificado X.509 por dispositivo |
| HTTP | TLS 1.3 | Let's Encrypt, auto-renew |
| Kafka | TLS 1.2 + SASL/SCRAM | Credenciais de serviço |

### Gerenciamento de Chaves
- **Provisionamento**: Chaves injetadas na fábrica (HSM)
- **Rotação**: OTA a cada 90 dias ou on-demand (revogação)
- **Revogação**: Lista de revogação distribuída (CRL) + OCSP

## Resiliência

### Offline-first
- **Buffer local**: 72h de dados em SPI flash (8MB)
- **Sync prioritária**: alerts > health > location > activity
- **Compressão**: LZ4 para dados históricos

### Network Resilience
- **Circuit breaker**: após 5 falhas consecutivas, modo offline
- **Backhaul múltiplo**: WiFi → LTE-M → LoRa → satélite (fallback)
- **QoS adaptativo**: aumenta granularidade quando rede está boa; diminui quando ruim

---

**Atualização:** Contínua. RFCs abertos para propostas de protocolo.
