# from guild_system.project.player import Player


class Guild:
    def __init__(self, name: str, ):
        self.name = name
        self.players_list = []

    def assign_player(self, player):
        if player.guild == "Unaffiliated" or self.name == player.guild:
            if player not in self.players_list:
                self.players_list.append(player)
                player.guild = self.name
                return f"Welcome player {player.name} to the guild {player.guild}"
            return f"Player {player.name} is already in the guild."
        return f"Player {player.name} is in another guild."

    def kick_player(self, player_name: str):
        if player_name in [p.name for p in self.players_list]:
            player = list(filter(lambda x: x.name == player_name, self.players_list))[0]
            self.players_list.remove(player)
            player.guild = "Unaffiliated"
            return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        for p in self.players_list:
            result += p.player_info()
        return result



# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())





