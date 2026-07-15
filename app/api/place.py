from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.place import PlaceCategoryListResponse
from app.services.place_service import list_places_by_category


router = APIRouter(prefix="/places", tags=["places"])


@router.get("/category", response_model=PlaceCategoryListResponse)
def read_places_by_category(
    contentTypeId: int = Query(..., description="contentTypeId 값, 예: 12(관광지), 14(문화시설)"),
    page: int = Query(1, ge=1),
    page_size: int = Query(4, ge=1, le=20),
    db: Session = Depends(get_db),
) -> PlaceCategoryListResponse:
    result = list_places_by_category(db, contentTypeId, page=page, page_size=page_size)
    return PlaceCategoryListResponse(**result)
