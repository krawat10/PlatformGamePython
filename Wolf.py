import Animal

class Wolf(Animal.Animal):

    def __init__(self, x, y, world):
        Animal.Animal.__init__(self, x, y, world)

    def _initFeatures(self):
        self._name = "Wolf"
        self._initative = 5
        self._strength = 9

    