from fastapi import APIRouter, Request
from database.bd import db
from dao.taskDao import TaskDao
from models.taskModel import TaskCreate, Salida

router = APIRouter(
    prefix="/tasks",
    tags=["Tareas"]
)

@router.post("/create", response_model=Salida)
async def create_task(task: TaskCreate, request: Request) -> Salida:
    taskDAO = TaskDao(request.app.db)
    return await taskDAO.create_task(task)