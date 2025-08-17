import strawberry
from app.db.database import SessionLocal
from app.types.skill_type import SkillType
from app.db.user_entity import UserEntity

@strawberry.type
class UserType:
    id: int = strawberry.field(description="Unique identifier for the user")
    name: str = strawberry.field(description="Name of the user")
    email: str = strawberry.field(description="Email address of the user")
    bio: str = strawberry.field(description="Short biography of the user", default="")
    skills: list[SkillType] | None = strawberry.field(description="List of skills associated with the user", default=None)
    # @strawberry.field
    # def skills(self) -> list[SkillType]:
    #     db = SessionLocal()
    #     user = db.query(UserEntity).filter(UserEntity.id == self.id).first()
    #     db.close()
    #     return [
    #         SkillType(id=link.skill.id, name=link.skill.name)
    #         for link in user.skill_links
    #     ]
