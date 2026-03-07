# Meeting Note Assistant - Comandos

## 1) Setup do ambiente (uv)

```bash
cd /workspaces/backend-i/session1
uv venv
source .venv/bin/activate
uv add typer
```

## 2) Executar a CLI

O comando principal está em `meeting-note-assistant/app/cli.py`.

```bash
uv run python meeting-note-assistant/app/cli.py "<title>" "<owner>" "<date>"
```

Exemplo:

```bash
uv run python meeting-note-assistant/app/cli.py "Sprint Planning" "Alex" "2026-03-07"
```

Saída esperada:

```text
--- Meeting Created ---
Title: Sprint Planning
Owner: Alex
Date:  2026-03-07
```

## 3) Validação de data (desafio)

Formato aceito: `YYYY-MM-DD`.

Exemplo inválido:

```bash
uv run python meeting-note-assistant/app/cli.py "Retro" "Alex" "2026-99-99"
```

Saída de erro esperada:

```text
Error: '2026-99-99' is not a valid date. Use YYYY-MM-DD format.
```
