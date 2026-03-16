from fastapi import APIRouter
from .schemas import MessageSchema
from .service import send_message, get_messages

router = APIRouter()


@router.post("/send")
def send_chat_message(message: MessageSchema):
    return send_message(message)


@router.get("/")
def retrieve_messages():
    return get_messages()