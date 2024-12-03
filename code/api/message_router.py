from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from queues import queue_api_filter
from datetime import datetime
from schemas.message_scheme import MessageScheme

router = APIRouter()

class MessageRequest(BaseModel):
    message: str

@router.post("/process")
async def process_message(request: MessageRequest):
    if not request.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty.")
    
    message = MessageScheme(text=request.message, timestamp=datetime.now())
    queue_api_filter.put(message)
    return {"status": "accepted", "message": request.message}
