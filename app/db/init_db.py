from app.db.database import Base, engine
from app.db.database import SessionLocal
from app.db.skill_entity import SkillEntity

def init_db():
    Base.metadata.create_all(bind=engine)

def seed_skills():
    db = SessionLocal()

    skills = [
        "Python",
        "FastAPI",
        "GraphQL",
        "Docker",
        "SQL",
        "Git",
        "REST APIs"
    ]

    for name in skills:
        existing = db.query(SkillEntity).filter(SkillEntity.name == name).first()
        if not existing:
            db.add(SkillEntity(name=name))

    db.commit()
    db.close()
    print("✅ Skills seeded successfully.")


if __name__ == "__main__":
    init_db()
    seed_skills()

