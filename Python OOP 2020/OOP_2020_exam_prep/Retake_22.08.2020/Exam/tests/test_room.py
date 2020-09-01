from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.people.child import Child
from project.rooms.room import Room
import unittest


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.child_one = Child(5, 1, 2, 1)
        self.child_two = Child(3, 2)
        self.room = Room("Smiths", 1000, 4)

    def test_set_expenses_OK(self):
        self.room.expenses = 10
        self.assertEqual(self.room.expenses, 10)

    def test_set_expenses_valueError(self):
        with self.assertRaises(ValueError) as ex:
            self.room.expenses = -10
            self.assertEqual(str(ex.exception), "Expenses cannot be negative")

    def test_calculate_expenses(self):
        self.room.calculate_expenses((Child(5, 1, 2, 1), Child(3, 2), TV(), Laptop()))
        self.assertEqual(self.room.expenses, 495)


if __name__ == "__main__":
    unittest.main()
