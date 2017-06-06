import Plant
import CyberSheep
import World
import Animal

class SosnowskyBorsch(Plant.Plant):

    def __init__(self, x, y, world):
        Plant.Plant.__init__(self, x, y, world)

    def _initFeatures(self):
        Plant.Plant._initFeatures(self)
        self._name = "SosnowskyBorsch"
        self._strength = 10

    def action(self):
        numberOfFieldsAround = self._world.getView().getNumberOfFieldsAroundOne()
        for i in range(0, numberOfFieldsAround):
            nextField = self._world.getView().getPositionAround(self._x, self._y, i)
            if (self._world.checkPosition(nextField[0], nextField[1]) == World.PositionStatus.MONSTER):
                if (isinstance(self._world.getCreature(nextField[0], nextField[1]), Animal.Animal)):
                    animal = self._world.getCreature(nextField[0], nextField[1])
                    if ((animal.getName() != self._name) & (not type(animal) is CyberSheep.CyberSheep)):
                        self._world.getCreature(nextField[0], nextField[1]).setIsAlive(False)
        Plant.Plant.action(self)

    def isPushBackAttack(self, attacker):
        if (type(attacker) is CyberSheep.CyberSheep):
            self.setIsAlive(False)
            return False
        else:
            attacker.setIsAlive(False)
            return True

