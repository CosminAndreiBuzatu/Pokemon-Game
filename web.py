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
    inputPlayer = request.args.get("player")

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
    elif inputPlayer == 1:
        pokemon = pokemonGame.deck1[0]
    elif inputPlayer == 2:
        pokemon = pokemonGame.deck2[0]
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


@app.route("/cardGameNextTurn")
def cardGameNextTurn():
    pokemonGame.removeTopCards()

    return render_template('cardGame.html', game=pokemonGame)


@app.route("/userAttacks")
def cardGameUserAttacked():
    attackType = request.args.get("attackType")
    pokemonGame.userAttacks(attackType)
    print(f"User uses {attackType}")

    return "nothing"


@app.route("/AiAttacks")
def cardGameAiAttacked():
    attackType = pokemonGame.AiPickAttack()
    pokemonGame.AiAttacks(attackType)
    print("Ai has attacked")

    return "nothing"


@app.route("/cardGameDownload")
def cardGameDownload():
    db = PokemonDatabase()
    db.downloadPokemon()
    pokemonGame = Game()

    return render_template('mainPage.html', game=pokemonGame)

# background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    print("Hello")
    return "nothing"


app.run()
