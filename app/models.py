from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float
from .database import Base
from typing import Optional


# This is the database model which  represents the 'addresses' table in SQLite fdatabase.
class Address(Base):
    __tablename__ = "addresses"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    latitude = Column(Float)
    longitude = Column(Float)




# schema to create a address
class AddressCreate(BaseModel):
    name: str
    latitude: float
    longitude: float


#schema to update a address 
class AddressUpdate(BaseModel):
    name: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
