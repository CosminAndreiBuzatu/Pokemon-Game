# game class is responsible for holding and processing data concerning the game
# this is to be used in web where user interacts with it

from pokemon import Pokemon
from pokemonDatabase import PokemonDatabase

class game:
    def __init__(self):
        pass

    def getNewDeck(self):
        # get 151 pokemon from database, put in a list and shuffle it.
        db = PokemonDatabase()
        deck = db.
