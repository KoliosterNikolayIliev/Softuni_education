from project.player.player import Player


class PlayerRepository:
    def __init__(self):
        self.count = 0
        self.players = []

    def add(self, player: Player):
        player_names = [x.username for x in self.players]
        if player.username in player_names:
            raise ValueError(f"Player {player.username} already exists!")
        self.players.append(player)
        self.count += 1

    def remove(self, player: str):
        if player == "":
            raise ValueError("Player cannot be an empty string!")
        player = self.find(player)
        self.players.remove(player)
        self.count -= 1

    def find(self, username: str):
        player = [x for x in self.players if x.username == username][0]
        return player
