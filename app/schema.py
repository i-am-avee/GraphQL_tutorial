import strawberry
from app.types.user_type import UserType
from app.types.user_input import UserInput
from app.resolvers.user_resolver import me, get_users, create_user, update_user, delete_user, get_user_by_id


@strawberry.type
class Query:
    users: list[UserType] = strawberry.field(resolver=get_users, description="Fetch all users")
    userById: UserType = strawberry.field(resolver=get_user_by_id, description="Fetch a user by ID")
    meUser: UserType = strawberry.field(resolver=me, description="Fetch the authenticated user's profile")

@strawberry.type
class Mutation:
    createUser: UserType = strawberry.field(resolver=create_user, description="Create a new user")
    updateUser: UserType = strawberry.field(resolver=update_user, description="Update user profile information")
    deleteUser: bool = strawberry.field(resolver=delete_user, description="Delete a user by ID")

schema = strawberry.Schema(query=Query, mutation=Mutation)