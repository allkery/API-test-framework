from pydantic import BaseModel, Field


class AlbumSchema(BaseModel):
    userId: int = Field(ge=1)
    id: int = Field(ge=1)
    title: str