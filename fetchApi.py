# This class/functions work to extract information from the pokemon API
# https://pokeapi.co/
import requests

r = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')

response = r.json()
r.text


