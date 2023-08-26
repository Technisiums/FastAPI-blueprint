from fastapi import APIRouter, Depends
from fastapi import status
from app.schemas.auth_schemas import UserBase
from typing import Annotated
from app.utils.auth import get_current_active_user
router = APIRouter()


@router.get('/healthcheck', status_code=status.HTTP_200_OK)
def health_check(current_user: Annotated[UserBase, Depends(get_current_active_user)]):
    return {"status": "OK"}
