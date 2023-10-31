from fastapi import APIRouter

from .endpoint import (
    arrange_schedule
)

api_router = APIRouter()

api_router.include_router(arrange_schedule.router, prefix="/fujin")