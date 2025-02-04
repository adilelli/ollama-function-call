from pydantic import BaseModel


class request_dto(BaseModel):
    text: str

class attraction(BaseModel):
    description: str