import inspect
import uuid
from dataclasses import dataclass
from enum import IntEnum
from typing import List, Dict, Optional
from fastapi import status

from pydantic import BaseModel


class SeverityEnum(IntEnum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3


@dataclass
class Error:
    code: str
    severity: SeverityEnum
    message: str
    http_error_code: int

    @classmethod
    def from_dict(cls, env):
        return cls(**{
            k: v for k, v in env.items()
            if k in inspect.signature(cls).parameters
        })


@dataclass
class Errors:
    error_list: List[Error]


class ErrorResponse(BaseModel):
    id: uuid.UUID
    code: str
    severity: SeverityEnum
    title: str
    detail: Optional[str]
    meta: Optional[Dict]


class ErrorsResponse(BaseModel):
    errors: List[ErrorResponse]


class MyBaseException(Exception):
    def __init__(self, error_code: str, exception: BaseException = None, severity: SeverityEnum = 0,
                 message: str = None, http_error_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR):
        super().__init__(error_code, exception, severity, message)
        self.error = Error(code=error_code, severity=severity, message=message, http_error_code=http_error_code)


def prepare_errors_response(my_base_exception: MyBaseException):
    error_response = None
    if isinstance(my_base_exception, MyBaseException):
        error = my_base_exception.error
        error_response = ErrorResponse(id=uuid.uuid4(), code=error.code, severity=error.severity, title=error.message)
        error_response = ErrorsResponse(errors=[error_response])
        return error_response.json()
    return error_response
