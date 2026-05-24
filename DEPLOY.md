# 🚀 Deploy no GitHub Pages

## Passo 1: Criar Token de Acesso Pessoal (PAT)

1. Vá em https://github.com/settings/tokens
2. Clique em **"Generate new token (classic)"**
3. Selecione escopo: `repo` (acesso total ao repositório)
4. Copie o token gerado

## Passo 2: Configurar Variáveis de Ambiente

No terminal do servidor:
```bash
export GIT_USER=juboyy
export GITHUB_TOKEN=ghp_SEU_TOKEN_AQUI
```

## Passo 3: Executar Deploy

```bash
cd /root/.openclaw/workspace/research-wiki
npm run deploy
```

O Docusaurus fará:
1. Build do site
2. Push para branch `gh-pages`
3. Ativar GitHub Pages automaticamente

## URL Final

Após deploy: **https://juboyy.github.io/research-wiki/**

## Configuração Manual (Alternativa)

Se preferir, pode fazer upload manual:
1. Faça download da pasta `/root/.openclaw/workspace/research-wiki/build/`
2. Crie repo `juboyy/research-wiki` no GitHub
3. Ative GitHub Pages (source: branch `gh-pages` ou `main`)
4. Upload dos arquivos da pasta `build/`

## 🔄 Auto-Deploy (Cron)

Para deploy automático a cada 4 horas:
```bash
crontab -e
# Adicionar:
0 */4 * * * cd /root/.openclaw/workspace/research-wiki && GIT_USER=juboyy GITHUB_TOKEN=ghp_SEU_TOKEN npm run deploy
```
