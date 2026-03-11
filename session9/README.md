# Session 9 - FastAPI Meeting API

## Descrição
API para criação de reuniões, validando título (mínimo 3 caracteres) e lista de participantes não vazia, conforme exercício da sessão 9.

## Como rodar

1. Crie o ambiente virtual com Python 3.14 usando [uv](https://github.com/astral-sh/uv):
   ```bash
   uv venv .venv --python=3.14
   source .venv/bin/activate
   uv pip install fastapi uvicorn pydantic
   ```

2. Inicie o servidor:
   ```bash
   uvicorn app.api.main:app --reload --host 0.0.0.0 --port 8000
   ```

## Endpoints

### Criar reunião
- **POST** `/meetings`
- **Body JSON:**
  - `title` (str, obrigatório, mínimo 3 caracteres)
  - `date` (str, obrigatório)
  - `owner` (str, obrigatório)
  - `participants` (lista de str, opcional, não pode ser vazia se fornecida)

#### Exemplo de requisição válida
```bash
curl -X POST http://127.0.0.1:8000/meetings \
  -H "content-type: application/json" \
  -d '{"title": "Planning Meeting", "date": "2026-03-15", "owner": "Jorge", "participants": ["Alice", "Bob"]}'
```

#### Exemplo de erro (título curto)
```bash
curl -X POST http://127.0.0.1:8000/meetings \
  -H "content-type: application/json" \
  -d '{"title": "Ok", "date": "2026-03-15", "owner": "Jorge"}'
```

#### Exemplo de erro (participantes vazio)
```bash
curl -X POST http://127.0.0.1:8000/meetings \
  -H "content-type: application/json" \
  -d '{"title": "Planning", "date": "2026-03-15", "owner": "Jorge", "participants": []}'
```

## Estrutura
- `app/api/schemas.py`: Schemas Pydantic
- `app/api/main.py`: Endpoint FastAPI
