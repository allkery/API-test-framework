from pydantic import BaseModel, ConfigDict, Field

class PostSchema(BaseModel):
    userId: int = Field(ge=0)
    id: int = Field(ge=0)
    title: str
    body: str

    model_config = ConfigDict(extra="forbid")