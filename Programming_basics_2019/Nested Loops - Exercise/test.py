import unittest


class Test(unittest.TestCase):
    def test_refuel_method_in_car_class(self):
        cr = Car(4, 50, 5, 30)
        self.assertEqual(cr.refuel(20), 50)
        cr.drive(1)
        self.assertEqual(cr.refuel(10), 45)


if __name__ == "__main__":
    unittest.main()



import unittest
class Test(unittest.TestCase):
    def test_buy_tickets_method_in_plane_class(self):
        pl = Plane(25,5,5)
        self.assertEqual(pl.buy_tickets(6,2),"There is no row 6 in the plane!")
        self.assertEqual(pl.buy_tickets(5,3), 3)
        self.assertEqual(pl.buy_tickets(4, 4), 4)
        self.assertEqual(pl.buy_tickets(5, 4), "Not enough tickets on row 5!")
        self.assertEqual(pl.seats_available, {5:2, 4:1})

if __name__ == "__main__":
    unittest.main()