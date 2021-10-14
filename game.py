# game class is responsible for holding and processing data concerning the game
# this is to be used in web where user interacts with it
# Todo
# - Compare the attack of the attacker with the defense of the defender, modifying the attack value based on the attacker/defender types.
# - If the attacker wins, they get the defender’s card and continue attacking the following round.
# - If the defender wins, they get the attacker’s card and also become the attacker for the following round.
# - Once a player runs out of cards completely the game is over

import random

import constants
import fetchApi
from pokemon import Pokemon
from pokemonDatabase import PokemonDatabase
from pokemonTypes import Types


class Game:
    def __init__(self):
        self.usersTurn = random.choice([True, False])
        self.winner = ""
        self.deck1 = []
        self.deck2 = []
        self.db = PokemonDatabase()

    def getNewDecks(self):
        # get 151 pokemon from database, put in a list and shuffle it, split them in two.
        newDeck = self.db.getAllFirstStagePokemon()
        random.shuffle(newDeck)

        if len(newDeck) % 2 == 1:
            newDeck.pop()
        midpoint = int(len(newDeck) / 2)
        self.deck1 = newDeck[:midpoint]
        self.deck2 = newDeck[midpoint:]

    def getTopCards(self) -> list:
        # return a list of two pokemon, one each for the two decks
        if self.deck1:
            pokemon1 = self.deck1[0]
        else:
            pokemon1 = None
        if self.deck2:
            pokemon2 = self.deck2[0]
        else:
            pokemon2 = None

        return [pokemon1, pokemon2]

    def getCardsLeft(self) -> list:
        # returns the number of cards in both decks, in a list
        n1 = len(self.deck1)
        n2 = len(self.deck2)
        return [n1, n2]

    def removeTopCards(self):
        # deletes the top cards of both decks, if no cards were in a deck, do nothing
        if self.deck1:
            del self.deck1[0]
        if self.deck2:
            del self.deck2[0]

    def randomiseTurn(self):
        self.usersTurn = random.choice([True, False])

    def usersTurn(self) -> bool:
        return self.usersTurn

    def switchTurns(self):
        self.usersTurn = not self.usersTurn

    def availableAttacks(self):
        pokemon = self.deck1[0]
        output = pokemon.types
        return output

    def AiPickAttack(self):
        pokemon = self.deck2[0]
        output = random.choice(pokemon.types)
        return output

    def AiAttacks(self, attackType) -> bool:
        didKO = self.dealDamage(self.deck2[0], self.deck1[0], attackType)

        if didKO:
            evolutionName = self.deck2[0].evolvesTo
            if evolutionName is not None:
                evolution = self.db.getPokemon(evolutionName)
                self.deck2[0] = evolution
            self.winCard(False)
            roundWin = True
        else:
            self.switchTurns()
            roundWin = False

        return roundWin
        # return self.checkForWinner() == 2

    def userAttacks(self, attackType) -> bool:
        didKO = self.dealDamage(self.deck1[0], self.deck2[0], attackType)

        if didKO:
            self.winCard(True)
            roundWin = True
            if self.deck1[0].evolvesTo:
                evol = self.db.getPokemon(self.deck1[0].evolvesTo)
                evolves = self.db.SQLToPokemon(evol)
                self.deck1[0] = evolves
        else:
            self.switchTurns()
            roundWin = False

        return roundWin
        # return self.checkForWinner() == 1

    def dealDamage(self, attacker, defender, attackType):
        attackValue = attacker.attack
        defenderValue = defender.defense
        db = PokemonDatabase()
        attackTypeObj = db.getType(attackType)
        multiplyer = attackTypeObj.calculateDamageMultiplier(defender.types)
        attackValue *= multiplyer
        return attackValue > defenderValue

    def winCard(self, userWon):
        if userWon:
            self.deck1.append(self.deck2[0])
            del self.deck2[0]
            self.takeCardToEnd(self.deck1)
        else:
            self.deck2.append(self.deck1[0])
            del self.deck1[0]
            self.takeCardToEnd(self.deck2)

    def takeCardToEnd(self,deck):
        removeCard = deck.pop(0)
        deck.append(removeCard)

    def checkForWinner(self) -> int:
        if not self.deck1:
            self.winner = "Player 2"
            return 2
        elif not self.deck2:
            self.winner = "Player 1"
            return 1
        else:
            return 0


if __name__ == "__main__":
    g = Game()
    g.getNewDecks()

    topcard1 = g.getTopCards()[0]
    g.removeTopCards()
    topcard2 = g.getTopCards()[0]
    assert topcard1 != topcard2
    topcard1 = g.deck1[0]
    g.winCard(False)
    assert topcard1 == g.deck2[-1]
