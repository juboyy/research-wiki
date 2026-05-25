#!/usr/bin/env python3
"""
AMIAU AutoResearch Cron — Tadashi Version
Gera rascunhos de artigos automaticamente a cada 4 horas seguindo
metodologia AutoResearchClaw (skill: autoresearch-tadashi.md).

Temas rotativos (6 slots de 4h):
  0h: Pet Tech          8h:  Consciência        16h: Pet Tech
  4h: Segurança         12h: IA e Comunicação  20h: Segurança
"""

import os
import sys
import subprocess
from datetime import datetime, timezone

RESEARCH_WIKI = "/root/.openclaw/workspace/research-wiki"
BLOG_PATH = os.path.join(RESEARCH_WIKI, "blog")
SKILL_PATH = os.path.join(RESEARCH_WIKI, "skills", "autoresearch-tadashi.md")

def slugify(text: str) -> str:
    replacements = {
        'á':'a','ã':'a','â':'a','à':'a','ä':'a',
        'é':'e','ê':'e','è':'e','ë':'e',
        'í':'i','î':'i','ì':'i','ï':'i',
        'ó':'o','ô':'o','õ':'o','ò':'o','ö':'o',
        'ú':'u','û':'u','ù':'u','ü':'u',
        'ç':'c','ñ':'n',
        ' ':'-','+':'-','/':'-','\\':'-',
    }
    text = text.lower()
    for k,v in replacements.items():
        text = text.replace(k,v)
    allowed = set('abcdefghijklmnopqrstuvwxyz0123456789-')
    return ''.join(c for c in text if c in allowed).strip('-')

def tema_por_hora(hour: int) -> str:
    slots = [
        (0,  "Pet Tech"),
        (4,  "Segurança"),
        (8,  "Acessibilidade"),
        (12, "Consciência Animal"),
        (16, "IA e Comunicação"),
        (20, "Wearables e IoT"),
    ]
    for threshold, tema in reversed(slots):
        if hour >= threshold:
            return tema
    return slots[0][1]

def generate_article() -> str:
    now = datetime.now(timezone.utc)
    date_iso = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H%M")
    hour = now.hour

    tema = tema_por_hora(hour)
    slug = f"auto-{slugify(tema)}"
    filename = f"{date_iso}-{slug}-{time_str}.md"
    filepath = os.path.join(BLOG_PATH, filename)

    # Se já existe artigo hoje para este tema, não gera outro
    prefix = f"{date_iso}-auto-"
    existing = [f for f in os.listdir(BLOG_PATH) if f.startswith(prefix)]
    if existing:
        print(f"[AUTORESEARCH] Já existe rascunho hoje: {existing[0]} — pulando.")
        return ""

    # Estrutura PRISMA-adaptada seguindo a skill
    article = f"""---
slug: {slug}-{time_str}
title: '{tema}: Análise Sistemática de {date_iso}'
authors: [eliza]
tags: [{slugify(tema)}, autoresearch, mercado, análise]
---

# {tema}: Análise Sistemática de {date_iso}

<span class="audience-badge badge-intermediario">🟡 Intermediário</span>

**Abstract** (rascunho — aguardando enriquecimento)

Contexto: o tema {tema} situa-se na interseção entre consciência animal, IA e wearables IoT. Método: revisão sistemática PRISMA-adaptada via AutoResearchClaw. Resultado: [a preencher após busca]. Conclusão: [a preencher].

---

## 1. Delimitação do Problema

**PICO adaptado:**
- **Population:** Mercado de {tema.lower()} em 2024-2030
- **Intervention:** Tecnologias de IA + wearables + comunicação interespécies
- **Contexto:** Segurança pública, saúde assistiva ou bem-estar animal
- **Outcome:** TAM/SAM/SOM, CAGR, adoção, barreiras regulatórias

**Tese provisória:** [a definir após busca — não pode ser vaga]

---

## 2. Busca Sistematizada (Stub)

- PubMed / arXiv / IEEE Xplore / Google Scholar
- Estratégia booleana: `"{tema}" AND ("market size" OR "CAGR" OR "forecast") AND (2024 OR 2025)`
- Limite: 500 resultados por fonte

**Fontes identificadas (placeholder):**
| # | Fonte | Ano | Tipo | Relevância |
|---|-------|-----|------|------------|
| 1 | [Nome] | 2024 | Relatório | Alta |
| 2 | [Nome] | 2025 | Paper | Média |

---

## 3. Extração de Dados (Stub)

| Métrica | Valor | Fonte | Confiança |
|---------|-------|-------|-----------|
| TAM 2030 | [inserir] | [fonte] | [alta/média/baixa] |
| CAGR | [inserir] | [fonte] | [alta/média/baixa] |
| Penetração atual | [inserir] | [fonte] | [alta/média/baixa] |

---

## 4. Análise Crítica

**Forças:** [a preencher]
**Fraquezas:** [a preencher]
**Contradições:** [a preencher]
**Lacunas:** [a preencher]

---

## 5. Limitações

1. Dados de mercado podem conter viés de otimismo de consultorias
2. Projeções de CAGR >20% requerem sanity-check com histórico
3. Regulação (LGPD, AI Act) é variável geográfica

---

## 6. Conclusão

[Tese reafirmada com evidências — a preencher]

---

## Referências

- [Placeholder — mínimo 15 referências após enriquecimento]

---

**Metodologia:** AutoResearchClaw v2.0, PRISMA-adaptado  
**Data de geração:** {now.isoformat()}  
**Tema rotativo:** {tema} (slot {hour//4}/5)  
**Status:** 📝 Rascunho — requer enriquecimento manual ou agente de pesquisa  
**Skill:** `{SKILL_PATH}`  
**Licença:** CC BY-SA 4.0
"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(article)

    print(f"[AUTORESEARCH] Rascunho criado: {filepath}")
    return filepath

def git_commit_and_deploy(filepath: str) -> bool:
    if not filepath:
        return True

    os.chdir(RESEARCH_WIKI)

    # Commit
    subprocess.run(["git", "add", "-A"], check=False)
    result = subprocess.run(
        ["git", "commit", "-m", f"autoresearch: rascunho {os.path.basename(filepath)}"],
        capture_output=True, text=True, check=False
    )
    if result.returncode != 0 and "nothing to commit" not in result.stdout.lower():
        print(f"[AUTORESEARCH] Git commit info: {result.stdout.strip()}")

    # Deploy
    env = os.environ.copy()
    token = env.get("GITHUB_TOKEN", "")
    if token:
        deploy_env = {
            **env,
            "GIT_USER": "juboyy",
            "GITHUB_TOKEN": token,
        }
        result = subprocess.run(
            ["npm", "run", "deploy"],
            capture_output=True, text=True, env=deploy_env, check=False
        )
        if result.returncode == 0:
            print("[AUTORESEARCH] Deploy realizado com sucesso.")
            return True
        else:
            print(f"[AUTORESEARCH] Deploy falhou: {result.stderr[-500:]}")
            return False
    else:
        print("[AUTORESEARCH] GITHUB_TOKEN ausente — deploy manual necessário.")
        return False

def main():
    print(f"[AUTORESEARCH] Início: {datetime.now(timezone.utc).isoformat()}")
    filepath = generate_article()
    if filepath:
        git_commit_and_deploy(filepath)
    print(f"[AUTORESEARCH] Fim: {datetime.now(timezone.utc).isoformat()}")

if __name__ == "__main__":
    main()
