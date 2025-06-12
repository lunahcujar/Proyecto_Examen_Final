from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum as SqlEnum
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import relationship
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

from dbconecttion import Base, engine



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    mail = Column(String, nullable=False)
    image_url = Column(String, nullable=True)



class UserCreate(BaseModel):
    name: str
    mail: str
    image_url: Optional[str] = None

    class Config:
        orm_mode = True


