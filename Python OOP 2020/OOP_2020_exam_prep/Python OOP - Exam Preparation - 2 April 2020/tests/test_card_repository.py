import unittest

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class test_CardRepository(unittest.TestCase):
    def setUp(self):
        self.card_repository = CardRepository()
        self.card = MagicCard("test_card")
        self.card2 = MagicCard("just_card")

    def test_add_new_card(self):
        self.card_repository.add(self.card)
        result = len(self.card_repository.cards)
        self.assertEqual(result, 1)

    def test_add_card_same_name_valueError(self):
        with self.assertRaises(ValueError):
            self.card_repository.add(self.card)
            self.card_repository.add(self.card)

    def test_remove_card_existing(self):
        self.card_repository.add(self.card)
        self.card_repository.add(self.card2)
        self.card_repository.remove("test_card")
        result = len(self.card_repository.cards)
        self.assertEqual(result, 1)

    def test_remove_card_non_existing_ValueError(self):
        with self.assertRaises(ValueError):
            self.card_repository.add(self.card2)
            self.card_repository.remove("")

    def test_find(self):
        self.card_repository.add(self.card2)
        result = self.card_repository.find("just_card").name
        self.assertEqual(result, "just_card")


if __name__ == "__main__":
    unittest.main()