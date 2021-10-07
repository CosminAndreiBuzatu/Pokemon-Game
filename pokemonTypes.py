class Types:

    def __init__(self, input):
        self.name = input["name"]
        self.doubleDamage = input["doubleDamage"]
        self.halfDamage = input["halfDamage"]
        self.noDamage = input["noDamage"]

    def showDamageMultiplier(self,name):
        if name in self.doubleDamage:
            return 2
        if name in self.halfDamage:
            return 0.5
        if name in self.noDamage:
            return 0
        else:
            return 1


    def calculateDamageMultiplier(self,listTypes):
        result = 1
        for type in listTypes:
           result = result * self.showDamageMultiplier(type)
        return result