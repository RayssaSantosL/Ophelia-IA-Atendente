#from fastapi import APIRouter
#from app.models.schemas import Message
#from app.core.nlp import chat_with_gpt

#router = APIRouter()

#@router.post("/process_message/")
#async def process_message(message: Message):
#    resposta = chat_with_gpt(message.text)
#    return {"resposta": resposta, "original_message": message.text}



from fastapi import APIRouter
from app.models.schemas import Message
from app.core.nlp import chat_with_gpt_mock  # altere para mock

router = APIRouter()

@router.post("/process_message/")
async def process_message(message: Message):
    resposta = chat_with_gpt_mock(message.text)  # usa a função mock
    return {"resposta": resposta, "original_message": message.text}
