from .memory_store import meetings

def list_meetings() -> None:
    if not meetings:
        print("Não existem reuniões.")
        return

    for meeting in meetings:
        total_items = len(meeting.action_items)
        done_items = sum(1 for item in meeting.action_items if item.status.lower() == "done")
        open_items = total_items - done_items

        print("=" * 40)
        print(f"ID da Reunião : {meeting.id}")
        print(f"Título        : {meeting.title}")
        print(f"Data          : {meeting.date}")
        print(f"Responsável   : {meeting.owner}")
        print(f"Participantes : {', '.join(meeting.participants) or 'Nenhum'}")
        print(f"Itens de Ação : {total_items} (abertos: {open_items}, concluídos: {done_items})")

        if not meeting.action_items:
            print("  Sem itens de ação.")
            continue

        for i, action in enumerate(meeting.action_items, start=1):
            print(f"  {i}. {action.description}")
            print(f"     Dono   : {action.owner}")
            print(f"     Prazo  : {action.due_date}")
            print(f"     Estado : {action.status}")
