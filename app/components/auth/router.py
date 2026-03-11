from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.get("/")
def auth_test():
    return {"message": "Auth component initialized"}
from fastapi import APIRouter
from .schemas import UserRegister, UserLogin
from .service import register_user, login_user

router = APIRouter()


@router.post("/register")
def register(user: UserRegister):
    return register_user(user)


@router.post("/login")
def login(user: UserLogin):
    return login_user(user)