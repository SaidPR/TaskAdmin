from fastapi import FastAPI
from database.bd import db
from router.taskRouter import router as task_router

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    app.db = db
    
app.include_router(task_router)
