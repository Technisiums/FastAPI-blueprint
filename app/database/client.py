from typing import List

from fastapi_sqlalchemy import db
from app.database.models import Persons


class DBClient:

    @staticmethod
    def get_persons_by_name(name: str) -> List[Persons]:
        with db():
            persons = db.session.query(Persons).filter(Persons.name.match(f'%{name}%')).all()
            return persons

    @staticmethod
    def save_person(person: Persons):
        with db():
            db.session.add(person)
            db.session.commit()

db_client = DBClient()