from sqlalchemy import Column, Integer, String
from app.db.database import Base

class SkillEntity(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
