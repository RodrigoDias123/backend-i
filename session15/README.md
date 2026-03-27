# Session15


Projeto Django inicial para gerenciamento de reuniões. No estado atual, a aplicação já possui a estrutura base do framework, uma app chamada `meetings`, banco SQLite configurado e uma rota HTTP simples para validação do funcionamento.

## Tecnologias

- Python 3.14
- Django 6.0.3
- SQLite3
- Uvicorn
- uv para gerenciamento do ambiente e execução de comandos

## Estrutura do projeto

```text
session15/
├── db.sqlite3
├── main.py
├── manage.py
├── pyproject.toml
├── README.md
├── meetings/
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
└── session15/
	├── settings.py
	├── urls.py
	├── asgi.py
	└── wsgi.py
```

## O que existe hoje

### App `meetings`

A app `meetings` já está registrada em `INSTALLED_APPS` e expõe uma rota própria.

### Modelo `Meeting`

O projeto possui um modelo para reuniões com os seguintes campos:

- `id`: identificador automático
- `title`: título da reunião
- `owner`: usuário responsável pela reunião
- `date`: data de criação automática
- `content`: conteúdo da reunião
- `sumary`: resumo da reunião

Observação: o campo `sumary` está escrito dessa forma no código e no banco atual.

### Rotas disponíveis

- `/admin/`: painel administrativo do Django
- `/meetings/`: endpoint da app `meetings`

Atualmente, a rota `/meetings/` retorna um HTML simples com a mensagem `Olá`.

## Requisitos

- `uv` instalado
- Python compatível com a versão definida no projeto

## Como executar

### 1. Instalar dependências

Se ainda não existir ambiente virtual configurado:

```bash
uv sync
```

### 2. Aplicar migrações

```bash
uv run python manage.py migrate
```

### 3. Iniciar o servidor de desenvolvimento

```bash
uv run python manage.py runserver
```

Depois disso, acesse:

- `http://127.0.0.1:8000/meetings/`
- `http://127.0.0.1:8000/admin/`

## Comandos úteis

### Verificar a instalação do Django

```bash
uv run python -m django --version
```

### Executar checagens do projeto

```bash
uv run python manage.py check
```

### Executar testes

```bash
uv run python manage.py test
```

No momento, o projeto não possui testes implementados.

### Ver migrações

```bash
uv run python manage.py showmigrations
```

## Banco de dados

O projeto usa SQLite com o arquivo local `db.sqlite3`. As migrações padrão do Django e a migração inicial da app `meetings` já foram aplicadas no ambiente atual.

## Arquivos principais

- `manage.py`: comandos administrativos do Django
- `session15/settings.py`: configurações da aplicação
- `session15/urls.py`: rotas principais do projeto
- `meetings/models.py`: modelo `Meeting`
- `meetings/views.py`: view da rota `/meetings/`
- `meetings/urls.py`: URLs da app `meetings`
- `main.py`: script Python simples, separado do fluxo principal do Django

## Estado atual do projeto

Este repositório está em uma fase inicial. Ele já oferece:

- estrutura base de um projeto Django funcional
- banco SQLite configurado
- app dedicada para reuniões
- modelo persistente para reuniões
- roteamento separado por app

Ainda faltam, por exemplo:

- CRUD completo para reuniões
- templates HTML
- formulários
- testes automatizados
- documentação de API, caso a aplicação evolua para REST

## 🚀 Projeto Django 6.0 com UV

Documentação Oficial: https://docs.djangoproject.com/en/6.0/

## 🛠️ 1. Configuração do Ambiente (UV)

O `uv` é a ferramenta moderna para gerir o Python e as dependências de forma isolada e rápida.

```bash
# Inicializa o ficheiro de configuração pyproject.toml na raiz
uv init

# Cria a pasta .venv (ambiente virtual) de forma explícita (opcional, pois o add já faz isso)
uv venv

# Instala a versão específica do Python 3.14 no projeto
uv install python 3.14

# Fixa (pina) o projeto à versão 3.14 para garantir consistência entre desenvolvedores
uv python pin 3.14

# Adiciona o Django e o Uvicorn (servidor ASGI para performance e async) às dependências
uv add uvicorn django

# Sincroniza o ambiente para garantir que todas as libs instaladas estão corretas
uv sync
```

## 2. Inicialização do Framework Django

O Django possui uma estrutura de "Projeto" (casca principal) e "Apps" (funcionalidades específicas).

```bash
# COMANDO CRUCIAL: Cria o projeto core na pasta atual
# O ponto '.' no final evita que o Django crie pastas duplicadas/redundantes
uv run django-admin startproject django_project .

# Para consultar todas as ferramentas e comandos disponíveis no django-admin:
uv run django-admin --help

# Cria um novo módulo (App). Use nomes no plural para representar coleções de dados
# Exemplo: 'meetings' para gerir uma lista de reuniões
uv run python manage.py startapp meetings
```

## Gestão de Containers e Limpeza (Docker)

Comandos úteis para gerir o ambiente e evitar conflitos de portas (como a 8000) com outros serviços:

```bash
# Lista todos os containers que estão em execução no momento
docker ps

# Para todos os containers ativos no sistema (limpeza total de processos antigos)
docker stop $(docker ps -aq)
```

## 🚀 Como Executar o Projeto

Para iniciar o servidor de desenvolvimento localmente, utilize:

```bash
uv run python manage.py runserver
```
