import unittest

from project.player.beginner import Beginner


class TestBeginner(unittest.TestCase):
    def setUp(self):
        self.beginner = Beginner("Gosho")

    def test_beginner_creation(self):
        self.assertEqual(self.beginner.username, "Gosho")
        self.assertEqual(self.beginner.health, 50)
        self.assertEqual(self.beginner.card_repository.__class__.__name__, "CardRepository")

    def test_set_username_empty_string_ValueError(self):
        with self.assertRaises(ValueError):
            self.beginner.username = ""

    def test_set_health_negative_ValueError(self):
        with self.assertRaises(ValueError):
            self.beginner.health = -1

    def test_is_dead_True(self):
        self.beginner.health = 0
        result = self.beginner.is_dead
        self.assertEqual(result, True)

    def test_take_damage_negative_error(self):
        with self.assertRaises(ValueError):
            self.beginner.take_damage(-100)

    def test_take_damage_for_real(self):
        self.beginner.take_damage(10)
        self.assertEqual(self.beginner.health, 40)


if __name__ == "__main__":
    unittest.main()