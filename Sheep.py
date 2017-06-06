import Animal

class Sheep(Animal.Animal):

    def __init__(self, x, y, world):
        Animal.Animal.__init__(self, x, y, world)

    def _initFeatures(self):
        self._name = "Sheep"
        self._initative = 4
        self._strength = 4

    
