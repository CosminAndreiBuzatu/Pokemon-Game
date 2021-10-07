class Pokemon:

    def __init__(self, input_dictionary):
        self.name = input_dictionary["name"]
        self.artwork = input_dictionary["artwork"]
        self.attack = input_dictionary["attack"]
        self.defense = input_dictionary["defense"]
        self.types = input_dictionary["types"]

    def __str__(self):
        return self.name

    def SQLFormat(self):
        # convert pokemon data into SQL format for database
        pass

    def getTypes(self):
        typesString = " ".join(self.types)
        return typesString