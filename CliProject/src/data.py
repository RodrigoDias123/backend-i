import json
import os

FILE_PATH = 'aniversarios.json'

def load_birthdays():
    """Lê os dados do ficheiro JSON."""
    if not os.path.exists(FILE_PATH):
        return {}
    
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {}

def save_birthdays(data):
    """Guarda o dicionário no ficheiro JSON."""
    with open(FILE_PATH, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)