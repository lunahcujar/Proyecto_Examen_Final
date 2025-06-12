from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum as SqlEnum
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import relationship
from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

from dbconecttion import Base, engine



class Vuelo(Base):
    __tablename__ = 'vuelos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    origen = Column(String, nullable=False)
    destino = Column(String, nullable=True)
    date = Column(DateTime, default=datetime.utcnow)



class VueloCreate(BaseModel):
    name: str
    origen: str
    destino: str
    date: datetime

    class Config:
        orm_mode = True