
from pydantic import BaseModel

class TaskModel(BaseModel):
    title: str
    description: str
    due_to: str