from fastapi import FastAPI
from app.api.routers.action_items import router as action_items_router
from app.api.routers.action_items import meetings_store

app = FastAPI()

app.include_router(action_items_router)

# Seed a meeting so the example from the exercise works
meetings_store["abc-123"] = {"id": "abc-123", "title": "Demo Meeting"}
