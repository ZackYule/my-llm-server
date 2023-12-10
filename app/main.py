from fastapi import FastAPI
from .routes.chat_routes import router as chat_router

app = FastAPI()

app.include_router(chat_router)
