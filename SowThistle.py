import Plant

class SowThistle(Plant.Plant):

    def __init__(self, x, y, world):
        Plant.Plant.__init__(self, x, y, world)

    def _initFeatures(self):
        Plant.Plant._initFeatures(self)
        self._name = "SowThistle"

    def action(self):
        for i in range(0, 3):
            Plant.Plant.action(self)
