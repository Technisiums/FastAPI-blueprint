from fastapi import APIRouter, Depends
from fastapi import status
from app.schemas.auth_schemas import UserBase
from typing import Annotated, List
from app.utils.auth import get_current_active_user
from app.services.person_service import get_persons_by_name, save_person
from app.schemas.person_schemas import GetPersonResponse, PostPersonRequest
router = APIRouter()


@router.get('/persons', status_code=status.HTTP_200_OK,response_model=List[GetPersonResponse])
def persons_by_name(name, current_user: Annotated[UserBase, Depends(get_current_active_user)]):
    return get_persons_by_name(name)


@router.post('/persons', status_code=status.HTTP_201_CREATED)
def add_person(person: PostPersonRequest, current_user: Annotated[UserBase, Depends(get_current_active_user)]):

    return save_person(person)
