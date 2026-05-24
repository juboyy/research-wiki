#!/usr/bin/env python3
"""
AMIAU Research Article Generator
Gerador automatizado de artigos para a Revista AMIAU
Executado via cron a cada 4 horas
"""
import os
import sys
import subprocess
import json
from datetime import datetime, timezone

RESEARCH_WIKI_PATH = "/root/.openclaw/workspace/research-wiki"
BLOG_PATH = os.path.join(RESEARCH_WIKI_PATH, "blog")

def generate_article():
    """Generate a new research article"""
    now = datetime.now(timezone.utc)
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H%M")
    
    # Topics rotation based on hour
    hour = now.hour
    if hour % 12 < 4:
        topic = "conexao"
        topic_label = "Conexão"
        theme = "Relação pessoal e familiar com pets, vínculo emocional, comunicação humano-animal"
    elif hour % 12 < 8:
        topic = "seguranca"
        topic_label = "Segurança"
        theme = "Aplicações policiais, cães de trabalho, segurança pública, monitoramento"
    else:
        topic = "confianca"
        topic_label = "Confiança"
        theme = "Cuidados com idosos, PCDs, tecnologia assistiva, acessibilidade"
    
    slug = f"artigo-{date_str}-{time_str}-{topic}"
    filename = f"{date_str}-{time_str}-{topic}.md"
    filepath = os.path.join(BLOG_PATH, filename)
    
    # Article template
    article = f"""---
slug: {slug}
title: 'Artigo de Pesquisa: {topic_label} e Tecnologia'
authors: [eliza]
tags: [consciência, ia, animais, iot, wearables, {topic}]
---

# Pesquisa em {topic_label}: {theme}

**Data:** {now.strftime("%d/%m/%Y %H:%M")} UTC  
**Tema:** {topic_label}  
**Autor:** ELIZA (AutoResearchClaw System)

{{/* truncate */}}

## Resumo

Este artigo explora as interseções entre {theme}, inteligência artificial, e tecnologias vestíveis. Gerado automaticamente via metodologia AutoResearchClaw.

## 1. Introdução

[Conteúdo gerado via AutoResearchClaw]

## 2. Estado da Arte

[Conteúdo gerado via AutoResearchClaw]

## 3. Aplicações Práticas

[Conteúdo gerado via AutoResearchClaw]

## 4. Desafios e Oportunidades

[Conteúdo gerado via AutoResearchClaw]

## 5. Conclusão

[Conteúdo gerado via AutoResearchClaw]

---

*Artigo gerado automaticamente pela Revista AMIAU*  
*Metodologia: AutoResearchClaw*  
*Data: {now.isoformat()}*
"""
    
    with open(filepath, 'w') as f:
        f.write(article)
    
    print(f"[GENERATOR] Article generated: {filepath}")
    return filepath

def build_site():
    """Build Docusaurus site"""
    os.chdir(RESEARCH_WIKI_PATH)
    result = subprocess.run(
        ["npm", "run", "build"],
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        print("[GENERATOR] Site built successfully")
        return True
    else:
        print(f"[GENERATOR] Build failed: {result.stderr}")
        return False

def deploy_site():
    """Deploy to GitHub Pages"""
    os.chdir(RESEARCH_WIKI_PATH)
    # Using docusaurus deploy command
    env = os.environ.copy()
    env["GIT_USER"] = "juboyy"
    env["USE_SSH"] = "false"
    
    result = subprocess.run(
        ["npm", "run", "deploy"],
        capture_output=True,
        text=True,
        env=env
    )
    if result.returncode == 0:
        print("[GENERATOR] Site deployed successfully")
        return True
    else:
        print(f"[GENERATOR] Deploy failed: {result.stderr}")
        return False

def main():
    print(f"[GENERATOR] Starting article generation at {datetime.now(timezone.utc).isoformat()}")
    
    # Generate article
    article_path = generate_article()
    
    # Build site
    if build_site():
        # Deploy
        deploy_site()
    
    print(f"[GENERATOR] Done at {datetime.now(timezone.utc).isoformat()}")

if __name__ == "__main__":
    main()
