from fastapi import APIRouter
from .schemas import RatingSchema
from .service import submit_rating, list_ratings

router = APIRouter()


@router.post("/submit")
def rate_user(rating: RatingSchema):
    return submit_rating(rating)


@router.get("/")
def get_ratings():
    return list_ratings()