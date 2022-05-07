
from db import models
from db.database import engine
from fastapi import FastAPI
import task

app = FastAPI(title="ToDo API")
app.include_router(task.router)

models.Base.metadata.create_all(engine)