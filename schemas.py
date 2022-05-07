
from pydantic import BaseModel

class TaskModel(BaseModel):
    header: str
    due_date: str
    description: str