# database class/functions. create and use a SQL database
import sqlite3

import constants
from pokemon import Pokemon
from fetchApi import *



class PokemonDatabase:

    def __init__(self):
        try:
            self.database = sqlite3.connect(f"gameDatabase.db")
            self.cursor = self.database.cursor()
            self.createPokemonTable()
            self.createTypesTable()
            self.addDummyDataTypes(constants.types_dict)
            self.addDummyDataPokemon(constants.bulbasaur_dict)
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

    def addDummyDataTypes(self, dummy):
        fix = [dummy["name"],dummy["doubleDamage"], dummy["halfDamage"],dummy["noDamage"]]
        sqlCommand = f'''
            INSERT INTO Type ( Name, DoubleDamage, HalfDamage, NoDamage ) 
            VALUES ( ? , ? , ? , ? );
        '''
        self.cursor.execute(sqlCommand, fix)
        self.database.commit()

    def addDummyDataPokemon(self,dummy):
        fix = [dummy["name"], dummy['artwork'],
             dummy['attack'], dummy['defence'], dummy['types']]
        sqlCommand = f'''
            INSERT INTO Pokemon ( Name, Artwork, Attack, Defence, Types ) 
            VALUES ( ? , ? , ? , ? , ? );
        '''
        self.cursor.execute(sqlCommand,fix)
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
        listOfPokemon = pokemonApiObject.fetchManyPokemon(1, 151)
        self.addManyPokemon(listOfPokemon)
        self.downloadTypes()


    def createTypesTable(self):
        # Create a SQL Table
        sqlCommand = f'''
            CREATE TABLE IF NOT EXISTS Type ( Name TEXT, DoubleDamage TEXT, HalfDamage TEXT, NoDamage TEXT)
        '''
        self.cursor.execute(sqlCommand)
        self.database.commit()

    def addTypes(self, type):
        values = [type.name, ' '.join(type.doubleDamage), ' '.join(type.halfDamage), ' '.join(type.noDamage)]
        sqlCommand = f'''
            INSERT INTO Type ( Name, DoubleDamage, HalfDamage, NoDamage ) 
            VALUES ( ? , ? , ? , ? );
        '''
        self.cursor.execute(sqlCommand, values)
        self.database.commit()

        return Types(dict)

    def dBToType(self, row):
        dict = {
            "name": row[0],
            "doubleDamage": row[1].split(),
            "halfDamage": row[2].split(),
            "noDamage": row[3].split()
            }

        return Types(dict)

    def getType(self, name):
        sqlCommand = f'''
            SELECT * FROM Type
            WHERE name = ?;
        '''
        self.cursor.execute(sqlCommand, [name])
        type = self.cursor.fetchall()
        return self.dBToType(type[0])



    def addAllTypes(self, listOfTypes):
        for type in listOfTypes:
            self.addTypes(type)

    def clearTypesTable(self):
        sqlCommand = f'''
            DELETE FROM Type
        '''
        self.cursor.execute(sqlCommand)
        self.database.commit()

    def downloadTypes(self):
        self.clearTypesTable()
        listOfTypes = pokemonApiObject.fetchAllTypes(1, 18)
        self.addAllTypes(listOfTypes)

if __name__ == "__main__":
    db = PokemonDatabase()
    db.clearPokemonTable()
    db.downloadPokemon()
    listp = db.getAllPokemon()
    print(db.getType('electric'))
    print(listp)

