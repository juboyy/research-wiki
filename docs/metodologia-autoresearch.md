---
sidebar_position: 3
---

# Metodologia AutoResearch

## Princípio Fundamental

AutoResearchClaw não é um "gerador de conteúdo". É um **sistema de pesquisa estruturada** que automatiza etapas mecânicas da investigação científica, preservando julgamento humano (ou agente) nos pontos críticos.

## Pipeline de 8 Etapas

### 1. Delimitação do Problema (Human/Agent Input)
- **Input**: Pergunta de pesquisa, âmbito, público-alvo
- **Output**: PICO adaptado (Population, Intervention, Context, Outcome)
- **Critério de qualidade**: Pergunta deve ser falsificável

### 2. Busca Sistematizada (Automated)
- **Fontes**: PubMed, arXiv, IEEE Xplore, Google Scholar, Semantic Scholar
- **Estratégia**: Booleana com sinônimos, truncamento, filtros de data/idioma
- **Limite**: 500 resultados brutos por fonte
- **Deduplicação**: DOI matching + similaridade de título (>80%)

### 3. Triagem por Relevância (Semi-automated)
- **Fase 1 (auto)**: Filtro por keywords em título/abstract; descarte óbvio
- **Fase 2 (agent)**: Leitura de abstract; decisão include/exclude/uncertain
- **Critérios de inclusão**: Peer-reviewed, data ≤10 anos (exceto clássicos), idioma EN/PT/ES
- **Critérios de exclusão**: Editoriais, abstracts de conferência sem proceedings, preprints sem revisão

### 4. Extração de Dados (Automated + Agent Review)
- **Campos extraídos**: Autores, ano, journal, DOI, método, N amostra, principal achado, limitações, conflitos de interesse
- **Formatação**: Tabela estruturada (CSV/JSON)
- **Validação**: Agent verifica 10% aleatório para precisão

### 5. Análise de Qualidade (Agent)
- **Checklist**: PRISMA para reviews; CONSORT para RCTs; STROBE para observacionais
- **Score**: Alta / Média / Baixa qualidade (determina peso na síntese)
- **Exclusão por qualidade**: Estudos Baixa são excluídos da síntese principal, mencionados em apêndice

### 6. Síntese e Interpretação (Agent)
- **Técnica**: Narrativa qualitativa + meta-análise quando viável (N≥3, heterogeneidade I²&lt;50%)
- **Visualização**: Forest plots (meta-análise), diagramas de fluxo (revisão)
- **Identificação de gaps**: Lacunas explícitas no conhecimento atual

### 7. Redação (Automated Template + Agent Polish)
- **Template**: Abstract estruturado → Introdução com gap → Métodos → Resultados → Discussão → Conclusão
- **Anti-AI-SLOP check**: 
  - Zero frases genéricas ("em um mundo cada vez mais...")
  - Dados específicos com intervalos
  - Citações com contexto interpretativo (não apenas listagem)
  - Tese argumentativa clara
- **Revisão**: Agent lê e reescreve parágrafos "genéricos" detectados

### 8. Verificação Final (Agent)
- **Checklist**:
  - [ ] Mínimo 15 referências
  - [ ] 70% primárias (peer-reviewed)
  - [ ] Todos os DOIs/links verificáveis
  - [ ] Nenhum "lorem ipsum" ou placeholder
  - [ ] Abstract &lt;250 palavras
  - [ ] Word count >4500
  - [ ] Zero frases AI-SLOP (verificação manual por amostragem)
- **Output**: Artigo pronto para publicação

## Métricas de Qualidade

| Métrica | Mínimo | Ideal |
|---------|--------|-------|
| Palavras | 4.500 | 6.000+ |
| Referências | 15 | 25+ |
| Fontes primárias | 70% | 80%+ |
| Dados quantitativos | 5+ pontos | 10+ pontos |
| Frases AI-SLOP | 0 | 0 |
| Links quebrados | 0 | 0 |
| Tempo de geração | &lt;4h | ~2h |

## Limitações Conhecidas

1. **Alucinações**: LLMs podem "inventar" estudos. Mitigação: verificação cruzada de DOI.
2. **Recência**: Modelos têm cutoff de conhecimento. Mitigação: busca em tempo real.
3. **Vieses de publicação**: Estudos negativos subpublicados. Mitigação: busca em registros de ensaio clínico.
4. **Idioma**: Foco em EN/PT; pesquisa em mandarim/japonês subrepresentada.

## Ferramentas Utilizadas

- **Busca**: SerpAPI, CrossRef, Europe PMC
- **Extração**: GPT-4/Claude + parsing estruturado
- **Verificação**: DOI Resolver, Unpaywall, OpenAlex
- **Redação**: Docusaurus MDX + template LaTeX-like
- **Deploy**: GitHub Pages + CI/CD

## Versionamento

Cada artigo é versionado:
- **v1.0**: Publicação inicial
- **v1.1**: Correções menores (links, typos)
- **v2.0**: Atualização substantiva (novos dados, métodos)
- **Changelog**: Documentado em cada arquivo

---

**Padrão:** Adaptado de PRISMA 2020, Cochrane Handbook v6.3, e Guidelines for Reporting Evaluation Studies in Health Informatics.

**Última atualização:** 2026-05-25
