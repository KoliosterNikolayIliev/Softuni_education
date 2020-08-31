import unittest

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class test_battlfield(unittest.TestCase):
    def setUp(self):
        self.attacker1 = Beginner("Gosho")
        self.attacker2 = Advanced("Pesho")
        self.enemy1 = Beginner("Misho")
        self.enemy2 = Advanced("Pencho")

    def test_fight_with_dead_player_should_raise_error(self):
        bf = BattleField()
        p1 = self.attacker1
        p2 = self.enemy1
        p1.health = 0
        with self.assertRaises(ValueError) as cm:
            bf.fight(p1, p2)
        self.assertEqual(str(cm.exception), "Player is dead!")

    def test_beginner_bonus_health(self):
        BattleField.fight(self.attacker1, self.enemy1)
        result = (self.attacker1.health, self.enemy1.health)
        self.assertEqual(result, (90, 90))

    def test_beginner_bonus_cards_damage_points(self):
        self.attacker1.card_repository.add(MagicCard("ura"))
        self.enemy2.card_repository.add(MagicCard("jura"))
        BattleField.fight(self.attacker1, self.enemy2)
        attacker_cards_damage = [x.damage_points for x in self.attacker1.card_repository.cards]
        enemy_cards_damage = [x.damage_points for x in self.enemy2.card_repository.cards]
        result = (attacker_cards_damage, enemy_cards_damage)
        self.assertEqual(result, ([35], [5]))

    def test_not_beginner(self):
        BattleField.fight(self.attacker2, self.enemy2)
        result = (self.attacker2.health, self.enemy2.health)
        self.assertEqual(result, (250, 250))

    def test_player_dies_in_fight(self):
        bf = BattleField()
        mg1 = MagicCard("Magic One")
        mg2 = MagicCard("Magic Two")
        p1 = self.attacker1
        p2 = self.enemy1
        p1.card_repository.add(mg1)
        p1.card_repository.add(mg2)
        bf.fight(p1, p2)
        with self.assertRaises(ValueError) as cm:
            bf.fight(p1, p2)
        self.assertEqual(str(cm.exception), "Player's health bonus cannot be less than zero.")


if __name__ == "__main__":
    unittest.main()