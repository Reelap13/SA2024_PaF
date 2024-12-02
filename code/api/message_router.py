from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from queues import queue_api_filter

router = APIRouter()

class MessageRequest(BaseModel):
    message: str

@router.post("/process")
async def process_message(request: MessageRequest):
    if not request.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty.")
    queue_api_filter.put(request.message)
    return {"status": "accepted", "message": request.message}
