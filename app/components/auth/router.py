from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.get("/")
def auth_test():
    return {"message": "Auth component initialized"}