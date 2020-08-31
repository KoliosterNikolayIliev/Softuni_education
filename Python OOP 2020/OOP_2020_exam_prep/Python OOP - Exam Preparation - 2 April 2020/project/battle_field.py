from project.player.beginner import Beginner
from project.player.player import Player


class BattleField:
    @staticmethod
    def fight(attacker: Player, enemy: Player):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")
        beginners = [v for k, v in locals().items() if isinstance(v, Beginner)]
        if len(beginners) >= 1:
            for beginner in beginners:
                beginner.health += 40
                for card in beginner.card_repository.cards:
                    card.damage_points += 30

        attacker.health += sum([x.health_points for x in attacker.card_repository.cards])
        enemy.health += sum([x.health_points for x in enemy.card_repository.cards])

        for card in attacker.card_repository.cards:
            enemy.take_damage(card.damage_points)

        for card in enemy.card_repository.cards:
            attacker.take_damage(card.damage_points)
