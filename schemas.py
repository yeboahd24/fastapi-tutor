from pydantic import BaseModel, ConfigDict, Field


# This matches what is in the database
class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=50)


# Acting like DTO
class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)

    # fields that are not provided by the client but by the server
    id: int
    date_posted: str
