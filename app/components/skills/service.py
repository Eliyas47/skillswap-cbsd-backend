def add_skill(skill):
    return {
        "message": "Skill added successfully",
        "skill": skill.skill_name
    }


def list_skills():
    return [
        {"skill": "Python"},
        {"skill": "Graphic Design"}
    ]