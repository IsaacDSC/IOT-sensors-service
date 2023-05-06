from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

environments = dotenv_values(".env")

# CONFIG_DATABASE = "sqlite:///./sql_app.db"
CONFIG_DATABASE = environments['DATABASE_URL']
engine = create_engine(CONFIG_DATABASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
Base.metadata.create_all(engine)