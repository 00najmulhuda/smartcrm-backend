from fastapi import FastAPI
from app.database import create_db_and_tables
from app.models import note
from app.routers import auth
from app.routers import blog
from app.routers import lead
from app.routers import note
from app.routers import user

app = FastAPI()
app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(lead.router)
app.include_router(note.router)
app.include_router(user.router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables() 



    