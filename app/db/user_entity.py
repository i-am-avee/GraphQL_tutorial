from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.db.database import Base
# from app.db.user_skill_link import UserSkillLink


class UserEntity(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    bio = Column(Text, nullable=True)
    password = Column(String(255), nullable=False)
    skill_links = relationship("UserSkillLink", back_populates="user")
