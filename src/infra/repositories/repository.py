from sqlalchemy.orm import Session

from ..schemas import schemas

from ..models import models


def create_sensor(db: Session, sensor: schemas.SensorRequest):
    db_sensor = models.Sensor(**sensor.dict())
    db.add(db_sensor)
    db.commit()
    db.refresh(db_sensor)
    return db_sensor


def update_sensor(db: Session, sensor: schemas.SensorRequest):
    sensor_query = db.query(models.Sensor).filter(models.Sensor.tag == sensor.tag)
    db_sensor = sensor_query.first()
    if not db_sensor:
        return "NOT_FOUND"
    update_data = sensor.dict(exclude_unset=True)
    sensor_query.filter(models.Sensor.tag == sensor.tag).update(
        update_data, synchronize_session=False)
    db.commit()
    db.refresh(db_sensor)
    return db_sensor


def get_sensor_by_tag(db: Session, tag: str):
    return db.query(models.Sensor).filter(models.Sensor.tag == tag).first()
