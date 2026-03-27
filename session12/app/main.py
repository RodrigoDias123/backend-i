from fastapi import FastAPI
from app.api.routers.action_items import router as action_items_router

app = FastAPI(title="Session 12 - Filters, Sorting, and Pagination")

app.include_router(action_items_router)
