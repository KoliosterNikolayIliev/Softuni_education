from project.customer import Customer
from project.dvd import DVD
from project.movie_world import MovieWorld

import unittest


class TestsMovieWorld(unittest.TestCase):
    def test_movie_world_rent_dvd_already_rented_by_user(self):
        movie_world = MovieWorld("Test")
        d = DVD("A", 1, 1254, "February", 10)
        c = Customer("Pesho", 20, 4)
        movie_world.add_customer(c)
        movie_world.add_dvd(d)
        movie_world.rent_dvd(4, 1)
        result = movie_world.rent_dvd(4, 1)
        self.assertEqual(result, "Pesho has already rented A")


if __name__ == "__main__":
    unittest.main()
