from sqlalchemy.orm import Session
from ..domain.sensor_entity import SensorEntity
from ..infra.repositories import repository
from ..infra.schemas.schemas import SensorRequest


class SensorService:
    def __init__(
        self,
        db: Session,
        entity: SensorEntity,
        repository: repository
    ):
        self.db = db
        self.entity = entity
        self.repository = repository

    def register_activity_sensor(self, input: SensorRequest):
        valid = self.entity.is_valid(
            value=input.value,
            unit=input.unit,
            tag=input.tag,
        )
        if (not valid):
            return {'message': 'Fields invalids the sensor'}
        alreadyExist = self.repository.get_sensor_by_tag(
            db=self.db,
            tag=input.tag
        )
        if (not alreadyExist):
            return self.repository.create_sensor(self.db, input)
        return self.repository.update_sensor(self.db, input)
