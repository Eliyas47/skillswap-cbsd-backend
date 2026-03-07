from fastapi import FastAPI
from app.components.auth.router import router as auth_router

app = FastAPI(title="Skill Swap API")

app.include_router(auth_router)


@app.get("/")
def home():
    return {"message": "Skill Swap Backend Running"}