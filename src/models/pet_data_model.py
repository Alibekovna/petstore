from pydantic import BaseModel, validator
from typing import Optional, List, Literal


class NewPet(BaseModel):
    id: int
    category: Optional[dict]
    name: Optional[str]
    photoUrls: List[str]
    tags: List[dict]
    status: Literal['sold', 'pending', 'available']

    @validator('id')
    def id_must_be_6_digits(cls, v):
        if len(str(v)) != 6:
            raise ValueError('must be 6 digits')
        return v


