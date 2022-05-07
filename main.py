
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

class Todo(BaseModel):
    header: str
    due_date: str
    description: str

app = FastAPI(title="ToDo API")

ToDo_list = []

def sort_by_date(e):
    return e['due_date']

@app.get('/', response_model=List[Todo], summary="Retrieves all tasks")
async def get_list():
    return ToDo_list   


@app.post('/todo', summary="Adds another task to the list")
async def create_todo(todo: Todo):
    ToDo_list.append(todo)
    return todo


@app.get('/todo/{id}', summary="Returns task by id")
async def get_todo(id: int):
    try:
        return ToDo_list[id]
    except:
        raise HTTPException(status_code=404, detail="ToDo Not Found")


@app.put('/update/{id}', summary="Updates task by id")
async def update_todo(id: int, todo: Todo):
    try:
        ToDo_list[id] = todo
        return ToDo_list
    except:
        raise HTTPException(status_code=404, detail="ToDo Not Found")

@app.delete('/todo/{id}', summary="Deletes task by id")
async def delete_todo(id: int):
    try:
        obj = ToDo_list
        ToDo_list.pop(id)
        return obj
    except:
        raise HTTPException(status_code=404, detail="ToDo Not Found")