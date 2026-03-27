# Session 16 | Django Admin


Django project for Session 16 focused on configuring Django Admin for the `Meeting` model.

## Project Structure

```text
.
├── db.sqlite3
├── exercise.md
├── manage.py
├── meetings
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── management
│   │   └── commands
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── templates
│   │   ├── index.html
│   │   └── meetings
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── pyproject.toml
├── .python-version
├── README.md
├── session16
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── uv.lock
```

## Exercise Objective

Configure the admin to:

- register the `Meeting` model
- show `id`, `title`, `date`, and `owner` in the list view
- allow search by title and owner
- allow filtering by date and owner
- order by newest date first

## Requirements

- Python 3.14+
- `uv` installed

## Installation

```bash
uv sync
```

## Run Migrations

```bash
uv run python manage.py migrate
```

## Create Superuser

```bash
uv run python manage.py createsuperuser
```

## Start the Server

```bash
uv run python manage.py runserver
```

Admin available at:

`http://127.0.0.1:8000/admin`

## Implemented Admin Configuration

In `MeetingAdmin`:

- `list_display = ("id", "title", "date", "owner")`
- `list_filter = ("date", "owner")`
- `search_fields = ("title", "owner__username")`
- `ordering = ("-date",)`

## How to Validate

1. Open the admin and sign in with a superuser account.
2. Verify the meetings list shows the expected columns.
3. Test search by title and by the owner's username.
4. Test filters by date and owner.
5. Create, edit, and delete meetings in admin.

## Technical Check

```bash
uv run python manage.py check
```

Expected output:

`System check identified no issues (0 silenced).`
