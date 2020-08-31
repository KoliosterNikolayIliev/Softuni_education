import unittest

from project.hardware.hardware import Hardware
from project.software.software import Software


class TestHardware(unittest.TestCase):
    def setUp(self):
        self.hardware = Hardware("test", "Heavy", 50, 30)
        self.software = Software("test_sw", "Express", 30, 20)

    def test_hardware_creation(self):
        self.assertEqual(self.hardware.name, "test")
        self.assertEqual(self.hardware.type, "Heavy")
        self.assertEqual(self.hardware.capacity, 50)
        self.assertEqual(self.hardware.memory, 30)
        self.assertEqual(self.hardware.software_components, [])

    def test_successful_install(self):
        self.hardware.install(self.software)
        result = self.hardware.software_components[0].name
        self.assertEqual(result, "test_sw")

    def test_unsuccessful_EX(self):
        with self.assertRaises(Exception):
            self.software = Software("test_sw", "Express", 100, 20)
            self.hardware.install(self.software)

    def test_unsuccessful2_EX(self):
        with self.assertRaises(Exception):
            self.software = Software("test_sw", "Express", 10, 200)
            self.hardware.install(self.software)

    def test_uninstall(self):
        self.software = Software("test_sw", "Express", 30, 20)
        self.hardware.install(self.software)
        self.hardware.uninstall(self.software)
        result = self.hardware.software_components
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
