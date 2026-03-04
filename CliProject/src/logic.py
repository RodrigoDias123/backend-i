from datetime import datetime

def add_friend(name, birthdate):
    """Valida se a data está no formato correto."""
    try:
        datetime.strptime(birthdate, '%Y-%m-%d')
        return name, birthdate
    except ValueError:
        raise ValueError("A data tem de estar no formato AAAA-MM-DD (ex: 1990-12-05).")

def calculate_days_until_birthday(birthdate_str, today_str):
    """Calcula quantos dias faltam para o próximo aniversário."""
    birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')
    today = datetime.strptime(today_str, '%Y-%m-%d')
    
    next_birthday = birthdate.replace(year=today.year)
    
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)
    
    return (next_birthday - today).days

def filter_upcoming_birthdays(friends, days):
    """Filtra e devolve os amigos que fazem anos nos próximos X dias."""
    upcoming_friends = []
    today_str = datetime.now().strftime('%Y-%m-%d')
    
    for name, birthdate in friends.items():
        days_until_birthday = calculate_days_until_birthday(birthdate, today_str)
        if days_until_birthday <= days:
            upcoming_friends.append((name, birthdate, days_until_birthday))

    upcoming_friends.sort(key=lambda x: x[2])
    return upcoming_friends

def sort_birthdays(friends):
    """Ordena a lista geral de amigos apenas por mês e dia (para fazer um calendário)."""
    return sorted(
        friends.items(), 
        key=lambda x: (
            datetime.strptime(x[1], '%Y-%m-%d').month,
            datetime.strptime(x[1], '%Y-%m-%d').day
        )
    )


def sort_birthdays(friends):
    return sorted(
        friends.items(), 
        key=lambda x: (
            datetime.strptime(x[1], '%Y-%m-%d').month,
            datetime.strptime(x[1], '%Y-%m-%d').day
        )
    )
