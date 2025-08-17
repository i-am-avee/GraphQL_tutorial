from fastapi import FastAPI, Request
from app.auth.routes import router as auth_router
from strawberry.fastapi import GraphQLRouter
from app.schema import schema
from fastapi.middleware.cors import CORSMiddleware
from app.db import UserEntity, SkillEntity, UserSkillLink

def get_context(request: Request):
    return {"request": request}

graphql_app = GraphQLRouter(schema,
                            context_getter=get_context,
                            graphql_ide= "apollo-sandbox"
                            )

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth")
app.include_router(graphql_app, prefix="/graphql")

