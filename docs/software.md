# Software e Firmware

<span class="audience-badge badge-avancado">🔴 Avançado</span>

## Arquitetura de Software (FreeRTOS)

| Tarefa | Core | Prioridade | Função |
|--------|------|------------|--------|
| **AudioCapture** | 0 | 24 | I2S DMA, double-buffering, 16kHz |
| **AudioPreprocess** | 0 | 20 | FFT, MFCC, noise gate, VAD |
| **NeuralInfer** | 1 | 22 | TFLite Micro, forward pass CNN+RNN |
| **ContextFusion** | 1 | 18 | Sensor fusion, classificação de intenção |
| **LLMBridge** | 1 | 16 | BLE packetization, streaming de prompt |
| **CommManager** | 0 | 14 | WiFi/BT stack, MQTT, HTTPS |
| **PowerManager** | 0 | 12 | Sleep scheduling, monitoramento de bateria |
| **DataLogger** | 0 | 10 | Logging em SD card / flash |

## Pipeline de Processamento

```
Áudio bruto (16kHz)
    ↓
Pré-processamento
    ├── Spectral gating (redução de ruído)
    ├── Normalização de pitch
    └── Segmentação em eventos
    ↓
Extração de Features
    ├── MFCC (13 coefs × 20 frames)
    ├── Espectrograma Mel (128 bins)
    └── Pitch tracking (YIN algorithm)
    ↓
Classificação (CNN + RNN)
    ├── CNN: 128×128 spectrogram → embedding 512-dim
    ├── RNN: BiLSTM 2 layers → embedding 256-dim
    └── Fusão + Dense → 6 classes
    ↓
Integração de Contexto
    ├── Time encoding (sin/cos 24h)
    ├── Location (one-hot, 11 categorias)
    └── Activity (embedding IMU)
    ↓
Geração via LLM
    ├── Category mapping
    ├── Context enrichment
    └── Prompt → GPT-4 / LLaMA-3B
    ↓
Output
    ├── Visual (smartphone app)
    ├── Audio (TTS)
    └── Logging & feedback loop
```

## Frameworks Utilizados

- **FreeRTOS** — Sistema operacional de tempo real
- **TensorFlow Lite Micro** — Inferência neural embarcada
- **ESP-IDF** — SDK oficial Espressif
- **MQTT** — Comunicação leve para IoT
- **BLE 5.0** — Conectividade de baixa potência com smartphone

## Modelo de ML

| Componente | Especificação |
|-----------|--------------|
| CNN | 4 conv blocks (32→64→128→256 filtros), pooling 2×2 |
| RNN | BiLSTM 2 camadas, 128 unidades ocultas |
| Fusão | Concatenação + Dense(512→128→6) |
| Classes caninas | atenção, alerta, aviso, dor/ansiedade, brincadeira/alegria, territorial |
| Classes felinas | saudação, demanda, urgência, contentamento, estresse, predatório |
