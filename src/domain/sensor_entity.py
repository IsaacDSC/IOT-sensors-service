class SensorEntity:
    def is_valid(tag: str, unit: str, value: float):
        return not (not tag or not unit or not value)

