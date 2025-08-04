# TaskAdmin 📝

TaskAdmin es una API construida con **FastAPI** y **MongoDB** para la gestión de tareas. Permite crear, actualizar, listar y eliminar tareas de manera sencilla.

## 🚀 Tecnologías usadas

- Python 3.12
- FastAPI
- Pydantic
- Motor (MongoDB Async Driver)
- Uvicorn
- MongoDB Atlas

## 📁 Estructura del proyecto

```
TaskAdmin/
│── main.py
database/
│   └── bd.py
models/
│   └── taskModel.py
├── dao/
│   └── taskDao.py
└── routers/
└── taskRouter.py
├── venv/
├── .gitignore
├── requirements.txt
└── README.md
```

## 🔧 Instalación y ejecución local

1. **Clona el repositorio**

```bash
git clone https://github.com/SaidPR/TaskAdmin.git
cd TaskAdmin
```

2. **Crea y activa el entorno virtual**

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instala las dependencias**

```bash
pip install -r requirements.txt
```

4. **Configura la conexión a MongoDB**

Cambia la URL en `database/bd.py`:

```python
MONGO_URL = "mongodb+srv://<usuario>:<contraseña>@<cluster>.mongodb.net/?retryWrites=true&w=majority&appName=TaskAdmin"
```

5. **Ejecuta el servidor**

```bash
uvicorn app.main:app --reload
```

## 📬 Endpoints

- `POST /tasks/create`: Crea una nueva tarea
- `GET /tasks`: Lista todas las tareas
- `PUT /tasks/{id}`: Actualiza una tarea
- `DELETE /tasks/{id}`: Elimina una tarea

> La mayoría de los endpoints se encuentran bajo el prefijo `/tasks`

