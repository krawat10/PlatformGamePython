import Plant

class Grass(Plant.Plant):

    def __init__(self, x, y, world):
        Plant.Plant.__init__(self, x, y, world)

    def _initFeatures(self):
        Plant.Plant._initFeatures(self)
        self._name = "Grass"
