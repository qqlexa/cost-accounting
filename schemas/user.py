from typing import List

from pydantic import BaseModel

from schemas.item import Item
from schemas.category import Category


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    items: List[Item] = []
    categories: List[Category] = []

    class Config:
        orm_mode = True
