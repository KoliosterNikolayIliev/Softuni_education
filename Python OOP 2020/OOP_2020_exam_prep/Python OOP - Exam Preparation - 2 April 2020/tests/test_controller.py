from project.controller import Controller
from project.card.card_repository import CardRepository
from project.player.player_repository import PlayerRepository
import unittest


class TestsController(unittest.TestCase):
    def setUp(self):
        self.controller = Controller()


    def test_add_beginner_should_add_beginner_to_player_repo(self):
        self.controller.add_player("Beginner", "Peter")
        player = self.controller.player_repository.players[0]
        self.assertEqual(player.username, "Peter")
        self.assertEqual(player.__class__.__name__, "Beginner")

    def test_add_advanced_should_add_advanced_to_player_repo(self):
        self.controller.add_player("Advanced", "Peter")
        player = self.controller.player_repository.players[0]
        self.assertEqual(player.username, "Peter")
        self.assertEqual(player.__class__.__name__, "Advanced")

    def test_add_player_should_return_message(self):
        message = self.controller.add_player("Advanced", "Peter")
        self.assertEqual(message, "Successfully added player of type Advanced with username: Peter")

    def test_add_magic_should_add_magic_to_card_repo(self):
        self.controller.add_card("Magic", "Magic Card")
        card = self.controller.card_repository.cards[0]
        self.assertEqual(card.name, "Magic Card")
        self.assertEqual(card.__class__.__name__, "MagicCard")

    def test_add_trap_should_add_trap_to_card_repo(self):
        self.controller.add_card("Trap", "Trap Card")
        card = self.controller.card_repository.cards[0]
        self.assertEqual(card.name, "Trap Card")
        self.assertEqual(card.__class__.__name__, "TrapCard")

    def test_add_card_should_return_message(self):
        message = self.controller.add_card("Trap", "Trap Card")
        self.assertEqual(message, "Successfully added card of type TrapCard with name: Trap Card")

    def test_add_player_card_should_add_card_to_player_repo(self):
        self.controller.add_player("Advanced", "Peter")
        self.controller.add_card("Trap", "Trap Card")
        self.controller.add_player_card("Peter", "Trap Card")
        card = self.controller.player_repository.players[0].card_repository.cards[0]
        self.assertEqual(card.name, "Trap Card")

    def test_add_player_card_should_return_message(self):
        self.controller.add_player("Advanced", "Peter")
        self.controller.add_card("Trap", "Trap Card")
        message = self.controller.add_player_card("Peter", "Trap Card")
        self.assertEqual(message, "Successfully added card: Trap Card to user: Peter")

    def test_fight_should_return_message(self):
        self.controller.add_player("Advanced", "Peter")
        self.controller.add_player("Advanced", "George")
        self.controller.add_card("Trap", "Trap Card")
        self.controller.player_repository.find("Peter").card_repository.add(self.controller.card_repository.cards[0])
        message = self.controller.fight("Peter", "George")
        self.assertEqual(message, "Attack user health 255 - Enemy user health 130")

    def test_report_returns_correct_str(self):
        self.controller.add_player("Advanced", "Peter")
        self.controller.add_player("Advanced", "George")
        self.controller.add_card("Trap", "Trap Card")
        self.controller.player_repository.find("Peter").card_repository.add(self.controller.card_repository.cards[0])
        self.assertEqual(self.controller.report(),
                         "Username: Peter - Health: 250 - Cards 1\n### Card: Trap Card - Damage: 120\nUsername: George - Health: 250 - Cards 0\n")


if __name__ == "__main__":
    unittest.main()