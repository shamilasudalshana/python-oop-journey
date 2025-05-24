import random

class Sensor:

    # to initalize the number of sensors
    no_of_sensors = 0

    def __init__(self, id, location, unit):
        self.id = id
        self.location = location
        self.unit = unit
        self.value = None # to keep the value none until it is assigned using the read_value method
        Sensor.no_of_sensors += 1

    def read_value(self):
        self.value = random.randint(1,1000)
        return self.value
    
    # calculate the no of instances. 
    @classmethod
    def count_no_sensors(cls):
        return cls.no_of_sensors
    
    # to provide the prinit the instant objects directly 
    def __str__(self):
        return f"Sensor {self.id} at {self.location} [{self.unit}]"
    

if __name__ == "__main__":

    sensors = [
        Sensor(2, "Dresde", "C"),
        Sensor(3, "Berlin", "C"),
        Sensor(67, "Colombo 5", "C"),
    ]

    for sensor in sensors:
        reading_value = sensor.read_value()
        print(f"Sensor {sensor.id} is located in {sensor.location} and currently reads {reading_value}{sensor.unit}")






