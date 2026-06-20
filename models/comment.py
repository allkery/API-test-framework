from pydantic import BaseModel, Field, EmailStr


class CommentSchema(BaseModel):
    postId: int = Field(ge=1)
    id : int = Field(ge=1)
    name: str
    email: EmailStr
    body: str
    