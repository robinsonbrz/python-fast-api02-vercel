from typing import Optional

from pydantic import BaseModel


class NoteSchema(BaseModel):
    title: Optional[str]
    content: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "Título da nota.",
                "content": "Exemplo de nota."
            }
        }
