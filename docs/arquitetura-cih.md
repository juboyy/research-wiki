# Arquitetura do CIH

## O Consciousness Interface Harness

O CIH é a arquitetura central do projeto AMIAU — um middleware de 4 camadas que media entre sinais acústicos brutos, dados sensoriais contextuais e geração de linguagem natural.

## Design Filosófico

O CIH não pretende "ler mentes". Ele funciona como uma **prótese semiótica**:

- **Amplificação de Sinais** — Detecta características acústicas que humanos normalmente ignoram
- **Reconhecimento de Padrões** — Identifica regularidades estatísticas nas associações vocalização-contexto
- **Projeção Semântica** — Mapeia padrões para linguagem humana com marcadores de incerteza

## As 4 Camadas

### Layer 1: Percepção
- Captura Acústica (microfone array, 16kHz mono)
- Sensores de Movimento (acelerômetro, giroscópio)
- Ambientais (temperatura, luz, horário)
- Espaciais (GPS, posicionamento indoor)

### Layer 2: Processamento
- Pré-processamento de Áudio
- Extração de Features (MFCC, espectrograma, pitch)
- Classificação Acústica (CNN + RNN)
- Integração de Contexto (fusão temporal + espacial)

### Layer 3: Tradução
- Mapeamento Categorial
- Enriquecimento Contextual
- Geração via LLM
- Personalização Individual

### Layer 4: Saída
- Display Visual (app smartphone)
- Feedback de Áudio (TTS)
- Logging & Aprendizado

## Hipótese Gradualista

| Nível | Descrição | Exemplo |
|-------|-----------|---------|
| L0 | Sem interface | Humanos adivinhando |
| L1 | Mapeamento categorial | "Cachorro = alerta" |
| L2 | Enriquecimento contextual | "Cachorro na porta + horário = entrega" |
| **L3** | **Geração frasal (alvo CIH)** | **"Alguém chegou! Vou ver quem é!"** |
| L4 | Troca dialógica | Turn-taking bidirecional |
| L5 | Ponte fenomenal | Acesso direto à experiência subjetiva |
