from pydantic import BaseModel

class PacocaBase(BaseModel):
    name: str
    description: str
    price: float

class PacocaCreate(PacocaBase):
    pass

class Pacoca(PacocaBase):
    id: int

    class Config:
        from_attributes = True
