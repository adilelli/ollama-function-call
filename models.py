from pydantic import BaseModel


class request_dto(BaseModel):
    text: str

class attraction(BaseModel):
    description: str

class education(BaseModel):
    description: str

class food(BaseModel):
    description: str

class healthcare(BaseModel):
    description: str

class housing(BaseModel):
    description: str

class infra(BaseModel):
    description: str

class transport(BaseModel):
    description: str

class utilities(BaseModel):
    description: str