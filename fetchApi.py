# This class/functions work to extract information from the pokemon API
# https://pokeapi.co/
import requests

r = requests.get('https://pokeapi.co/api/v2/pokemon/?offset=0&limit=151')
#
# response = r.json()
# r.text


# items = response[""]
#
# for pokemon in items:
#     theFirstObject = departures[busNumber][0]
#     print()

# if __name__ == "__main__":
#     main()

# Store the following:
# For each Pokemon:
# - Name
# - Artwork image (as URL)
# - Attack value
# - Defense value
# - Types