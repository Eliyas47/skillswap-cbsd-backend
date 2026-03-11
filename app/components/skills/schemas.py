from pydantic import BaseModel


class SkillCreate(BaseModel):
    skill_name: str
    description: str