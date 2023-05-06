from fastapi import FastAPI

from .infra.models import models
from .infra.configs.database import SessionLocal, engine

from .infra.routes.routes import Routes

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def sessionDb():
    db = SessionLocal()
    try:
        yield db
    except NameError:
        print(NameError)
    finally:
        db.close()


Routes(app, sessionDb)
