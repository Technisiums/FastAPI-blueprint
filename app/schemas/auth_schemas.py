from typing import Union

from pydantic import BaseModel, Field, SecretStr


class UserBase(BaseModel):
    username: str = Field(name='User Name')
    full_name: str = Field(name='Full Name')
    email: str = Field(name='Email Address')
    disabled: bool = Field(name='User Status', description='If True user is disabled')


class User(UserBase):
    hashed_password: str = Field(name='Hashed Password')


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None
