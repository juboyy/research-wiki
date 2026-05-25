# Hardware e Eletrônica

<span class="audience-badge badge-avancado">🔴 Avançado</span>

## Visão Geral do Sistema

O AMIAU collar é um dispositivo wearable de edge-AI que captura vocalizações animais, processa localmente e transmite traduções para um aplicativo mobile pareado.

## Componentes Principais

| Componente | Especificação | Função |
|-----------|--------------|--------|
| MCU | ESP32-S3-WROOM-1 | Processamento principal, WiFi/BT |
| Microfone | Knowles SPH0645LM4H | Captura de áudio 16kHz |
| Pré-amp | MAX9814 | Controle de ganho automático |
| IMU | LIS3DH | Detecção de atividade e postura |
| Bateria | Li-Po 3.7V 500mAh | 3-7 dias de autonomia |
| Fuel Gauge | MAX17048 | Monitoramento de carga |

## Arquitetura de Circuito

```
USB-C → TP4056 → Li-Po 500mAh → TPS7A02 → ESP32-S3
                                      ↓
                                   I2C Bus
                                      ↓
    ┌─────────┬─────────┬─────────┬─────────┬─────────┐
    │ SPH0645 │ MAX9814 │ LIS3DH  │ TMP117  │ VEML6030│
    │ (MIC)   │ (AGC)   │ (IMU)   │ (Temp)  │ (Lux)   │
    └─────────┴─────────┴─────────┴─────────┴─────────┘
```

## Orçamento de Potência

| Modo | Corrente | Duração Diária | Energia |
|------|----------|----------------|---------|
| Deep Sleep | 0.5mA | 20h | 10mAh |
| Listening | 15mA | 3h | 45mAh |
| Processamento | 80mA | 5min | 6.7mAh |
| WiFi Sync | 120mA | 5min | 10mAh |

**Total diário:** ~72mAh → **Vida útil:** ~7 dias

## BOM (Bill of Materials)

| Item | Part # | Qty | Custo |
|------|--------|-----|-------|
| ESP32-S3-WROOM-1 | N8R8 | 1 | $3.50 |
| MEMS Mic SPH0645 | LM4H | 1 | $1.20 |
| MAX9814 | - | 1 | $1.80 |
| LIS3DH | - | 1 | $0.80 |
| TMP117 | - | 1 | $1.50 |
| VEML6030 | - | 1 | $0.60 |
| MAX17048 | - | 1 | $1.20 |
| TP4056 | - | 1 | $0.30 |
| TPS7A02 | - | 1 | $0.50 |
| Li-Po 500mAh | 14500 | 1 | $3.00 |
| PCB + Componentes | - | - | $5.00 |
| Housings de Silicone | Custom | 1 | $2.00 |
| **Total BOM** | | | **~$21.40** |

**Custo-alvo em produção (10k unidades):** menor que $15/unidade
