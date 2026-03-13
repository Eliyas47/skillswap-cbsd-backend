from pydantic import BaseModel


class SwapRequestSchema(BaseModel):
    requester_id: int
    receiver_id: int
    skill_offered: str
    skill_requested: str