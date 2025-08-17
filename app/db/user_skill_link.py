from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.db.database import Base
# from app.db.skill_entity import SkillEntity
# from app.db.user_entity import UserEntity

class UserSkillLink(Base):
    __tablename__ = "user_skill_link"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    skill_id = Column(Integer, ForeignKey("skills.id"), primary_key=True)

    user = relationship("UserEntity", back_populates="skill_links")
    skill = relationship("SkillEntity")