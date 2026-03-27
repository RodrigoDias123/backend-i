# Session 17 - Authentication and Permissions

Projeto Django para configurar grupos e permissões do app meetings, com foco no requisito principal:
o grupo editor pode visualizar e editar reuniões, mas nao pode deletar.

## Objetivo do exercicio

Configurar tres grupos de usuario:

- admin
- editor
- viewer

Permissoes esperadas:

- admin: view, change e delete de meeting
- editor: view e change de meeting (sem delete)
- viewer: apenas view de meeting

## Tecnologias

- Python 3.14
- Django 6.0.3
- uv

## Estrutura principal

- manage.py
- config/settings.py
- meetings/models.py
- meetings/management/commands/create_groups.py

## Como rodar o projeto

1. Instalar dependencias

```bash
uv sync
```

2. Criar migracoes

```bash
uv run python manage.py makemigrations
```

3. Aplicar migracoes

```bash
uv run python manage.py migrate
```

4. Criar grupos e permissoes

```bash
uv run python manage.py create_groups
```

5. Criar usuario admin (superuser)

```bash
uv run python manage.py createsuperuser
```

Depois, acesse o painel admin em http://127.0.0.1:8000/admin.

## Comando de grupos

O comando abaixo cria os grupos admin, editor e viewer e atribui as permissoes do modelo Meeting:

```bash
uv run python manage.py create_groups
```

Ele usa os codenames:

- view_meeting
- change_meeting
- delete_meeting

## Testes manuais no shell

Abrir shell Django:

```bash
uv run python manage.py shell
```

### Verificar grupos e permissoes

```python
from django.contrib.auth.models import Group

print("admin:", sorted(Group.objects.get(name="admin").permissions.values_list("codename", flat=True)))
print("editor:", sorted(Group.objects.get(name="editor").permissions.values_list("codename", flat=True)))
print("viewer:", sorted(Group.objects.get(name="viewer").permissions.values_list("codename", flat=True)))
```

### Verificar regra do editor

```python
from django.contrib.auth.models import User, Group

u, _ = User.objects.get_or_create(username="jorge")
u.set_password("pass123")
u.save()
u.groups.clear()
u.groups.add(Group.objects.get(name="editor"))

print(u.has_perm("meetings.change_meeting"))
print(u.has_perm("meetings.view_meeting"))
print(u.has_perm("meetings.delete_meeting"))
```

Saida esperada:

```text
True
True
False
```

## Comandos rapidos de teste

```bash
uv run python manage.py makemigrations
uv run python manage.py migrate
uv run python manage.py create_groups
uv run python manage.py test
```

## Criar usuario admin

Para criar um usuario com acesso total ao admin do Django:

```bash
uv run python manage.py createsuperuser
```

Preencha username, email (opcional) e senha quando o comando pedir.

## Criterios de sucesso

- Grupos admin, editor e viewer criados
- editor com view e change, sem delete
- viewer apenas com view
- admin com view, change e delete
- verificacao no shell retornando True, True, False para usuario editor
