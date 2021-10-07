# game class is responsible for holding and processing data concerning the game
# this is to be used in web where user interacts with it
# Todo
# - Handle the event when the user has chosen an attack type and clicks 'Attack'
# - Handle the event when the user has chosen 'Continue' for the AI to attack
# - Compare the attack of the attacker with the defense of the defender, modifying the attack value based on the attacker/defender types.
# - If the attacker wins, they get the defender’s card and continue attacking the following round.
# - If the defender wins, they get the attacker’s card and also become the attacker for the following round.
# - Once a player runs out of cards completely the game is over

import random
from pokemon import Pokemon
from pokemonDatabase import PokemonDatabase


class Game:
    def __init__(self):
        self.usersTurn = random.choice([True, False])
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

    def getCardsLeft(self):
        # returns the number of cards in both decks, in a list
        n1 = len(self.deck1)
        n2 = len(self.deck2)
        return [n1, n2]

    def removeTopCards(self):
        # deletes the top cards of both decks, if no cards were in a deck, do nothing
        if self.deck1:
            self.deck1.pop()
        if self.deck2:
            self.deck2.pop()

    def usersTurn(self):
        return self.usersTurn

    def availableAttacks(self):
        pokemon = self.deck1[-1]
        output = [pokemon.type1, pokemon.type2]
        return output

    def AiPickAttack(self):
        pokemon = self.deck1[-1]
        output = random.choice([pokemon.type1, pokemon.type2])
        return output

    def userAttacks(self, attacktype):
        #deck1[-1]

if __name__ == "__main__":
    g = Game()
    g.getNewDecks()

    topcards = g.getTopCards()
    print(topcards[0].name)

    g.removeTopCards()

    topcards = g.getTopCards()
    print(topcards[0].name)
