import unittest

from project.survivor import Survivor


class TestSurvivor(unittest.TestCase):
    def setUp(self):
        self.survivor = Survivor("Pesho", 37)

    def test_initial_health(self):
        result = self.survivor.health
        self.assertEqual(result,100)

    def test_initial_needs(self):
        result = self.survivor.needs
        self.assertEqual(result, 100)

    def test_name_Ok(self):
        result = self.survivor = Survivor("Gosho", 33)
        self.assertEqual(result.name, "Gosho")
        self.assertEqual(result.age, 33)

    def test_name_empty_string_VE(self):
        with self.assertRaises(ValueError):
            self.survivor = Survivor("", 24)

    def test_age_Ok(self):
        result = self.survivor
        self.assertEqual(result.age, 37)

    def test_age_VE(self):
        with self.assertRaises(ValueError):
            Survivor("p", -12)


    def test_health_OK(self):
        self.survivor.health = 80
        self.assertEqual(self.survivor.health, 80)

    def test_health_VE(self):
        with self.assertRaises(ValueError):
            self.survivor.health = -2

    def test_needs_OK(self):
        self.survivor.needs = 80
        self.assertEqual(self.survivor.needs, 80)

    def test_needs_VE(self):
        with self.assertRaises(ValueError):
            self.survivor.needs = -2

    def test_needs_sustenance_yes(self):
        self.survivor.needs = 60
        result = self.survivor.needs_sustenance
        self.assertEqual(result, True)

    def test_needs_sustenance_no(self):
        self.survivor.needs = 100
        result = self.survivor.needs_sustenance
        self.assertEqual(result, False)

    def test_needs_healing_yes(self):
        self.survivor.health = 80
        result = self.survivor.needs_healing
        self.assertEqual(result, True)

    def test_needs_healing_no(self):
        self.survivor.health = 100
        result = self.survivor.needs_healing
        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()
