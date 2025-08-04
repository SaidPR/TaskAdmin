from models.taskModel import TaskCreate, Salida

class TaskDao:
    def __init__(self, db):
        self.db = db

    async def create_task(self, task: TaskCreate) -> Salida:
        salida = Salida(status="", message="")
        try:
            if task.title == "":
                salida.status = "error"
                salida.message = "El título de la tarea es obligatorio."
                return salida

            result = await self.db.task.insert_one(task.dict())
        except Exception as e:
            salida.status = "error"
            salida.message = str(e)
            return salida

        salida.status = "success"
        salida.message = "Tarea creada correctamente."
        return salida
