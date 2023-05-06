import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship

from ..configs.database import Base


class Sensor(Base):
    __tablename__ = "sensors"

    id: int = Column(Integer, primary_key=True, index=True)
    sensor_name: str = Column(String, index=True)
    tag: str = Column(String, unique=True, index=True)
    value: float = Column(Float)
    unit: str = Column(String)
    created_date: str = Column(DateTime, default=datetime.datetime.utcnow)
    updated_date: str = Column(DateTime, default=datetime.datetime.utcnow)
