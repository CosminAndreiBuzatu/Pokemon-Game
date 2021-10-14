class Pokemon:

    def __init__(self, input_dictionary):
        self.name = input_dictionary["name"]
        self.artwork = input_dictionary["artwork"]
        self.attack = input_dictionary["attack"]
        self.defense = input_dictionary["defense"]
        self.types = input_dictionary["types"]
        self.evolutionStage = input_dictionary["evolutionStage"]
        self.evolvesTo = input_dictionary["evolvesTo"]

    def __str__(self):
        return self.name

    def SQLFormat(self):
        # convert pokemon data into SQL format for database
        pass

    def getTypes(self):
        typesString = " ".join(self.types)
        return typesString

    def evolve(self,db):
        if self.evolvesTo:
            evol = db.getPokemon(self.evolvesTo)
            evolves = db.SQLToPokemon(evol)
            self.name = evolves.name,
            self.artwork = evolves.artwork,
            self.attack = evolves.attack,
            self.defense = evolves.defense,
            self.types = evolves.types,
            self.evolutionStage = evolves.evolutionStage,
            self.evolvesTo = evolves.evolvesTo

    def toJson(self):
        output = {
            "name": self.name,
            "artwork": self.artwork,
            "attack": self.attack,
            "defense": self.defense,
            "types": self.getTypes(),
            "evolutionStage": self.evolutionStage,
            "evolvesTo" : self.evolvesTo
        }
