import Plant

class Guarana(Plant.Plant):

    def __init__(self, x, y, world):
        Plant.Plant.__init__(self, x, y, world)

    def _initFeatures(self):
        Plant.Plant._initFeatures(self)
        self._name = "Guarana"

    def isPushBackAttack(self, attacker):
        newStrength = attacker.getStrength() + 3
        attacker.setStrength(newStrength)
        self.setIsAlive(False)
        return False
    