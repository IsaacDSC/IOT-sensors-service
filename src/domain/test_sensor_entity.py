from domain.sensor_entity import SensorEntity


def test_is_valid_sensor():
    input_valid = SensorEntity.is_valid(
        tag="tq001",
        unit="kg",
        value=19.9,
    )
    assert input_valid == True


def test_not_valid_sensor():
    test = SensorEntity.is_valid(
        tag="tq001",
        unit="kg",
        value=0,
    )
    assert test == False
