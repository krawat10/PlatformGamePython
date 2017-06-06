import Organism
import random

class Plant(Organism.Organism):

    def __init__(self, x, y, world):
        Organism.Organism.__init__(self, x, y, world)
    
    def _initFeatures(self):
        self._initative = 0
        self._strength = 0
        self._chanceToMultiplication = 8

    def action(self):
        if (self._isAbleToMultiplication()):
            self.multiplication()

    def _isAbleToMultiplication(self):
        return (random.randint(0, self._chanceToMultiplication - 1) == 1)

