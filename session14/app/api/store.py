from itertools import count

from app.api.schemas import Item, ItemCreate, ItemUpdate


class ItemStore:
    def __init__(self) -> None:
        self._items: dict[int, Item] = {}
        self._ids = count(start=1)

    def list(self, search: str | None = None, skip: int = 0, limit: int = 10) -> list[Item]:
        items = list(self._items.values())
        if search:
            normalized = search.lower()
            items = [
                item
                for item in items
                if normalized in item.name.lower()
                or (item.description and normalized in item.description.lower())
            ]
        return items[skip : skip + limit]

    def create(self, payload: ItemCreate) -> Item:
        item = Item(id=next(self._ids), **payload.model_dump())
        self._items[item.id] = item
        return item

    def get(self, item_id: int) -> Item | None:
        return self._items.get(item_id)

    def update(self, item_id: int, payload: ItemUpdate) -> Item | None:
        current = self.get(item_id)
        if current is None:
            return None
        updated = current.model_copy(update=payload.model_dump(exclude_none=True))
        self._items[item_id] = updated
        return updated

    def delete(self, item_id: int) -> bool:
        return self._items.pop(item_id, None) is not None


store = ItemStore()