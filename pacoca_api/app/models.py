from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Pacoca(Base):
    __tablename__ = "pacocas"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float, index=True)
