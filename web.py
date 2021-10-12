# This file is for creating and running site using Flask

from flask import Flask, render_template, request
from constants import *
from game import Game
from pokemonDatabase import PokemonDatabase
from pokemon import Pokemon

app = Flask(__name__)
pokemonGame = Game()


@app.route("/temp")
def index():
    return render_template('mainPage.html')


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
        pokemon = Pokemon(noPokemonDict)
        pokemon.name = "Empty database"

    return render_template('Pokedex.html', pokemon=pokemon, names=names)


@app.route("/downloadPokemon")
def downloadPokemon():
    db = PokemonDatabase()
    db.downloadPokemon()

    names = db.getAllNames()
    if names:
        inputName = names[0]
        pokemon = db.getPokemon(inputName)
    else:
        pokemon = Pokemon(noPokemonDict)
        pokemon.name = "Empty database"

    return render_template('Pokedex.html', pokemon=pokemon, names=names)


@app.route("/cardGameNew")
def cardGameNew():
    pokemonGame.getNewDecks()

    return render_template('cardGame.html', game=pokemonGame)


@app.route("/cardGameNextTurn")
def cardGameNextTurn():
    pokemonGame.removeTopCards()

    return render_template('cardGame.html', game=pokemonGame)


@app.route("/cardGameUserAttacked")
def cardGameUserAttacked():
    attackType = request.args.get("attackType")
    pokemonGame.userAttacks(attackType)

    return render_template('cardGame.html', game=pokemonGame)


@app.route("/cardGameAiAttacked")
def cardGameAiAttacked():
    attackType = pokemonGame.AiPickAttack()
    pokemonGame.AiAttacks(attackType)

    return render_template('cardGame.html', game=pokemonGame)


@app.route("/cardGameDownload")
def cardGameDownload():
    db = PokemonDatabase()
    db.downloadPokemon()
    pokemonGame = Game()

    return render_template('mainPage.html', game=pokemonGame)


app.run()
