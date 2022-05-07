
from schemas import TaskModel
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_todo

router = APIRouter(
    prefix='/tasks',
)

# Create Task
@router.post('/')
def create_task(request: TaskModel, db: Session = Depends(get_db())):
    return db_todo.add_task(db, request)