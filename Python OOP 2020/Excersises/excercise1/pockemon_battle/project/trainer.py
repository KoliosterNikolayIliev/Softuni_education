# from pockemon_battle.project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if pokemon not in self.pokemon:
            self.pokemon.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        if pokemon_name in [p.name for p in self.pokemon]:
            for n in range(len(self.pokemon)):
                if pokemon_name == self.pokemon[n].name:
                    self.pokemon.remove(self.pokemon[n])
                    break
            return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n"
        if len(self.pokemon)>0:
            for p in self.pokemon:
                result += f"- {p.pokemon_details()}\n"

        return result

# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# # print(trainer.release_pokemon("Charizard"))
# print(trainer.release_pokemon("Pikachu"))
#
# print(trainer.trainer_data())

