
from sqlalchemy.orm.session import Session
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