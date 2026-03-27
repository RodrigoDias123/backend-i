# Meetings API com FastAPI + Ollama


API simples para registar meetings e gerar automaticamente um resumo em portugues usando um modelo local no Ollama.

## O que este projeto faz

- Cria meetings com `title` e `content`
- Gera um resumo curto (ate 5 linhas) via Ollama
- Lista meetings guardadas em memoria
- Consulta uma meeting por ID

## Stack

- Python 3.14
- FastAPI
- Uvicorn
- Typer (CLI)
- Requests
- Ollama (container separado)
- Docker Compose

## Estrutura

```text
src/
	api/main.py      # Endpoints FastAPI
	client.py        # Cliente HTTP para Ollama (/api/generate)
	data.py          # Armazenamento em memoria (dict)
	models.py        # Schemas Pydantic
	cli.py           # Comandos CLI (run)
compose.yml        # Servicos api + ollama
dockerfile         # Imagem da API
Makefile           # Atalhos para subir stack e fazer pull do modelo
```

## Requisitos

- Docker + Docker Compose

Opcional (execucao local sem Docker):

- Python 3.14+
- `uv` instalado

## Como correr com Docker (recomendado)

1. Subir os servicos:

```bash
make start
```

2. Fazer pull do modelo usado pela API:

```bash
make pull
```

3. (Opcional) Correr em foreground:

```bash
make run
```

API disponivel em:

- `http://localhost:8000`
- Docs Swagger: `http://localhost:8000/docs`
- Atalho de redirect: `http://localhost:8000/doc`

## Como correr localmente (sem Docker)

1. Instalar dependencias:

```bash
uv sync
```

2. Garantir que o Ollama esta acessivel (por defeito em `http://localhost:11434`) e que o modelo existe.

3. Iniciar a API:

```bash
uv run python src/cli.py run
```

Se correr fora do Compose, ajuste `OLLAMA_BASE_URL` para `http://localhost:11434`.

## Endpoints

### `POST /meetings`

Cria uma meeting e gera resumo com Ollama.

Exemplo:

```bash
curl -X POST http://localhost:8000/meetings \
	-H "Content-Type: application/json" \
	-d '{
		"title": "Sprint planning",
		"content": "Falamos sobre prioridades da sprint, riscos e distribuicao de tarefas para a proxima semana."
	}'
```

### `GET /meetings`

Lista todas as meetings guardadas.

```bash
curl http://localhost:8000/meetings
```

### `GET /meetings/{meeting_id}`

Busca uma meeting especifica por ID.

```bash
curl http://localhost:8000/meetings/1
```

## Variaveis de ambiente

Configuradas em `src/client.py`:

- `OLLAMA_MODEL` (default: `smollm:135m-base-v0.2-q2_K`)
- `OLLAMA_BASE_URL` (default: `http://ollama:11434`)
- `OLLAMA_CONNECT_TIMEOUT` (default: `5`)
- `OLLAMA_READ_TIMEOUT` (default: `180`)
- `OLLAMA_INPUT_MAX_CHARS` (default: `3000`)
- `OLLAMA_NUM_PREDICT` (default: `160`)

Exemplo ao correr localmente:

```bash
export OLLAMA_BASE_URL="http://localhost:11434"
uv run python src/cli.py run
```

## Notas importantes

- Os dados ficam apenas em memoria (`meetings_store`), por isso perdem-se ao reiniciar a API.
- O endpoint `POST /meetings` depende do Ollama. Se o servico/modelo nao estiver disponivel, pode retornar erro `502` ou `504`.
- O Compose usa volume `./ollama_data` para persistir modelos do Ollama.

## Comandos uteis

```bash
# subir stack em background
make start

# descarregar modelo no container ollama
make pull

# ver logs da API
docker compose logs -f api

# parar stack
docker compose down
```
