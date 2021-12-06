from db.models.users import User
from sqlalchemy.orm import Session


def get_user(db: Session, username: str):
    user = db.query(User).filter(User.email == username).first()
    return user
