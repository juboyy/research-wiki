---
sidebar_position: 1
---

# API Reference

<span class="audience-badge badge-avancado">🔴 Avançado</span>

## Base URL
```
https://api.amiau.org/v1
```

## Autenticação
Todas as requisições requerem header `Authorization: Bearer {token}`

## Endpoints

### Coleira (Collar)

#### POST /collar/register
Registra nova coleira no sistema.

**Request:**
```json
{
  "device_id": "string",
  "animal_type": "dog|cat|horse|other",
  "animal_name": "string",
  "handler_id": "string",
  "firmware_version": "string"
}
```

**Response:**
```json
{
  "collar_id": "uuid",
  "status": "active",
  "registered_at": "ISO8601"
}
```

#### GET /collar/\{collar_id\}/telemetry
Retorna dados telemétricos mais recentes.

**Query params:**
- `from`: ISO8601
- `to`: ISO8601
- `granularity`: raw|1min|5min|1h|1d

**Response:**
```json
{
  "collar_id": "uuid",
  "data": [
    {
      "timestamp": "ISO8601",
      "location": {"lat": float, "lng": float, "accuracy": float},
      "acceleration": {"x": float, "y": float, "z": float},
      "heart_rate": int,
      "temperature": float,
      "battery": float
    }
  ]
}
```

### IA — Análise Comportamental

#### POST /ai/behavior/analyze
Analisa padrão comportamental a partir de dados de sensores.

**Request:**
```json
{
  "collar_id": "uuid",
  "window_minutes": 60,
  "sensor_data": [...]
}
```

**Response:**
```json
{
  "behaviors": [
    {
      "type": "walking|running|sleeping|eating|anxious|playing",
      "confidence": float,
      "duration_seconds": int,
      "start_time": "ISO8601"
    }
  ],
  "summary": {
    "dominant_behavior": "string",
    "anomaly_detected": boolean,
    "wellness_score": float
  }
}
```

### Comunicação

#### POST /communication/interpret
Interpreta sinal de comunicação animal.

**Request:**
```json
{
  "collar_id": "uuid",
  "signal_type": "vocalization|posture|physiological",
  "raw_data": {...},
  "context": "home|vet|park|training"
}
```

**Response:**
```json
{
  "interpretation": {
    "primary_need": "food|water|attention|rest|anxiety|pain|play",
    "confidence": float,
    "suggested_action": "string",
    "urgency": "low|medium|high|critical"
  }
}
```

## Códigos de Erro

| Código | Significado | Resolução |
|--------|-------------|-----------|
| 400 | Bad Request | Verificar payload |
| 401 | Unauthorized | Token inválido ou expirado |
| 403 | Forbidden | Sem permissão para este recurso |
| 404 | Not Found | Collar ID não existe |
| 429 | Rate Limited | Aguardar 60s antes de nova requisição |
| 500 | Internal Error | Contatar suporte |

## Rate Limits

- **Free tier**: 100 req/h
- **Pro tier**: 10.000 req/h
- **Enterprise**: Ilimitado (SLA 99,9%)

## SDKs

- **Python**: `pip install amiau-sdk`
- **JavaScript**: `npm install @amiau/sdk`
- **Rust**: `cargo add amiau`

---

*Documentação completa em desenvolvimento. Última atualização: 2026-05-25.*
