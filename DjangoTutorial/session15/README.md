# Session15 - Django Polls

Projeto de estudo baseado no tutorial oficial do Django (partes 1 a 8), com app de enquetes, admin customizado, arquivos estaticos, testes automatizados e integracao com Django Debug Toolbar.

## Stack

- Python 3.14
- Django 6.0.x
- django-debug-toolbar 6.2.x
- SQLite (db.sqlite3)
- Gerenciamento de dependencias com uv

## Estrutura do projeto

```text
session15/
├── manage.py
├── db.sqlite3
├── pyproject.toml
├── session15/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── polls/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── tests.py
│   ├── templates/polls/
│   │   ├── index.html
│   │   ├── detail.html
│   │   └── results.html
│   └── static/polls/
│       ├── style.css
│       └── images/background.png
└── templates/admin/
    └── base_site.html
```

## Configuracao rapida

1. Instalar dependencias

```bash
uv sync
```

2. Rodar migracoes

```bash
uv run python manage.py migrate
```

3. Criar superusuario (admin)

```bash
uv run python manage.py createsuperuser
```

4. Subir servidor

```bash
uv run python manage.py runserver
```

## Comandos principais

### Dependencias

```bash
# adicionar pacote
uv add <pacote>

# instalar/atualizar ambiente conforme lock
uv sync
```

### Django - gerenciamento

```bash
# versao do Django
uv run python -m django --version

# verificacao de configuracao
uv run python manage.py check

# gerar migracoes
uv run python manage.py makemigrations

# aplicar migracoes
uv run python manage.py migrate

# ver SQL de uma migracao
uv run python manage.py sqlmigrate polls 0001

# shell do Django
uv run python manage.py shell

# rodar servidor local
uv run python manage.py runserver
```

### Testes

```bash
# todos os testes do app polls
uv run python manage.py test polls
```

## Rotas da aplicacao

### Publicas

- /polls/
- /polls/<id>/
- /polls/<id>/results/
- /polls/<id>/vote/

### Admin e debug

- /admin/
- /__debug__/ (apenas com DEBUG=True)

## Funcoes e classes implementadas

### polls/models.py

- Question.question_text: texto da pergunta
- Question.pub_date: data/hora de publicacao
- Question.__str__(): retorna question_text
- Question.was_published_recently(): retorna True apenas se pub_date estiver entre agora e 24h atras
- Choice.question: FK para Question
- Choice.choice_text: texto da opcao
- Choice.votes: contador de votos (default 0)
- Choice.__str__(): retorna choice_text

### polls/views.py

- IndexView(ListView)
  - template: polls/index.html
  - contexto: latest_question_list
  - get_queryset(): ultimas 5 perguntas com pub_date <= now
- DetailView(DetailView)
  - template: polls/detail.html
  - get_queryset(): exclui perguntas futuras
- ResultsView(DetailView)
  - template: polls/results.html
  - get_queryset(): exclui perguntas futuras
- vote(request, question_id)
  - recebe POST com choice
  - incrementa votos com F("votes") + 1
  - redireciona para polls:results
  - se choice nao for enviado, renderiza detail com error_message

### polls/admin.py

- ChoiceInline(TabularInline)
  - model: Choice
  - extra: 3
- QuestionAdmin(ModelAdmin)
  - fieldsets para organizar formulario
  - inlines para editar Choice dentro de Question
  - list_display: question_text, pub_date, was_published_recently
  - list_filter: pub_date
  - search_fields: question_text
- registro no admin: Question com QuestionAdmin

### polls/urls.py

- app_name = "polls"
- index -> IndexView
- detail -> DetailView
- results -> ResultsView
- vote -> vote

### session15/settings.py

- Banco: SQLite (db.sqlite3)
- Time zone: Europe/Lisbon
- Templates de projeto ativos em BASE_DIR / "templates"
- Debug Toolbar ativa em DEBUG=True:
  - adiciona debug_toolbar em INSTALLED_APPS
  - adiciona DebugToolbarMiddleware em MIDDLEWARE
  - INTERNAL_IPS = ["127.0.0.1"]

### session15/urls.py

- inclui rotas do app polls
- inclui admin
- inclui __debug__/ quando DEBUG=True

## Templates e estaticos

### Templates

- polls/templates/polls/index.html
  - lista perguntas
  - carrega CSS com {% load static %}
- polls/templates/polls/detail.html
  - formulario de voto (POST)
  - csrf_token
  - radios para escolhas
- polls/templates/polls/results.html
  - exibe votos por escolha

### Estaticos

- polls/static/polls/style.css
  - links em verde
  - imagem de fundo com caminho relativo
- polls/static/polls/images/background.png

## Admin customizado

- Branding custom em templates/admin/base_site.html:
  - titulo: Polls Administration

## Testes existentes

Arquivo polls/tests.py cobre:

- QuestionModelTests
  - futuro -> False
  - antigo -> False
  - recente -> True
- QuestionIndexViewTests
  - sem perguntas
  - pergunta passada
  - pergunta futura
  - passada + futura
  - duas passadas em ordem
- QuestionDetailViewTests
  - futura retorna 404
  - passada retorna 200
- QuestionResultsViewTests
  - futura retorna 404
  - passada retorna 200

## Fluxo recomendado de desenvolvimento

1. Fazer alteracao em models/views/templates
2. Rodar check

```bash
uv run python manage.py check
```

3. Rodar testes

```bash
uv run python manage.py test polls
```

4. Se alterou modelo, gerar e aplicar migracoes

```bash
uv run python manage.py makemigrations
uv run python manage.py migrate
```

## Troubleshooting rapido

- Debug toolbar nao aparece
  - confirmar DEBUG=True
  - confirmar INTERNAL_IPS inclui 127.0.0.1
  - confirmar middleware e app debug_toolbar ativos
  - abrir rota /__debug__/

- Mudancas de CSS nao aparecem
  - confirmar {% load static %} no template
  - confirmar caminho: {% static 'polls/style.css' %}
  - recarregar pagina sem cache

- Erro de comando python
  - usar sempre uv run python ...
