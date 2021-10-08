from game import Game
from fetchApi import *

def test_gameCanMakeEvenDecks():
    game = Game()
    game.getNewDecks()

    assert len(game.deck1) == len(game.deck2)


def test_gameCanRemoveTopCards():
    game = Game()
    game.getNewDecks()

    deckStartSize = len(game.deck1)

    game.removeTopCards()

    deckEndSize = len(game.deck1)

    assert deckEndSize == deckStartSize - 1


def test_gameShowsNoneWhenNoCardsInDeck():
    game = Game()
    game.getNewDecks()

    deckStartSize = len(game.deck1)

    for card in range(deckStartSize):
        game.removeTopCards()

    topCards = game.getTopCards()

    assert topCards == [None, None]


def test_gameReturnsNumberOfCardsInDeck():
    game = Game()
    game.getNewDecks()

    deckStartSize = game.getCardsLeft()

    game.removeTopCards()

    deckEndSize = game.getCardsLeft()

    assert deckEndSize[0] == deckStartSize[0] - 1

def test_fightingVsRock():
    fighting = pokemonApiObject.fetchTypes(2)
    rock = pokemonApiObject.fetchTypes(6)

    fighting.showDamageMultiplier(rock.name)

    assert fighting.showDamageMultiplier(rock.name) == 2

def test_fightingRockGrass():
    fighting =pokemonApiObject.fetchTypes(2)
    rock = pokemonApiObject.fetchTypes(6)
    grass = pokemonApiObject.fetchTypes(12)

    defender = fighting.calculateDamageMultiplier([rock.name,grass.name])

    assert defender == 2

def test_fightingRockFairy():
    fighting =pokemonApiObject.fetchTypes(2)
    rock = pokemonApiObject.fetchTypes(6)
    fairy = pokemonApiObject.fetchTypes(18)

    defender = fighting.calculateDamageMultiplier([rock.name,fairy.name])

    assert defender == 1


def test_fightingVsRockFairyGhost():
    fighting =pokemonApiObject.fetchTypes(2)
    rock = pokemonApiObject.fetchTypes(6)
    fairy = pokemonApiObject.fetchTypes(18)
    ghost = pokemonApiObject.fetchTypes(8)

    defender = fighting.calculateDamageMultiplier([rock.name,fairy.name,ghost.name])

    assert defender == 0


def test_fightingVsNone():
    fighting =pokemonApiObject.fetchTypes(2)

    defender = fighting.calculateDamageMultiplier([])

    assert defender == 1

