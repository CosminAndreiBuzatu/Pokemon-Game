# This file is for creating and running site using Flask

from flask import Flask, render_template, request
from constants import *
from game import Game
from pokemonDatabase import PokemonDatabase


app = Flask(__name__)
pokemonGame = Game()
db = PokemonDatabase()

@app.route("/")
def index():
    return render_template('mainPage.html')


@app.route("/pokedex")
def pokedex():
    names = db.getAllNames()
    if names:
        inputName = names[0]
        pokemon = db.getPokemon(inputName)
    else:
        pokemon = Pokemon(bulbasaur_dict)
        pokemon.name = "Empty database"

    return render_template('Pokedex.html', pokemon=pokemon, names=names)


@app.route("/downloadPokemon")
def downloadPokemon():
    db.downloadAllPokemon()

    names = db.getAllNames()
    if names:
        inputName=names[0]
        pokemon = db.getPokemon(inputName)
    else:
        pokemon = Pokemon(bulbasaur_dict)
        pokemon.name = "Empty database"

    return render_template('Pokedex.html', pokemon=pokemon, names=names)

