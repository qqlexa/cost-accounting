from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.category import Category
from schemas.item import ItemCreate
import models.item
from crud.crud_user import get_user
from models.user import User


def create_user_item(db: Session, item: ItemCreate, user_id: int):
    if get_user(db, user_id) is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_item = models.item.Item(**item.dict())
    db_item.user_id = user_id
    user = db.query(User).join(Category, Category.user_id == User.id).filter(Category.id == db_item.category_id).all()
    if user is not None:
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    else:
        raise HTTPException(status_code=404, detail="You have no such category")
