from typing import List, Optional

from pydantic import BaseModel, Field, field_validator
from typing_extensions import NotRequired, Required
from typing_extensions import TypedDict

from app.schemas.common_schemas import ErrorCodeCommon
from app.utils.conditional_check_utils import conditional_check
from app.utils.exception_utils import ValidationException

from datetime import datetime
from dataclasses import dataclass

class Schedule(TypedDict):
    process_id: str
    schedule: str


class Information(TypedDict):
    company_id: str
    product_id: str

class TimeView(TypedDict):
    start_date: str
    end_date: str

class InfoScheduleRequest(BaseModel):
    request_id: str = Field(
        description="request ID"
    )
    information: Information = Field(
        description="Information"
    )
    timeview: TimeView = Field(
        description="Time view"
    )
    timestamp: int = Field(
        description="Timestamp"
    )

    @field_validator("information")
    def validate_information(cls, v):
        product_id = v['product_id']

        if conditional_check.is_null(product_id):
            raise ValidationException(
                message="Empty input : product_id"
                , errors=ErrorCodeCommon.CMN_VAL_001.name
            )
        
        return v


class InfoScheduleResponse(BaseModel):
    response_id: str
    timestamp: int
    status: str
    information: Optional[Information] = None
    message: Optional[str] = None
    error_code: Optional[str] = None

