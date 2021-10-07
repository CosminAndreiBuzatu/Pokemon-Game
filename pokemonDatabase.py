# database class/functions. create and use a SQL database
import sqlite3
from pokemon import Pokemon
from fetchApi import *


class PokemonDatabase:

    def __init__(self):
        try:
            self.database = sqlite3.connect(f"gameDatabase.db")
            self.cursor = self.database.cursor()
            self.createPokemonTable()
        except Exception as e:
            print(e)

    def __del__(self):
        self.database.close()

    def createPokemonTable(self):
        # Create a SQL Table
        sqlCommand = f'''
            CREATE TABLE IF NOT EXISTS Pokemon ( Name TEXT, Artwork TEXT, Attack INT, Defence INT, Types TEXT )
        '''
        self.cursor.execute(sqlCommand)
        self.database.commit()

    def clearPokemonTable(self):
        sqlCommand = f'''
            DELETE FROM Pokemon
        '''
        self.cursor.execute(sqlCommand)
        self.database.commit()

    def addPokemon(self, pokemon):
        values = [pokemon.name, pokemon.artwork, pokemon.attack, pokemon.defense, ' '.join(pokemon.types)]
        sqlCommand = f'''
            INSERT INTO Pokemon ( Name, Artwork, Attack, Defence, Types ) 
            VALUES ( ? , ? , ? , ? , ? );
        '''
        self.cursor.execute(sqlCommand, values)
        self.database.commit()

    def addManyPokemon(self, listOfPokemon):
        for pokemon in listOfPokemon:
            self.addPokemon(pokemon)

    def getPokemon(self, name):
        sqlCommand = f'''
            SELECT * FROM Pokemon
            WHERE Name = ?;
        '''
        self.cursor.execute(sqlCommand, [name])
        rows = self.cursor.fetchall()

        if len(rows) == 0:
            return "Error, no pokemon found"
        else:
            return self.SQLToPokemon(rows[0])

    def getAllPokemon(self):
        sqlCommand = '''
            SELECT * FROM Pokemon
        '''

        self.cursor.execute(sqlCommand)
        rows = self.cursor.fetchall()

        if len(rows) == 0:
            return "Error, no pokemon found"

        output = []
        for row in rows:
            pokemon = self.SQLToPokemon(row)
            output.append(pokemon)
        return output


    def SQLToPokemon(self, row):
        dict = {
            "name": row[0],
            "artwork": row[1],
            "attack": row[2],
            "defense": row[3],
            "types": row[4].split()
            }

        return Pokemon(dict)

    def getAllNames(self):

        sqlCommand = f'''
            SELECT Name FROM Pokemon;
        '''
        self.cursor.execute(sqlCommand)
        rows = self.cursor.fetchall()

        if len(rows) == 0:
            return "Error, no pokemon found"
        else:
            listForm = [x[0] for x in rows]
            return listForm

    def downloadPokemon(self):
        self.clearPokemonTable()
        listOfPokemon = fetchManyPokemon(1, 151)
        self.addManyPokemon(listOfPokemon)

if __name__ == "__main__":
    db = PokemonDatabase()
    db.clearPokemonTable()
    db.downloadPokemon()
    listp = db.getAllPokemon()
    print(listp)
