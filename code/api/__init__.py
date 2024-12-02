from fastapi import APIRouter
from .message_router import router as message_router

router = APIRouter()

router.include_router(message_router, prefix="")