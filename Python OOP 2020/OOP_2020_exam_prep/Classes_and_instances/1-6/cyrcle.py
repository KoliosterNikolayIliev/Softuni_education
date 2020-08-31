class Circle:
    pi = 3.14

    def __init__(self, r):
        self.radius = r

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self):
        result = Circle.pi * self.radius ** 2
        return result

    def get_circumference(self):
        result = 2*Circle.pi * self.radius
        return round(result, 2)

circle = Circle(10)
circle.set_radius(12)
print(circle.get_area())
print(circle.get_circumference())

import unittest

class Tests(unittest.TestCase):
   def test_set_radius(self):
        c = Circle(15)
        c.set_radius(150)
        self.assertEqual(c.radius, 150)

if __name__ == "__main__":
   unittest.main()
