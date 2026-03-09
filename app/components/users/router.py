from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
def get_users():
    return {"message": "List of users placeholder"}


@router.get("/profile")
def view_profile():
    return {"message": "User profile placeholder"}