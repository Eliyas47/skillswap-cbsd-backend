from fastapi import APIRouter
from .schemas import SkillCreate
from .service import add_skill, list_skills

router = APIRouter()


@router.post("/add")
def create_skill(skill: SkillCreate):
    return add_skill(skill)


@router.get("/")
def get_skills():
    return list_skills()