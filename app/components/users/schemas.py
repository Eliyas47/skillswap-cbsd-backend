from pydantic import BaseModel


class UserProfile(BaseModel):
    username: str
    email: str
    bio: str | None = None