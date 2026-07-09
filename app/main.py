from fastapi import FastAPI
from app.database import create_db_and_tables
from app.routers import auth
from app.routers import blog
from app.routers import lead

app = FastAPI()
app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(lead.router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables() 



    