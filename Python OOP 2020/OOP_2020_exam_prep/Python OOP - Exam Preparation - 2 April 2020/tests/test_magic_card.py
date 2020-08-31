import unittest

from project.card.magic_card import MagicCard


class TestMagicCard(unittest.TestCase):
    def setUp(self):
        self.magic_card = MagicCard("mali")

    def test_magic_card_creation(self):
        self.assertEqual(self.magic_card.name, "mali")
        self.assertEqual(self.magic_card.damage_points, 5)
        self.assertEqual(self.magic_card.health_points, 80)

    def test_name_empty_string(self):
        with self.assertRaises(ValueError):
            self.magic_card.name = ""

    def test_set_health_points_ValueError(self):
        with self.assertRaises(ValueError):
            self.magic_card.health_points = -1

    def test_set_damage_points_ValueError(self):
        with self.assertRaises(ValueError):
            self.magic_card.damage_points = -1


if __name__ == "__main__":
    unittest.main()