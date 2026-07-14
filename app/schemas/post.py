from datetime import datetime

from pydantic import BaseModel, Field


class PostCreateResponse(BaseModel):
    id: int
    message: str


class PostListItem(BaseModel):
    id: int
    title: str
    nickname: str
    place_id: int
    image_count: int
    created_at: datetime


class PostListResponse(BaseModel):
    total: int
    items: list[PostListItem]


class PostImageItem(BaseModel):
    image_id: int


class PostDetailResponse(BaseModel):
    id: int
    title: str
    content: str
    nickname: str
    place_id: int
    images: list[PostImageItem]


class PostDeleteRequest(BaseModel):
    password: str = Field(min_length=1)
