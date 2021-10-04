# This class/functions work to extract information from the pokemon API
# https://pokeapi.co/
import requests

r = requests.get('https://pokeapi.co/api/v2/pokemon/?offset=0&limit=151')
print(r.text)
response = r.json()

Items = response["results"]
for pokemon in Items:
        print(pokemon["name"])
        print(pokemon["url"])
#     theFirstObject = departures[busNumber][0]
#     # for each bus object in the response
#     print(busNumber)

# Create a database which is able to store the following information about a Pokemon:
# - Name
# - Artwork image (as URL)
# - Attack value
# - Defense value
# - Types
