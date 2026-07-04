from dotenv import load_dotenv
import os
from sqlmodel import SQLModel, create_engine, Session


load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

def get_session():
    with Session(engine) as session:
        yield session

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

from app.models import User, BlogPost, Category, Comment, Lead, Note