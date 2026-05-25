# AutoResearchClaw Skill

## Propósito
Geração automatizada de artigos científicos de alta qualidade sobre consciência, IA, animais, comunicação, IoT e wearables.

## Metodologia Anti-AI-SLOP

### O que é AI SLOP (e como evitar)
- ❌ Listas genéricas de "vantagens e desvantagens"
- ❌ Frases vazias como "em um mundo cada vez mais conectado"
- ❌ Resumos superficiais de temas óbvios
- ❌ Citações sem fontes reais
- ❌ Estrutura de ensaio de escola (intro, 3 parágrafos, conclusão)

### Princípios de Qualidade Paper
1. **Hipótese clara**: cada artigo tem uma tese central argumentativa
2. **Evidências específicas**: dados, números, estudos reais com DOI
3. **Análise crítica**: não apenas descrever, mas interpretar e conectar
4. **Originalidade**: perspectiva única que só faz sentido neste contexto
5. **Referências verificáveis**: links clickáveis para fontes primárias

## Estrutura do Artigo Profissional

### 1. Abstract (150 palavras)
- Contexto em 1 frase
- Gap/problema em 1 frase
- Tese principal em 1 frase
- Metodologia em 1 frase
- Implicação em 1 frase

### 2. Introdução (500-800 palavras)
- Abertura com situação concreta (não genérica)
- Estado da arte com lacunas
- Pergunta de pesquisa explícita
- Tese argumentativa
- Roteiro do artigo

### 3. Corpo (3000-4000 palavras)
- Seções temáticas com subtítulos específicos
- Evidências quantitativas e qualitativas
- Análise comparativa
- Conexões interdisciplinares

### 4. Discussão (500-800 palavras)
- Implicações teóricas
- Implicações práticas
- Limitações do estudo
- Direções futuras

### 5. Conclusão (300-500 palavras)
- Síntese da tese
- Contribuição original
- Chamada para ação ou reflexão

### 6. Referências
- Mínimo 15 referências
- 70% primárias (artigos, livros)
- 30% secundárias (reports, white papers)
- Todas com links clickáveis ou DOI

## Temas de Mercado (Ciclo de 4h)

### Slot 1 (00:00 UTC): Conexão + Pet Tech
- Análise de mercado de wearables para pets
- Tendências de consumo em pet tech
- Investimentos e startups do setor

### Slot 2 (04:00 UTC): Segurança + K9 Tech
- Inovações em tecnologia para forças de segurança
- Smart cities e vigilância inteligente
- Mercado de defesa e segurança pública

### Slot 3 (08:00 UTC): Confiança + Acessibilidade
- Silver economy e envelhecimento ativo
- Tecnologia assistiva para PCDs
- Health tech e monitoramento remoto

### Slot 4 (12:00 UTC): Consciência + IA
- Estado da arte em consciência animal
- IA como tradutor interespecífico
- Implicações éticas e regulatórias

### Slot 5 (16:00 UTC): IoT + Wearables
- Tendências em wearables IoT
- Edge computing e processamento local
- Privacidade e segurança de dados

### Slot 6 (20:00 UTC): Comunicação + Dados
- Big data em comportamento animal
- Semantic compression e NLP
- Arquiteturas de comunicação distribuída

## Comando de Geração
```bash
cd /root/.openclaw/workspace/research-wiki && python3 scripts/generate_article.py
```

## Verificação de Qualidade
- Mínimo 4500 palavras
- Mínimo 15 referências
- Zero frases AI-SLOP
- Tese argumentativa clara
- Dados quantitativos específicos
- Links verificáveis

## Integração com Docusaurus
- Gera arquivo .md em blog/
- Executa build
- Faz deploy para gh-pages
- Atualiza index de artigos
