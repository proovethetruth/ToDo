
import datetime
from sqlalchemy.orm.session import Session
from sqlalchemy import desc
from schemas import TaskModel
from db.models import ToDo


def add_task(db: Session, request: TaskModel):
    new_task = ToDo(
        title = request.title,
        description = request.description,
        due_to = request.due_to
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


def get_all_tasks(db: Session):
    return db.query(ToDo).order_by(ToDo.due_to).all()

def get_tomorrow_tasks(db: Session):
    return db.query(ToDo).filter(ToDo.due_to == datetime.date.today() + datetime.timedelta(days=1)).all()

def update_task(db: Session, id: int, request: TaskModel):
    task = db.query(ToDo).filter(ToDo.id == id)
    task.update({
        ToDo.title: request.title,
        ToDo.description: request.description,
        ToDo.due_to: request.due_to
    })
    db.commit()
    return {"{request.title} task" : "updated to {ToDo.title}"}


def delete_task(db: Session, id: int, request: TaskModel):
    task = db.query(ToDo).filter(ToDo.id == id).first()
    db.delete(task)
    db.commit()
    return {"{request.title} task" : "deleted"}