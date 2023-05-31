from typing import Optional

from sqlmodel import SQLModel, Field
from sqlmodel import create_engine, Session

# class User(SQLModel, table=True, extend_existing=True):
#     id: Optional[int] = Field(default=None, primary_key=True)
#     username: str
#     email: str
#     password: str

# engine = create_engine("sqlite:///database.db")
# SQLModel.metadata.create_all(engine)

# user = User(username="jean_pierre", email="jean.pierre@example.com", password="azerty")
# with Session(engine) as session:
#     session.add(user)
#     session.commit()


class User(SQLModel, table=True, extend_existing=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str
    password: str
