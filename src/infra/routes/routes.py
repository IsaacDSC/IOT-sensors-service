from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..schemas import schemas
from ..repositories import repository
from ...app.services_sensor import SensorService, SensorEntity, repository


def Routes(app, sessionDb):
    @app.get("/", status_code=status.HTTP_200_OK)
    async def health_check():
        return {"status": True}

    @app.post("/operation/sensor/analogic", status_code=status.HTTP_200_OK)
    def analogic_sensor_register(
        sensor: schemas.SensorRequest, db: Session = Depends(sessionDb)
    ):
        registered = SensorService(
            db=db,
            entity=SensorEntity,
            repository=repository
        ).register_activity_sensor(sensor)
        return registered
