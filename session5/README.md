# Action Item CLI


CLI para gerenciamento de itens de ação com validação robusta de campos obrigatórios e formato de data.

## Requisitos

- Python 3.14+
- uv (gerenciador de pacotes Python)

## Instalação

```bash
uv sync
```

## Uso

### Criar um item de ação

```bash
uv run python app/cli.py create-action-item --description "Descrição" --owner "Nome" --due-date "YYYY-MM-DD"
```

### Exemplos

#### ✅ Sucesso

```bash
uv run python app/cli.py create-action-item --description "Do something" --owner "Jorge" --due-date "2026-03-15"
# Output: Action item created successfully
# Exit code: 0
```

#### ❌ Erro: Owner ausente

```bash
uv run python app/cli.py create-action-item --description "Do something" --due-date "2026-03-15"
# Output: Validation error: 'owner' is required
# Exit code: 1
```

#### ❌ Erro: Formato de data inválido

```bash
uv run python app/cli.py create-action-item --description "Do something" --owner "Jorge" --due-date "15-03-2026"
# Output: Validation error: Date must be YYYY-MM-DD
# Exit code: 1
```

#### ❌ Erro: Due date ausente

```bash
uv run python app/cli.py create-action-item --description "Do something" --owner "Jorge"
# Output: Validation error: 'due_date' is required
# Exit code: 1
```

## Estrutura do Projeto

```
app/
├── __init__.py
├── cli.py                      # Interface CLI
├── core/
│   ├── __init__.py
│   ├── errors.py              # Classes de exceção customizadas
│   └── validators.py          # Funções de validação
└── services/
    ├── __init__.py
    └── action_item_service.py # Serviço de criação de itens
```

## Validações

- **owner**: Campo obrigatório
- **due_date**: Campo obrigatório com formato YYYY-MM-DD
- **description**: Campo obrigatório (argumento posicional)

## Códigos de Saída

- `0`: Sucesso
- `1`: Erro de validação
