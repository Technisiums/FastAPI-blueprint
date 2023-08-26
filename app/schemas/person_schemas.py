from datetime import datetime

from pydantic import BaseModel, Field
from enum import Enum
from uuid import UUID


class Gender(Enum):
    male = "Male"
    female = "Female"
    other = "Other"




class GetPersonResponse(BaseModel):
    id: UUID
    name: str
    gender: Gender
    created_at: datetime


class PostPersonRequest(BaseModel):
    name: str = Field(name="Name")
    gender: Gender = Field(name="Name")
