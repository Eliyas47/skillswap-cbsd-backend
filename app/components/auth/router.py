from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def test_auth():
    return {"message": "Auth component working"}