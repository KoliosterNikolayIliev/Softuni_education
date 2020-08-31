import unittest

from project.player.advanced import Advanced


class TestAdvanced(unittest.TestCase):
    def setUp(self):
        self.advanced = Advanced("Gosho")

    def test_advanced_creation(self):
        self.assertEqual(self.advanced.username, "Gosho")
        self.assertEqual(self.advanced.health, 250)
        self.assertEqual(self.advanced.card_repository.__class__.__name__, "CardRepository")

    def test_set_username_empty_string_ValueError(self):
        with self.assertRaises(ValueError):
            self.advanced.username = ""

    def test_set_health_negative_ValueError(self):
        with self.assertRaises(ValueError):
            self.advanced.health = -1

    def test_is_dead_True(self):
        self.advanced.health = 0
        result = self.advanced.is_dead
        self.assertEqual(result, True)

    def test_take_damage_negative_error(self):
        with self.assertRaises(ValueError):
            self.advanced.take_damage(-100)

    def test_take_damage_for_real(self):
        self.advanced.take_damage(50)
        self.assertEqual(self.advanced.health, 200)


if __name__ == "__main__":
    unittest.main()