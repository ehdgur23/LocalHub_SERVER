from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    query: str = Field(..., min_length=1, description="사용자의 자연어 질문")


class ChatResponse(BaseModel):
    answer: str
