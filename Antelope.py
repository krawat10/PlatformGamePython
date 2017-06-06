import Animal
import random

class Antelope(Animal.Animal):

    def __init__(self, x, y, world):
        Animal.Animal.__init__(self, x, y, world)
    
    def action(self):
        for i in range(0, 2):
            Animal.Animal.action(self)
            if(not self._isAlive):
                self.setIsAlive(False)
                return
        

    def isPushBackAttack(self, attacker):

        chance = random.randint(0, 1)
        if ((chance == 0) & (attacker.getName() != self._name)):
            isMoved = False
            while (not isMoved):
                self._newXY = self.newRandomPositionAround()
                isMoved = self._moveToOpenPosition()
                self._world.getView().setNewMessage("Antelope ran away.")
                return True
        else:
            return Animal.Animal.isPushBackAttack(self, attacker)

        return False
    
    
    def _initFeatures(self):
        self._name = "Antelope"
        self._initative = 4
        self._strength = 4
    
