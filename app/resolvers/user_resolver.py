import strawberry

from app.auth.auth import hash_password
from app.db.database import SessionLocal
from app.db.user_entity import UserEntity
from app.types.user_type import UserType
from app.types.skill_type import SkillType
from app.types.user_input import UserInput, UpdateUserInput
from app.auth.dependencies import get_current_user
from strawberry.types import Info
from app.db.skill_entity import SkillEntity
from app.db.user_skill_link import UserSkillLink

def get_authenticated_user(info: Info) -> UserType:
    """Retrieve the currently authenticated user from the request context."""
    request = info.context["request"]
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise Exception("Authorization header missing or invalid")
    token = auth_header.split("Bearer ", 1)[1]
    user = get_current_user(token)
    return user


def me(info: Info) -> UserType:
    """Fetch the authenticated user's profile."""
    auth_user = get_authenticated_user(info)
    db = SessionLocal()
    user = db.query(UserEntity).filter(UserEntity.id == auth_user.id).first()
    skills = [
        SkillType(id=link.skill.id, name=link.skill.name)
        for link in user.skill_links if link.skill
    ]
    db.close()
    return UserType(id=user.id, name=user.name, email=user.email, bio=user.bio, skills=skills)

def get_users() -> list[UserType]:
    """Fetch all users from the database."""
    db = SessionLocal()
    users = db.query(UserEntity).all()
    result = []
    for user in users:
        skills = [
            SkillType(id=link.skill.id, name=link.skill.name)
            for link in user.skill_links if link.skill
        ]
        result.append(
            UserType(id=user.id, name=user.name, email=user.email, bio=user.bio, skills=skills)
        )
    db.close()
    return result

def get_user_by_id(id: int) -> UserType:
    """Fetch a user by ID."""
    db = SessionLocal()
    user = db.query(UserEntity).filter(UserEntity.id == id).first()
    if not user:
        raise ValueError("User not found")
    skills = [
        SkillType(id=link.skill.id, name=link.skill.name)
        for link in user.skill_links if link.skill
    ]
    db.close()
    return UserType(id=user.id, name=user.name, email=user.email, bio=user.bio, skills=skills)

def create_user(input: UserInput) -> UserType:
    """Create a new user with hashed password."""
    db = SessionLocal()
    hashed_pw = hash_password(input.password)
    new_user = UserEntity(name=input.name, email=input.email, bio=input.bio, password=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    for skill_name in input.skills:
        skill = db.query(SkillEntity).filter(SkillEntity.name == skill_name).first()
        if skill:
            link = UserSkillLink(user_id=new_user.id, skill_id=skill.id)
            db.add(link)
    db.commit()
    db.refresh(new_user)
    skills = [
        SkillType(id=link.skill.id, name=link.skill.name)
        for link in new_user.skill_links if link.skill
    ]
    db.close()
    return UserType(id=new_user.id, name=new_user.name, email=new_user.email, bio=new_user.bio, skills=skills)

def update_user(info: Info, input: UpdateUserInput) -> UserType:
    """Update user profile information."""
    auth_user = get_authenticated_user(info)
    if auth_user.id != input.id:
        raise Exception("You can only update your own profile")
    db = SessionLocal()
    user = db.query(UserEntity).filter(UserEntity.id == input.id).first()
    if not user:
        db.close()
        raise ValueError("User not found")
    if input.name: user.name = input.name
    if input.email: user.email = input.email
    if input.bio: user.bio = input.bio
    if input.skills:
        # Clear existing skills
        db.query(UserSkillLink).filter(UserSkillLink.user_id == user.id).delete()
        for skill_name in input.skills:
            skill = db.query(SkillEntity).filter(SkillEntity.name == skill_name).first()
            if skill:
                link = UserSkillLink(user_id=user.id, skill_id=skill.id)
                db.add(link)
    db.commit()
    db.refresh(user)
    skills = [
        SkillType(id=link.skill.id, name=link.skill.name)
        for link in user.skill_links if link.skill
    ]
    db.close()
    return UserType(id=user.id, name=user.name, email=user.email, bio=user.bio, skills=skills)

def delete_user(info:Info, user_id: int) -> bool:
    """Delete a user profile."""
    auth_user = get_authenticated_user(info)
    if auth_user.id != user_id:
        raise Exception("You can only delete your own profile")

    db = SessionLocal()
    user = db.query(UserEntity).filter(UserEntity.id == user_id).first()
    if not user:
        db.close()
        return False

    # Delete all skill links associated with the user
    db.query(UserSkillLink).filter(UserSkillLink.user_id == user_id).delete()

    db.delete(user)
    db.commit()
    db.close()
    return True
