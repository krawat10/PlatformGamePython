import Animal
import random

class Turtle(Animal.Animal):


    def __init__(self, x, y, world):
        Animal.Animal.__init__(self, x, y, world)

    def _initFeatures(self):
        self._name = "Turtle"
        self._initative = 1
        self._strength = 2

    def action(self):
        isMove = random.randint(0, 4)
        if (isMove == 0):
            Animal.Animal.action(self)

    def isPushBackAttack(self, attacker):
        if (attacker.getStrength() >= 5):
            self.setIsAlive(False)
            return False
        elif (attacker.getName() ==  self._name):
            self.multiplication()
            return True
        else:
            return True
