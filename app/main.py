from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Skill Swap API"}