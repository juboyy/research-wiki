#!/bin/bash
# AMIAU AutoResearch Cron Script
# Roda a cada 4h, gera artigo com tema rotativo, commita e deploya

set -euo pipefail

WIKI_DIR="/root/.openclaw/workspace/research-wiki"
SKILL_PATH="$WIKI_DIR/skills/autoresearch-tadashi.md"
DATE_ISO=$(date +%Y-%m-%d)
DATETIME=$(date +%Y-%m-%d-%H%M)

# Temas rotativos (6 temas para 6 slots de 4h)
HOUR=$(date +%H)
THEME_INDEX=$(( (HOUR / 4) % 6 ))

THEMES=(
  "Pet Tech"
  "Segurança"
  "Acessibilidade"
  "Consciência Animal"
  "IA e Comunicação"
  "Wearables e IoT"
)

THEME="${THEMES[$THEME_INDEX]}"
SLUG="auto-${THEME,,}"
SLUG="${SLUG// /-}"
SLUG="${SLUG//í/i}"
SLUG="${SLUG//ã/a}"
SLUG="${SLUG//ç/c}"
SLUG="${SLUG//ê/e}"
SLUG="${SLUG//ô/o}"
SLUG="${SLUG//á/a}"
SLUG="${SLUG//é/e}"
SLUG="${SLUG//ó/o}"
SLUG="${SLUG//ú/u}"
SLUG="${SLUG//ü/u}"
SLUG="${SLUG//ñ/n}"

FILE="$WIKI_DIR/blog/${DATE_ISO}-${SLUG}.md"

echo "[$(date)] Tema: $THEME | Hora: $HOUR | Índice: $THEME_INDEX"

# Se arquivo já existe hoje, pula
if [ -f "$FILE" ]; then
  echo "[$(date)] Artigo já existe: $FILE — pulando."
  exit 0
fi

# Gera artigo usando a skill (chama o agente principal via OpenClaw CLI se disponível)
# Como subagente não pode spawnar outro agente facilmente, este script é um stub
# que documenta o processo. A geração real requer:
# 1. Web search pelo tema
# 2. Escrita estruturada seguindo autoresearch-tadashi.md
# 3. Salvamento em blog/

cat > "$FILE" <<EOF
---
slug: ${SLUG}-${DATETIME}
title: '[Rascunho AutoResearch] ${THEME}: Análise de ${DATE_ISO}'
authors: [eliza]
tags: [${SLUG}, autoresearch, rascunho]
---

# [Rascunho] ${THEME}: Análise de ${DATE_ISO}

**Status:** Rascunho gerado automaticamente. Aguardando revisão e enriquecimento.

**Tema:** ${THEME}
**Data:** ${DATE_ISO}
**Metodologia:** AutoResearchClaw v2.0

## Próximos Passos

1. Executar busca web por: "${THEME} market size CAGR 2024 2025 2030"
2. Extrair 5-10 fontes primárias
3. Escrever 4500+ palavras com tese argumentativa
4. Incluir tabelas quantitativas, casos, limitações
5. Revisar por AI-SLOP
6. Commit e deploy

---

*Gerado por cron_autoresearch.sh em $(date)*
*Skill: ${SKILL_PATH}*
EOF

echo "[$(date)] Rascunho criado: $FILE"

cd "$WIKI_DIR"

git add -A
git commit -m "autoresearch: rascunho ${THEME} (${DATE_ISO})" || true

# Deploy (se token disponível)
if [ -n "${GITHUB_TOKEN:-}" ]; then
  GIT_USER=juboyy GITHUB_TOKEN="$GITHUB_TOKEN" npm run deploy 2>&1 | tail -20
  echo "[$(date)] Deploy concluído."
else
  echo "[$(date)] GITHUB_TOKEN não definido — deploy manual necessário."
fi

echo "[$(date)] Ciclo concluído."
