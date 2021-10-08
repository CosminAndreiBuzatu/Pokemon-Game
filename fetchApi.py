# This class/functions work to extract information from the pokemon API
# https://pokeapi.co/
import requests
from pokemon import Pokemon
from pokemonTypes import Types

#create object and call all these functions on it
class PokemonAPI():
# Method to extract API data of one pokemon
    def fetchPokemon(number):
        try:
            r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{number}')
        except:
            print("Cannot connect to API")
            return None

        response = r.json()

        pokemonTypes =[]
        types = response["types"]
        for type in types:
            pokemonTypes.append(type["type"]["name"])
        input_dict = {
            "name": response["species"]["name"],
            "artwork": response["sprites"]["front_default"],
            "attack": response["stats"][1]["base_stat"],
            "defense": response["stats"][2]["base_stat"],
            "types": pokemonTypes,
        }
        return Pokemon(input_dict)


    # method to get a list of pokemon from start number ot end number e.g. 1 to 151
    def fetchManyPokemon(start, end):
        listOfPokemon = []
        for number in range(start, end + 1):
            pokemon = fetchPokemon(number)
            listOfPokemon.append(pokemon)
        return listOfPokemon

    # r = requests.get('https://pokeapi.co/api/v2/pokemon/?offset=0&limit=151')

    # Store the following:
    # For each Pokemon:
    # - Name
    # - Artwork image (as URL)
    # - Attack value
    # - Defense value
    # - Types


    def fetchTypes(number):
        try:
            r = requests.get(f'https://pokeapi.co/api/v2/type/{number}')
        except:
            print("Cannot connect to API")
            return None

        response = r.json()

        doubleDamages =[]
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
