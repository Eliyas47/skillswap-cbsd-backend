from fastapi import FastAPI
from app.components.auth.router import router as auth_router
from app.components.users.router import router as users_router

app = FastAPI(title="Skill Swap API")

app.include_router(auth_router)
app.include_router(users_router)


@app.get("/")
def home():
    return {"message": "Skill Swap Backend Running"}