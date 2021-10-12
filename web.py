# This file is for creating and running site using Flask

from flask import Flask, render_template, request
from constants import *
from game import Game
from pokemonDatabase import PokemonDatabase
from pokemon import Pokemon

app = Flask(__name__)
pokemonGame = Game()


@app.route("/")
def mainPage():
    return render_template('mainPage.html')


@app.route("/pokedex")
def pokedex():
    db = PokemonDatabase()
    names = db.getAllNames()
    inputName = request.args.get("name")
    if inputName is not None:
        pokemon = db.getPokemon(inputName)
    elif names:
        inputName = names[0]
        pokemon = db.getPokemon(inputName)
    else:
        pokemon = Pokemon(bulbasaur_dict)
        pokemon.name = "Empty database"

    return render_template('Pokedex.html', pokemon=pokemon, names=names)


@app.route("/card", methods=["GET", "POST"])
def card():
    db = PokemonDatabase()
    names = db.getAllNames()
    inputName = request.args.get("name")

    if inputName is not None:
        print(f"---{inputName}---")
        if inputName in names:
            pokemon = db.getPokemon(inputName)
        elif names:
            inputName = names[0]
            pokemon = db.getPokemon(inputName)
        else:
            pokemon = Pokemon(bulbasaur_dict)
            pokemon.name = "Empty database"
    else:
        pokemon = Pokemon(bulbasaur_dict)
        pokemon.name = "Empty database"

    return render_template('card.html', pokemon=pokemon)


@app.route("/downloadPokemon")
def downloadPokemon():
    db = PokemonDatabase()
    db.downloadPokemon()

    names = db.getAllNames()
    if names:
        inputName = names[0]
        pokemon = db.getPokemon(inputName)
    else:
        pokemon = Pokemon(bulbasaur_dict)
        pokemon.name = "Empty database"

    return render_template('Pokedex.html', pokemon=pokemon, names=names)


@app.route("/cardGameNew")
def cardGameNew():
    pokemonGame.getNewDecks()
    pokemonGame.randomiseTurn()

    return render_template('cardGame.html', game=pokemonGame)


@app.route("/selectMove")
def selectMove():
    return render_template('selectMove.html', game=pokemonGame)


@app.route("/cardGameDisplay")
def cardGameDisplay():
    return render_template('cardGameDisplay.html', game=pokemonGame)


@app.route("/cardsLeft")
def cardsLeft():
    player = request.args.get("player")
    player = int(player)
    return render_template('cardsLeft.html', game=pokemonGame, player=player)


@app.route("/userAttacks")
def cardGameUserAttacked():
    attackType = request.args.get("attackType")
    pokemonGame.userAttacks(attackType)
    print(f"User uses {attackType}")
    output = {
        "name1": pokemonGame.deck1[0].name,
        "name2": pokemonGame.deck2[0].name
    }
    return output


@app.route("/AiAttacks")
def cardGameAiAttacked():
    attackType = pokemonGame.AiPickAttack()
    pokemonGame.AiAttacks(attackType)
    print("Ai has attacked")
    output = {
        "name1": pokemonGame.deck1[0].name,
        "name2": pokemonGame.deck2[0].name
    }
    return output


@app.route("/cardGameDownload")
def cardGameDownload():
    db = PokemonDatabase()
    db.downloadPokemon()
    pokemonGame = Game()

    return render_template('mainPage.html', game=pokemonGame)


app.run()
