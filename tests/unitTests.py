from game import Game


def gameCanMakeEvenDecks():
    game = Game()
    game.getNewDecks()

    assert len(game.deck1) == len(game.deck2)


def gameCanRemoveTopCards():
    game = Game()
    game.getNewDecks()

    deckStartSize = len(game.deck1)

    game.removeTopCards()

    deckEndSize = len(game.deck1)

    assert deckEndSize == deckStartSize - 1


def gameShowsNoneWhenNoCardsInDeck():
    game = Game()
    game.getNewDecks()

    deckStartSize = len(game.deck1)

    for card in range(deckStartSize):
        game.removeTopCards()

    topCards = game.getTopCards()

    assert topCards == [None, None]


def gameReturnsNumberOfCardsInDeck():
    game = Game()
    game.getNewDecks()

    deckStartSize = game.getCardsLeft()

    game.removeTopCards()

    deckEndSize = game.getCardsLeft()

    assert deckEndSize[0] == deckStartSize[0] - 1