import logging
import os

from fastapi import FastAPI

from app.api.chat import router as chat_router
from app.api.post import router as post_router
from app.db.database import init_db

logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO").upper(),
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

app = FastAPI(title="LocalHub Server")

init_db()
app.include_router(chat_router)
app.include_router(post_router)


@app.get("/")
def read_root() -> dict[str, str]:
    return {
        "message": "LocalHub Server is running",
        "chat_endpoint": "/chat",
    }
