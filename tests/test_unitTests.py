from game import Game
from fetchApi import *
from pokemonDatabase import *

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

def test_dragonairBeatsVenomoth():
    db = PokemonDatabase()
    pokemonA = db.getPokemon('dragonair')
    pokemonD = db.getPokemon('venomoth')
    attackType = 'dragon'
    Winner = Game().dealDamage(pokemonA,pokemonD,attackType)

    assert Winner == True

def test_blastoiseBeatsRhydon():
    db = PokemonDatabase()
    pokemonA = db.getPokemon('blastoise')
    pokemonD = db.getPokemon('rhydon')
    attackType = 'water'
    Winner = Game().dealDamage(pokemonA,pokemonD,attackType)

    assert Winner == True

def test_gastlyBeatsMachoke():
    db = PokemonDatabase()
    pokemonA = db.getPokemon('machoke')
    pokemonD = db.getPokemon('gastly')
    attackType = 'fighting'
    Winner = Game().dealDamage(pokemonA,pokemonD,attackType)

    assert Winner == False

def test_haunterBeatsArbok():
    db = PokemonDatabase()
    pokemonA = db.getPokemon('arbok')
    pokemonD = db.getPokemon('haunter')
    attackType = 'poison'
    Winner = Game().dealDamage(pokemonA,pokemonD,attackType)

    assert Winner == False

def test_gyaradosBeatsTentacool():
    db = PokemonDatabase()
    pokemonA = db.getPokemon('gyarados')
    pokemonD = db.getPokemon('tentacool')
    attackType = 'water'
    Winner = Game().dealDamage(pokemonA,pokemonD,attackType)

    assert Winner == True