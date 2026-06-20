from pydantic import BaseModel, Field


class TodoSchema(BaseModel):
    userId: int = Field(ge=1)
    id: int = Field(ge=1)
    title: str
    completed: bool