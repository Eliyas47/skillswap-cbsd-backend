from fastapi import APIRouter
from .schemas import SwapRequestSchema
from .service import create_swap_request, list_swap_requests

router = APIRouter()


@router.post("/request")
def send_swap_request(request: SwapRequestSchema):
    return create_swap_request(request)


@router.get("/")
def get_swap_requests():
    return list_swap_requests()