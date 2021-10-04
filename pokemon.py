class Pokemon:

    def __init__(self, input_dictionary):
        self.name = input_dictionary["name"]
        self.artwork = input_dictionary["artwork"]
        self.attack = input_dictionary["attack"]
        self.defense = input_dictionary["defence"]
        self.type1 = input_dictionary["type1"]
        self.type2 = input_dictionary["type2"]

    def SQLFormat(self):
        # convert pokemon data into SQL format for database
        pass
