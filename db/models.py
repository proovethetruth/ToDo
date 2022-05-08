
from db.database import Base
from sqlalchemy import Column, Integer, String

class ToDo(Base):
    __tablename__ = 'Tasks'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    due_to = Column(String)