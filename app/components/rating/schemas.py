from pydantic import BaseModel


class RatingSchema(BaseModel):
    reviewer_id: int
    reviewed_user_id: int
    score: int
    feedback: str