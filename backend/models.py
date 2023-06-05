from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel, Field
from sqlmodel import create_engine, Session

import sqlite3


class User(SQLModel, table=True, extend_existing=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str
    password: str
    

class Link(SQLModel, table=True, extend_existing=True):
    id: int = Field(primary_key=True)
    url: str
    description: str
    timestamp: datetime = Field(default=datetime.now().replace(second=0, microsecond=0))
    user_id: int = Field(foreign_key="user.id")


database_url = "sqlite:///backend/database.db"
engine = create_engine(database_url)
SQLModel.metadata.create_all(engine)
