#!/bin/bash
# Cron job for AMIAU Research Wiki — AutoResearch Article Generator
# Runs every 4 hours, generates 1 article based on rotating theme

set -e

REPO_DIR="/root/.openclaw/workspace/research-wiki"
BLOG_DIR="$REPO_DIR/blog"
SKILL_FILE="$REPO_DIR/skills/autoresearch-tadashi.md"
DATE=$(date +%Y-%m-%d)
HOUR=$(date +%H%M)
THEME=$(shuf -n1 <<'EOF'
mercado-pet-tech
mercado-seguranca-publica
mercado-acessibilidade-assistiva
consciencia-animal-evidencias
ia-comunicacao-interspecifica
wearables-iot-arquitetura
etica-comunicacao-animal
startups-k9-tech
startups-pet-tech
startups-assistiva
cronograma-projeto-amiau
EOF
)

echo "[$(date)] Starting AutoResearch cron — Theme: $THEME"

# Generate article using OpenClaw subagent
cd "$REPO_DIR"

# Create topic-specific prompt
PROMPT="Generate a research-grade wiki article for the AMIAU Project on theme: $THEME

Requirements:
- 4500+ words
- 15+ references with DOIs
- 70% primary sources
- Clear argumentative thesis
- Quantitative data with specific numbers
- Critical analysis including limitations
- Zero AI-SLOP (no generic lists, no vague openings, no unsubstantiated claims)
- Follow PRISMA-adapted methodology
- Audience: mixed (Leitores + Acadêmicos + Técnicos + Investidores)

Structure:
1. Abstract (structured: Context/Method/Result/Conclusion)
2. Introduction with clear thesis
3. 3-4 body sections advancing the argument with data tables
4. Limitations section
5. Future directions
6. Conclusion
7. References (DOIs + clickable URLs)

Output file: $BLOG_DIR/${DATE}-${HOUR}-${THEME}.md

After writing, run:
cd $REPO_DIR && git add -A && git commit -m \"AutoResearch: $THEME $DATE\" && GITHUB_TOKEN=... GIT_USER=juboyy npm run deploy

If deploy fails, save error log to $REPO_DIR/.cron-errors/$DATE-$HOUR.log"

echo "$PROMPT" > "$REPO_DIR/.cron-prompt.txt"

# Log
mkdir -p "$REPO_DIR/.cron-logs"
echo "[$DATE $HOUR] Theme: $THEME" >> "$REPO_DIR/.cron-logs/history.log"

# The actual generation is done by OpenClaw subagent — this script just sets up
echo "[$(date)] Prompt prepared. Waiting for subagent execution."
