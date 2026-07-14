import logging

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import search_places
from app.services.llm_service import generate_answer

router = APIRouter(prefix="/chat", tags=["chat"])
logger = logging.getLogger(__name__)


@router.post("", response_model=ChatResponse)
def chat(payload: ChatRequest, db: Session = Depends(get_db)):
    logger.info("CHAT_REQUEST query=%r", payload.query)
    result = search_places(db, payload.query)
    answer = generate_answer(payload.query, result)
    logger.info(
        "CHAT_RESPONSE status=SUCCESS result_count=%d answer=%r",
        result["resultCount"],
        answer,
    )
    return ChatResponse(answer=answer)
