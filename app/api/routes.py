from fastapi import APIRouter
from pydantic import BaseModel
from app.core.nlp import chat_with_gpt

router = APIRouter()

class Message(BaseModel):
    text: str

@router.post("/process_message/")
async def process_message(message: Message):
    resposta = chat_with_gpt(message.text)
    return {"resposta": resposta, "original_message": message.text}
