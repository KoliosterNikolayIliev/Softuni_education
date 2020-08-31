import unittest

from project.player.player_repository import PlayerRepository
from project.player.advanced import Advanced


class test_PlayerRepository(unittest.TestCase):
    def setUp(self):
        self.player_repository = PlayerRepository()
        self.player = Advanced("test_player")
        self.player2 = Advanced("just_player")

    def test_add_new_player(self):
        self.player_repository.add(self.player)
        result = len(self.player_repository.players)
        self.assertEqual(result, 1)

    def test_add_player_same_name_valueError(self):
        with self.assertRaises(ValueError):
            self.player_repository.add(self.player)
            self.player_repository.add(self.player)

    def test_remove_player_existing(self):
        self.player_repository.add(self.player)
        self.player_repository.add(self.player2)
        self.player_repository.remove("test_player")
        result = len(self.player_repository.players)
        self.assertEqual(result, 1)

    def test_remove_player_non_existing_ValueError(self):
        with self.assertRaises(ValueError):
            self.player_repository.add(self.player2)
            self.player_repository.remove("")

    def test_find(self):
        self.player_repository.add(self.player2)
        result = self.player_repository.find("just_player").username
        self.assertEqual(result, "just_player")


if __name__ == "__main__":
    unittest.main()