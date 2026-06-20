from pydantic import BaseModel, Field


class PhotoSchema(BaseModel):
    albumId: int = Field(ge=1)
    id: int = Field(ge=1)
    title: str
    url: str
    thumbnailUrl: str