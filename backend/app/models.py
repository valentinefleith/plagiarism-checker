from pydantic import BaseModel


class TextPost(BaseModel):
    body: str
