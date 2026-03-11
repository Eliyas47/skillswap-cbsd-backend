from fastapi import FastAPI
from app.components.auth.router import router as auth_router
from app.components.users.router import router as users_router

app = FastAPI(title="Skill Swap API")

app.include_router(auth_router)
app.include_router(users_router)


@app.get("/")
def home():
    return {"message": "Skill Swap Backend Running"}

from app.components.auth.router import router as auth_router

app = FastAPI(title="Skill Swap Backend")

app.include_router(auth_router, prefix="/auth", tags=["Auth"])


@app.get("/")
def root():
    return {"message": "Skill Swap Backend Running"}

from app.components.skill.router import router as skill_router

app.include_router(skill_router, prefix="/skill", tags=["Skill"])