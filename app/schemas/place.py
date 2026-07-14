from pydantic import BaseModel


class PlaceSearchItem(BaseModel):
    id: int
    content_id: str
    title: str
    address: str
