# Consciousness Interface Harness (CIH)

<span class="audience-badge badge-avancado">🔴 Avançado</span>

O **Consciousness Interface Harness (CIH)** é a arquitetura central do projeto AMIAU — um middleware de 4 camadas que media entre sinais acústicos brutos, dados sensoriais contextuais e geração de linguagem natural.

## Design Filosófico

O CIH não pretende "ler mentes". Ele funciona como uma **prótese semiótica**:

- **Amplificação de Sinais** — Detecta características acústicas que humanos normalmente ignoram
- **Reconhecimento de Padrões** — Identifica regularidades estatísticas nas associações vocalização-contexto de cada animal
- **Projeção Semântica** — Mapeia esses padrões para linguagem humana com marcadores de incerteza

## As 4 Camadas

```
┌─────────────────────────────────────────┐
│         CONSCIOUSNESS INTERFACE         │
├─────────────────────────────────────────┤
│ Layer 1: PERCEPÇÃO                      │
│   • Captura Acústica (16kHz, mono)      │
│   • Sensores de Movimento (IMU)         │
│   • Ambientais (temperatura, luz)       │
│   • Espaciais (GPS, posicionamento)     │
├─────────────────────────────────────────┤
│ Layer 2: PROCESSAMENTO                  │
│   • Pré-processamento de Áudio          │
│   • Extração de Features (MFCC)         │
│   • Classificação (CNN + RNN)           │
│   • Integração de Contexto              │
├─────────────────────────────────────────┤
│ Layer 3: TRADUÇÃO                       │
│   • Mapeamento Categorial               │
│   • Enriquecimento Contextual           │
│   • Geração via LLM                     │
│   • Personalização Individual           │
├─────────────────────────────────────────┤
│ Layer 4: SAÍDA                          │
│   • Display Visual (app)                │
│   • Feedback de Áudio (TTS)             │
│   • Logging & Aprendizado               │
└─────────────────────────────────────────┘
```

## Hipótese Gradualista

| Nível | Descrição | Exemplo |
|-------|-----------|---------|
| L0 | Sem interface | Humanos adivinhando |
| L1 | Mapeamento categorial | "Cachorro = alerta" |
| L2 | Enriquecimento contextual | "Cachorro na porta + horário = entrega" |
| **L3** | **Geração frasal (alvo CIH)** | **"Alguém chegou! Vou ver quem é!"** |
| L4 | Troca dialógica | Turn-taking bidirecional |
| L5 | Ponte fenomenal | Acesso direto à experiência subjetiva |
