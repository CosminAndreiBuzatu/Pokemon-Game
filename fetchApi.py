# This class/functions work to extract information from the pokemon API
# https://pokeapi.co/
import requests
from pokemon import Pokemon
from pokemonTypes import Types


# create object and call all these functions on it
class PokemonAPI():
    # Method to extract API data of one pokemon

    def fetchPokemon(self, number):
        try:
            r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{number}')
        except:
            print("Cannot connect to API")
            return None

        response = r.json()
        stage = None
        species = requests.get(response["species"]["url"]).json()
        evolution = requests.get(species["evolution_chain"]["url"]).json()
        if evolution["chain"]["species"]["name"] == response["species"]["name"]:
            stage = 1
        if len(evolution["chain"]["evolves_to"]) != 0:
            if evolution["chain"]["evolves_to"][0]["species"]["name"] == response["species"]["name"]:
                stage = 2
            if len(evolution["chain"]["evolves_to"][0]["evolves_to"]) != 0:
                if evolution["chain"]["evolves_to"][0]["evolves_to"][0]["species"]["name"] == response["species"][
                    "name"]:
                    stage = 3
        if stage == 1 and len(evolution["chain"]["evolves_to"]) != 0:
            evolves = evolution["chain"]["evolves_to"][0]["species"]["name"]
        elif stage == 2 and len(evolution["chain"]["evolves_to"][0]["evolves_to"]) != 0:
            evolves = evolution["chain"]["evolves_to"][0]["evolves_to"][0]["species"]["name"]
        else:
            evolves = None
        if "is_baby" in evolution["chain"] and evolution["chain"]["is_baby"] == True and stage != None:
            stage -= 1

        pokemonTypes = []
        types = response["types"]
        for type in types:
            pokemonTypes.append(type["type"]["name"])
        input_dict = {
            "name": response["species"]["name"],
            "artwork": response["sprites"]["front_default"],
            "attack": response["stats"][1]["base_stat"],
            "defense": response["stats"][2]["base_stat"],
            "types": pokemonTypes,
            "evolutionStage": stage,
            "evolvesTo": evolves,
        }
        return Pokemon(input_dict)

    # method to get a list of pokemon from start number ot end number e.g. 1 to 151
    def fetchManyPokemon(self, start, end):
        listOfPokemon = []
        for number in range(start, end + 1):
            pokemon = self.fetchPokemon(number)
            listOfPokemon.append(pokemon)
        return listOfPokemon

    def fetchTypes(self, number):
        try:
            r = requests.get(f'https://pokeapi.co/api/v2/type/{number}')
        except:
            print("Cannot connect to API")
            return None

        response = r.json()

        doubleDamages = []
        halfDamages = []
        noDamages = []
        double = response["damage_relations"]["double_damage_to"]
        for types in double:
            doubleDamages.append(types["name"])
        half = response["damage_relations"]["half_damage_to"]
        for types in half:
            halfDamages.append(types["name"])
        no = response["damage_relations"]["no_damage_to"]
        for types in no:
            noDamages.append(types["name"])

        input_dict = {
            "name": response["name"],
            "doubleDamage": doubleDamages,
            "halfDamage": halfDamages,
            "noDamage": noDamages,
        }

        return Types(input_dict)

    def fetchAllTypes(self, start, end):
        allTypes = []
        for number in range(start, end + 1):
            types = self.fetchTypes(number)
            allTypes.append(types)
        return allTypes


pokemonApiObject = PokemonAPI()
