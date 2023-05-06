from pydantic import BaseModel


class Sensor(BaseModel):
    sensor_name: str
    tag: str
    value: float
    unit: str


class SensorRequest(Sensor):
    sensor_name: str
    tag: str
    unit: str
    value: float


class SensorResponse(Sensor):
    id: int
    tag: str
    value: float
    unit: str
