from sensor import Sensor

sensors = [
    Sensor(2, "Dresde", "C"),
    Sensor(3, "Berlin", "C"),
    Sensor(67, "Colombo 5", "C"),
]

for sensor in sensors:
    reading_value = sensor.read_value()
    print(f"Sensor {sensor.id} is located in {sensor.location} and currently reads {reading_value}{sensor.unit}")

no_sensors = Sensor.count_no_sensors()

print(f"There are {no_sensors} instances generated from the Sensor class")