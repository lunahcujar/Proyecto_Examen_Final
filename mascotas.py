from typing import Optional

from pydantic import BaseModel, Field


class Pet(BaseModel):
    name:str = Field(..., min_length=3, max_length=20)
    breed: Optional[str] = Field(None, min_length=3, max_length=25)  # Opcional
    birth: Optional[int] = Field(None, gt=2000, lt=2025)  # Opcional
    kind: Optional[str] = Field(None, min_length=3, max_length=25)  # Opcional
    female: Optional[bool] = Field(None)  # Opcional

class PetResponse(BaseModel):
    name:str
    kind:str



class UpdatedPet(BaseModel):
    name: Optional[str] = Field(..., min_length=3, max_length=20)
    breed:Optional[str] = Field(..., min_length=3, max_length=25)
#token: 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
