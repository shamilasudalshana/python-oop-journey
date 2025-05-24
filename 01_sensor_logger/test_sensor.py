# to test the sensor class

import unittest
from sensor import Sensor

class TestSensor(unittest.TestCase):
    def test_initialization(self):
        test_sensor = Sensor(15, "New York", "F")
        self.assertEqual(test_sensor.id, 15)
        self.assertEqual(test_sensor.location, "New York")
        self.assertEqual(test_sensor.unit, "F")
        self.assertIsNone(test_sensor.value)

    def test_read_value_range(self):
        test_sensor = Sensor(2, "Berlin", "C")
        value = test_sensor.read_value()
        self.assertTrue(1 <= value <= 1000)

    def test_count_no_sensors(self):
        Sensor.no_of_sensors = 0 # make sure count is reset before the test 
        s1 = Sensor(1, "Geniva", "C")
        s2 = Sensor(22, "San Francisco", "F")
        self.assertEqual(Sensor.count_no_sensors(), 2)

    def test_str_output(self):
        sen = Sensor(10, "Leipzig", "C")
        "Sensor {self.id} at {self.location} [{self.unit}]"
        excepted = "Sensor 10 at Leipzig [C]"
        self.assertEqual(str(sen), excepted)

if __name__ == "__main__":
    unittest.main()