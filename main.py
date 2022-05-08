
from db import models
from db import db_todo
from db.database import engine, get_db
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
from schemas import TaskModel
from typing import List

app = FastAPI(title="ToDo API")

models.Base.metadata.create_all(engine)


@app.get('/', response_model=List[TaskModel], tags=['Display Tasks'], summary='List Tasks by ID')
def get_all_tasks(db: Session = Depends(get_db)):
    return db_todo.get_all_tasks(db)


@app.get('/by_date', response_model=List[TaskModel], tags=['Display Tasks'], summary='List Tasks by Date')
def get_all_tasks_by_date(db: Session = Depends(get_db)):
    return db_todo.get_all_tasks_by_date(db)


@app.get('/today', response_model=List[TaskModel], tags=['Display Tasks'], summary='List Tasks for Today')
def get_today_tasks(db: Session = Depends(get_db)):
    return db_todo.get_today_tasks(db)


@app.get('/tomorrow', response_model=List[TaskModel], tags=['Display Tasks'], summary='List Tasks for Tomorrow')
def get_tomorrow_tasks(db: Session = Depends(get_db)):
    return db_todo.get_tomorrow_tasks(db)


@app.post('/create_task', tags=['Database operations'], summary='Create Task')
def create_task(request: TaskModel, db: Session = Depends(get_db)):
    return db_todo.add_task(db, request)


@app.put('/update/{id}', tags=['Database operations'], summary='Update Task')
def update_task(id: int, request: TaskModel, db: Session = Depends(get_db)):
    return db_todo.update_task(db, id, request)


@app.delete('/delete/{id}', tags=['Database operations'], summary='Delete Task')
def update_task(id: int, request: TaskModel, db: Session = Depends(get_db)):
    return db_todo.delete_task(db, id, request)