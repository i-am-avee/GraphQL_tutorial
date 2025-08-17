import strawberry

@strawberry.input
class UserInput:
    name: str = strawberry.field(description="Name of the user")
    email: str = strawberry.field(description="Email address of the user")
    bio: str = strawberry.field(description="Short biography of the user", default="")
    password: str = strawberry.field(description="Password for the user account")
    skills: list[str] = strawberry.field(description="List of skill names to assign")

@strawberry.input
class UpdateUserInput:
    id: int = strawberry.field(description="Unique identifier for the user")
    name: str | None = strawberry.field(description="Name of the user", default=None)
    email: str | None = strawberry.field(description="Email address of the user", default=None)
    bio: str | None = strawberry.field(description="Short biography of the user", default=None)
    skills: list[str] | None = strawberry.field(description="List of skill names to assign", default=None)