# This class/functions work to extract information from the pokemon API
# https://pokeapi.co/
import requests

from pokemon import Pokemon


# Method to extract API data of one pokemon
def fetchPokemon(number):
    try:
        r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{number}')
    except:
        print("Cannot connect to API")
        return None

    response = r.json()

    input_dict = {
        "name": response["species"]["name"],
        "artwork": response["sprites"]["front_default"],
        "attack": response["stats"][1]["base_stat"],
        "defence": response["stats"][2]["base_stat"],
        "type1": response["types"][0]["type"]["name"],
        "type2": "none"
    }
    if len(response["types"]) > 1:
        input_dict["type2"] = response["types"][1]["type"]["name"]

    return Pokemon(input_dict)


# method to get a list of pokemon from start number ot end number e.g. 1 to 151
def fetchManyPokemon(start, end):
    listOfPokemon = []
    for number in range(start, end + 1):
        pokemon = fetchPokemon(number)
        listOfPokemon.append(pokemon)
    return listOfPokemon
