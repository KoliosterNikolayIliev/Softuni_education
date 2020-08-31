from Polymorphism_magic_methods.project.vechicle import Car
from Polymorphism_magic_methods.project.vechicle import Truck

import unittest


class CarTests(unittest.TestCase):
    def setUp(self):
        self.car = Car(50, 7)

    def test_drive_not_enough_fuel(self):
        self.car.drive(40)
        self.assertEqual(self.car.fuel_quantity, 50)

    def test_drive_enough_fuel(self):
        self.car.drive(2)
        self.assertEqual(self.car.fuel_quantity, 34.2)

    def test_refuel_add_fuel(self):
        self.car.refuel(30)
        self.assertEqual(self.car.fuel_quantity, 80)


class TruckTests(unittest.TestCase):
    def setUp(self):
        self.truck = Truck(50, 5)

    def test_drive_not_enough_fuel(self):
        self.truck.drive(60)
        self.assertEqual(self.truck.fuel_quantity, 50)

    def test_drive_enough_fuel(self):
        self.truck.drive(2)
        self.assertEqual(self.truck.fuel_quantity, 36.8)

    def test_refuel_add_fuel(self):
        self.truck.refuel(30)
        self.assertEqual(self.truck.fuel_quantity, 78.5)


if __name__ == "__main__":
    unittest.main()
