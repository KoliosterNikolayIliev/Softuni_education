from project.people.child import Child
from project.rooms.room import Room
import unittest


class TestRoom(unittest.TestCase):
    def setUp(self):
        child_one = Child(5, 1, 2, 1)
        child_two = Child(3, 2)
        self.room = Room("Test", 500, 2)
        self.room.children.append(child_one)
        self.room.children.append(child_two)

    def test_set_room_init_normal(self):
        self.assertEqual(self.room.family_name, "Test")
        self.assertEqual(self.room.expenses, 0)
        self.assertEqual(self.room.members_count, 2)
        self.assertEqual(self.room.budget, 500)
        self.assertEqual(len(self.room.children), 2)

    def test_calculate_expenses_no_args(self):
        self.room.calculate_expenses()
        self.assertEqual(self.room.expenses, 0)

    def test_calculate_expenses_args_normal(self):
        self.room.calculate_expenses(self.room.children)
        self.assertEqual(self.room.expenses, 420)

    def test_set_expenses_valueError(self):
        child_one = Child(-5, -1, -2, -1)
        child_two = Child(-3, -2)
        self.room.children.clear()
        self.room.children.append(child_one)
        self.room.children.append(child_two)
        with self.assertRaises(ValueError) as ex:
            self.room.calculate_expenses(self.room.children)
            self.assertEqual(str(ex.exception), "Expenses cannot be negative")


if __name__ == "__main__":
    unittest.main()
