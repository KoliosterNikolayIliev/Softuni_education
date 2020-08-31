import unittest

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):
    def setUp(self):
        self.paint_factory = PaintFactory("test_factory", 20)
        self.paint_factory.add_ingredient("white", 1)

    def test_add_normal_existing(self):
        self.paint_factory.add_ingredient("white", 1)
        result = self.paint_factory.products
        self.assertEqual(result, {"white": 2})

    def test_add_new_non_existing(self):
        self.paint_factory.add_ingredient("blue", 1)
        result = self.paint_factory.products
        self.assertEqual(result, {"white": 1, "blue": 1})

    def test_add_TE(self):
        with self.assertRaises(TypeError) as ex:
            self.paint_factory.add_ingredient("zele", 1)
        self.assertEqual(str(ex.exception), "Ingredient of type zele not allowed in PaintFactory")

    def test_add_VE(self):
        with self.assertRaises(ValueError):
            self.paint_factory.add_ingredient("blue", 10000)

    def test_rem_normal(self):
        self.paint_factory.remove_ingredient("white", 1)
        result = self.paint_factory.products
        self.assertEqual(result, {"white": 0})

    def test_rem_VE(self):
        with self.assertRaises(ValueError):
            self.paint_factory.remove_ingredient("white", 10000)

    def test_rem_KE(self):
        with self.assertRaises(KeyError):
            self.paint_factory.remove_ingredient("blue", 1)

    def test_property(self):
        result = self.paint_factory.products
        self.assertEqual(result, {'white': 1})


if __name__ == "__main__":
    unittest.main()
