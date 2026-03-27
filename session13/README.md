# Session 13 | API Testing


Implementacao do exercicio de testes para o endpoint POST /meetings.

## Requisitos

- uv
- Python 3.14+

## Setup

```bash
uv sync
```

## Rodar os testes

```bash
uv run pytest -q
```

Resultado esperado:

- 3 passed

## Estrutura

- app/main.py
- app/conftest.py
- app/tests/test_meetings.py

## Casos cobertos

- sucesso: cria reuniao com status 201
- erro: title ausente retorna 422
- erro: title com menos de 3 caracteres retorna 422

## Payload valido de exemplo

```json
{
  "title": "Planning",
  "date": "2026-03-15",
  "owner": "Jorge"
}
```
