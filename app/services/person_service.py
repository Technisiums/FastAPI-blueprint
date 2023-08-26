from typing import List

from app.database.client import db_client
from app.schemas.person_schemas import PostPersonRequest, GetPersonResponse
from app.database.models import Persons
import uuid


def get_persons_by_name(name) -> List[GetPersonResponse]:
    persons = db_client.get_persons_by_name(name)
    resp = []
    for person in persons:
        resp.append(GetPersonResponse(id=person.id,
                                      name=person.name,
                                      gender=person.gender,
                                      created_at=person.created_at))
    return resp


def save_person(request: PostPersonRequest):
    person = Persons(
        id=uuid.uuid4(),
        name=request.name,
        gender=request.gender
    )
    db_client.save_person(person)
