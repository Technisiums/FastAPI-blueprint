from fastapi_sqlalchemy import db
from app.database.models import Persons
from uuid import uuid4


class TestDataHandler():

    @staticmethod
    def add_persons(quantity: int = 5) -> list:
        ids = []
        with db():
            for _ in range(quantity):
                uuid = uuid4()
                db.session.add(Persons(
                    id=uuid,
                    name='created by test',
                    gender='male'))
                ids.append(uuid)
            db.session.commit()
        return ids


test_data_handler = TestDataHandler()