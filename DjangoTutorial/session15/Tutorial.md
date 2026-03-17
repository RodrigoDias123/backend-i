# Tutorial Django - Parte 1

Este repositório segue a primeira parte do tutorial oficial "Escrevendo seu primeiro aplicativo Django".

## Objetivo

Construir a base de um app de enquetes com:

- Projeto Django configurado
- App `polls` criado
- Primeira view e rotas funcionando

## Verificar versão do Django

Como este projeto usa `uv`, execute:

```bash
uv run python -m django --version
```

Saída esperada (ou similar):

```text
6.0.x
```

## Estrutura inicial do projeto

```text
.
├── manage.py
├── session15/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── pyproject.toml
```

## Criar o app polls

```bash
uv run python manage.py startapp polls
```

Estrutura criada:

```text
polls/
├── __init__.py
├── admin.py
├── apps.py
├── migrations/
│   └── __init__.py
├── models.py
└── views.py
```

## Primeira view

Arquivo `polls/views.py`:

```python
from django.http import HttpResponse


def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")
```

## URLconf do app

Criar `polls/urls.py`:

```python
from django.urls import path

from . import views

urlpatterns = [
	path("", views.index, name="index"),
]
```

## Incluir rotas no projeto

Atualizar `session15/urls.py`:

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
	path("polls/", include("polls.urls")),
	path("admin/", admin.site.urls),
]
```

## Rodar e testar

Subir servidor de desenvolvimento:

```bash
uv run python manage.py runserver
```

Testar no navegador:

- http://127.0.0.1:8000/polls/

Resposta esperada:

```text
Hello, world. You're at the polls index.
```

## Observações

- Um `404` em `/` é esperado nesta etapa.
- Aviso de migrações pendentes também é esperado antes de executar:

```bash
uv run python manage.py migrate
```

## Próximo passo

Seguir para a Parte 2 do tutorial para modelagem de dados, migrações e admin.

## Parte 2: Banco, Models e Admin

### Configurar app e fuso horário

No arquivo `session15/settings.py`:

- Adicionar `"polls.apps.PollsConfig"` em `INSTALLED_APPS`
- Ajustar `TIME_ZONE` (exemplo: `"America/Sao_Paulo"`)

### Criar models do app polls

No arquivo `polls/models.py`:

- `Question` com `question_text` e `pub_date`
- `Choice` com `question`, `choice_text` e `votes`

Também foram adicionados:

- `__str__()` em `Question` e `Choice`
- Método `was_published_recently()` em `Question`

### Ativar no admin

No arquivo `polls/admin.py`, registrar `Question`:

```python
from django.contrib import admin

from .models import Question

admin.site.register(Question)
```

### Gerar e aplicar migrações

```bash
uv run python manage.py makemigrations polls
uv run python manage.py sqlmigrate polls 0001
uv run python manage.py migrate
uv run python manage.py check
```

Saídas esperadas:

- Criação de `polls/migrations/0001_initial.py`
- SQL com tabelas `polls_question` e `polls_choice`
- Migração aplicada com `Applying polls.0001_initial... OK`
- `System check identified no issues (0 silenced)`

### Criar usuário admin e testar

```bash
uv run python manage.py createsuperuser
uv run python manage.py runserver
```

Abra no navegador:

- http://127.0.0.1:8000/admin/

Depois de logar, a seção `Polls` deve aparecer com o model `Questions`.

## Parte 3: Views e Templates

Nesta etapa, começamos a interface publica da aplicacao com 4 views:

- Index de perguntas
- Detalhe da pergunta
- Resultados da pergunta
- Acao de voto

### Atualizar URLs do app

Arquivo `polls/urls.py`:

- Adicionar `app_name = "polls"`
- Manter a rota de index
- Adicionar rotas de detail, results e vote com `question_id`

```python
from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
	path("", views.index, name="index"),
	path("<int:question_id>/", views.detail, name="detail"),
	path("<int:question_id>/results/", views.results, name="results"),
	path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

### Atualizar views

Arquivo `polls/views.py`:

- `index()` busca as 5 perguntas mais recentes e renderiza template
- `detail()` usa `get_object_or_404`
- `results()` e `vote()` permanecem como respostas simples

### Criar templates

Criar os arquivos:

- `polls/templates/polls/index.html`
- `polls/templates/polls/detail.html`

No `index.html`, usar URL nomeada com namespace para evitar URL hardcoded:

```html
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```

### Testar

```bash
uv run python manage.py check
uv run python manage.py runserver
```

Rotas para validar no navegador:

- http://127.0.0.1:8000/polls/
- http://127.0.0.1:8000/polls/1/
- http://127.0.0.1:8000/polls/1/results/
- http://127.0.0.1:8000/polls/1/vote/

## Parte 4: Generic Views

Nesta etapa, o app foi refinado para usar generic views e para evitar exibicao de perguntas futuras.

### Refatoracao para generic views

Arquivo `polls/views.py`:

- `IndexView` (`ListView`) para listar perguntas
- `DetailView` (`DetailView`) para pagina da pergunta
- `ResultsView` (`DetailView`) para pagina de resultados
- `vote()` processa POST, incrementa votos com `F("votes") + 1` e redireciona para resultados

Arquivo `polls/urls.py`:

- `index`: `views.IndexView.as_view()`
- `detail`: `path("<int:pk>/", ...)`
- `results`: `path("<int:pk>/results/", ...)`
- `vote`: `path("<int:question_id>/vote/", ...)`

### Regras de publicacao

Foram aplicadas as regras do tutorial:

- `IndexView` mostra apenas perguntas com `pub_date <= timezone.now()`
- `DetailView` retorna `404` para perguntas futuras
- `Question.was_published_recently()` retorna `True` apenas para perguntas do ultimo dia e nunca para futuras

## Parte 5: Testes Automatizados

Nesta etapa, adicionamos testes automatizados para proteger as regras de negocio da aplicacao de enquetes.

### O que foi alterado

Arquivo `polls/tests.py` criado com:

- Testes de modelo para `Question.was_published_recently()`:
	- pergunta futura retorna `False`
	- pergunta antiga (mais de 1 dia) retorna `False`
	- pergunta recente (menos de 1 dia) retorna `True`
- Testes da `IndexView`:
	- sem perguntas
	- apenas pergunta passada
	- apenas pergunta futura
	- mistura de passada + futura
	- duas perguntas passadas em ordem de publicacao
- Testes da `DetailView`:
	- pergunta futura retorna `404`
	- pergunta passada e exibida normalmente
- Testes da `ResultsView`:
	- pergunta futura retorna `404`
	- pergunta passada e exibida normalmente

### Ajuste adicional em views

Para manter comportamento consistente entre paginas, `ResultsView` tambem passou a ocultar perguntas futuras usando filtro por data de publicacao.

### Executar os testes

```bash
uv run python manage.py test polls
uv run python manage.py check
```

Saida esperada:

- `Found 12 test(s).`
- `OK`

## Parte 6: Arquivos Estaticos (CSS e Imagem)

Nesta etapa, adicionamos estilo visual a pagina de enquetes usando arquivos estaticos da app `polls`.

### Estrutura criada

```text
polls/
└── static/
	└── polls/
		├── style.css
		└── images/
			└── background.png
```

### Ligando CSS no template

Arquivo `polls/templates/polls/index.html` atualizado para carregar estaticos:

```django
{% load static %}
<link rel="stylesheet" href="{% static 'polls/style.css' %}">
```

### Estilo aplicado

Arquivo `polls/static/polls/style.css`:

- Cor verde para links da lista de perguntas
- Imagem de fundo via caminho relativo dentro de `static`

```css
body {
	background: white url("images/background.png") no-repeat;
}

li a {
	color: green;
}
```

### Testar no navegador

```bash
uv run python manage.py runserver
```

Depois, acesse:

- http://127.0.0.1:8000/polls/

Resultado esperado:

- links das perguntas em verde
- imagem de fundo no canto superior esquerdo

## Parte 7: Customizando o Django Admin

Nesta etapa, a area administrativa foi melhorada para facilitar cadastro, edicao e busca de perguntas e escolhas.

### Customizacoes em admin.py

Arquivo `polls/admin.py`:

- `ChoiceInline` com `admin.TabularInline` para editar escolhas dentro da pergunta
- `extra = 3` para exibir tres linhas adicionais de escolha
- `fieldsets` para organizar campos da pergunta
- `list_display` com colunas:
	- `question_text`
	- `pub_date`
	- `was_published_recently`
- `list_filter = ["pub_date"]`
- `search_fields = ["question_text"]`

### Melhorias no modelo para o admin

Arquivo `polls/models.py`:

- adicionado `@admin.display(...)` em `was_published_recently()` para:
	- mostrar icone booleano
	- permitir ordenacao por `pub_date`
	- usar descricao de coluna `Published recently?`

### Customizacao visual do cabecalho do admin

Arquivo `session15/settings.py`:

- `TEMPLATES[0]["DIRS"]` atualizado para incluir `BASE_DIR / "templates"`

Arquivo criado `templates/admin/base_site.html`:

- sobrescreve o bloco `branding`
- titulo exibido: `Polls Administration`

### Validacao

```bash
uv run python manage.py check
uv run python manage.py test polls
```

Resultado obtido:

- check sem problemas
- 12 testes executados, todos `OK`

## Parte 8: Pacotes de Terceiros (Django Debug Toolbar)

Nesta etapa, adicionamos um pacote de terceiros para depuracao da aplicacao: Django Debug Toolbar.

### Instalacao com uv

```bash
uv add django-debug-toolbar
```

Dependencia adicionada em `pyproject.toml`:

- `django-debug-toolbar>=6.2.0`

### Configuracao no projeto

Arquivo `session15/settings.py`:

- adiciona `debug_toolbar` em `INSTALLED_APPS` quando `DEBUG` esta ativo
- adiciona middleware `debug_toolbar.middleware.DebugToolbarMiddleware` quando `DEBUG` esta ativo
- define `INTERNAL_IPS = ["127.0.0.1"]`

Arquivo `session15/urls.py`:

- inclui as rotas da toolbar em `__debug__/` quando `DEBUG` esta ativo

### Como validar

```bash
uv run python manage.py runserver
```

Abra no navegador:

- http://127.0.0.1:8000/admin/

Com a pagina carregada, o handle da Debug Toolbar deve aparecer no lado direito.

### Verificacao tecnica

```bash
uv run python manage.py check
uv run python manage.py test polls
```

Resultado obtido:

- check sem problemas
- 12 testes executados, todos `OK`
