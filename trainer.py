from pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon.name not in self.pokemons:
            self.pokemons.append(pokemon.name)
            return f"Caught {pokemon.pokemon_details()}"
        else:
            return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        if pokemon_name in self.pokemons:
            self.pokemons.remove(pokemon_name)
            return f"You have released {pokemon_name}"
        else:
            return "This pokemon is not caught"

    def trainer_data(self):
        data = f"Pokemon trainer: {self.name}\nPokemon count {len(self.pokemons)}\n"
        for pokemon in self.pokemons:
            data += f"-{pokemon}"
        return data




