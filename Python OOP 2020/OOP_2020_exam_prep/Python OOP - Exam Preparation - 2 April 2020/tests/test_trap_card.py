import unittest

from project.card.trap_card import TrapCard


class TestTrapCard(unittest.TestCase):
    def setUp(self):
        self.trap_card = TrapCard("lele")

    def test_trap_card_creation(self):
        self.assertEqual(self.trap_card.name, "lele")
        self.assertEqual(self.trap_card.damage_points, 120)
        self.assertEqual(self.trap_card.health_points, 5)

    def test_name_empty_string(self):
        with self.assertRaises(ValueError):
            self.trap_card.name = ""

    def test_set_health_points_ValueError(self):
        with self.assertRaises(ValueError):
            self.trap_card.health_points = -1

    def test_set_damage_points_ValueError(self):
        with self.assertRaises(ValueError):
            self.trap_card.damage_points = -1


if __name__ == "__main__":
    unittest.main()