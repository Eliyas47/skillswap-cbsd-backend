from pydantic import BaseModel
from pydantic import BaseModel, EmailStr

class UserRegister(BaseModel):
    username: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str
