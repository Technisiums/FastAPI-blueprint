import uuid
from sqlalchemy import Column, String, DateTime, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
import datetime

from app.schemas.person_schemas import Gender
Base = declarative_base()




class Persons(Base):
    __tablename__ = "persons"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, comment="")
    name = Column(String, comment="Name of the Person", nullable=False)
    gender = Column(Enum(Gender), comment="Gender of the person")
    created_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False,comment="Date of Creation")


class Teachers(Base):
    __tablename__ = "teachers"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, comment="")
    name = Column(String, comment="Name of the Teacher", nullable=False)
    gender = Column(Enum(Gender), comment="Gender of the person")
    created_at = Column(DateTime, default=datetime.datetime.utcnow, nullable=False,comment="Date of Creation")

