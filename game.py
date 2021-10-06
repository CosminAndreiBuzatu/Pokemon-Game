# game class is responsible for holding and processing data concerning the game
# this is to be used in web where user interacts with it
import random
from pokemon import Pokemon
from pokemonDatabase import PokemonDatabase


class Game:
    def __init__(self):
        self.deck1 = []
        self.deck2 = []

    def getNewDecks(self):
        # get 151 pokemon from database, put in a list and shuffle it, split them in two.
        db = PokemonDatabase()
        newDeck = db.getAllPokemon()
        random.shuffle(newDeck)

        if len(newDeck) % 2 == 1:
            newDeck.pop()
        midpoint = int(len(newDeck) / 2)
        self.deck1 = newDeck[:midpoint]
        self.deck2 = newDeck[midpoint:]

    def getTopCards(self):
        # return a list of two pokemon, one each for the two decks
        if self.deck1:
            pokemon1 = self.deck1[-1]
        else:
            pokemon1 = None
        if self.deck2:
            pokemon2 = self.deck2[-1]
        else:
            pokemon2 = None

        return [pokemon1, pokemon2]

    def removeTopCards(self):
        # deletes the top cards of both decks, if no cards were in a deck, do nothing
        if self.deck1:
            self.deck1.pop()
        if self.deck2:
            self.deck2.pop()


if __name__ == "__main__":
    g = Game()
    g.getNewDecks()

    topcards = g.getTopCards()
    print(topcards[0].name)

    g.removeTopCards()

    topcards = g.getTopCards()
    print(topcards[0].name)
