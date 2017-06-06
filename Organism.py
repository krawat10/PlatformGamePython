from abc import ABCMeta, abstractmethod
import World
import OrganismFactory



class Organism:

    def __init__(self, x, y, world):
        print("Organism")
        self._strength = None
        self._initative = None
        self._name = None
        self._isAlive = None
        self.setIsAlive(True)
        self._world = world
        self._x = x
        self._y = y
        self._newXY = (0, 0)
        self._initFeatures()
        self._world.getView().drawObject(self._x, self._y, self._name)


    @abstractmethod
    def _initFeatures(self):
        pass

    def getStrength(self):
        return self._strength
    
    def setStrength(self, value):
        self._strength = value

    def getInitative(self):
        return self._initative

    def getX(self):
        return self._x

    def setX(self, value):
        self._x = value

    def getY(self):
        return self._y

    def setY(self, value):
        self._y = value

    def getName(self):
        return self._name

    def getIsAlive(self):
        return self._isAlive

    def setIsAlive(self, value):
        self._isAlive = value
        if not value:
            self._world.getView().setNewMessage(str(self._name) + " is dead")
            self._world.getView().deleteObject(self._x, self._y)

    @abstractmethod
    def action(self):
        pass

    def AIsLessThanB(self, second_organism):
        return self.getStrength() < second_organism.getStrength()

    def _draw(self, x, y):
        self._world.getView().deleteObject(self._x, self._y)
        self._world.getView().drawObject(x, y, self._name)
        self._x = x
        self._y = y

    def isPushBackAttack(self, attackrer):
        print("org pushback")
        if self.AIsLessThanB(attackrer):
            self.setIsAlive(False)
            return False
        else:
            attackrer.setIsAlive(False)
            return True

    def newRandomPositionAround(self):
        return self._world.getView().positionAround(self._x, self._y)

    def multiplication(self):
        for i in range(0, 8):
            self._newXY = self.newRandomPositionAround()
            if (self._world.checkPosition(self._newXY[0], self._newXY[1]) == World.PositionStatus.OPEN):
                print("multi")
                newOrganism = OrganismFactory.OrganismFactory(self._world, self._newXY[0], self._newXY[1]).GetObject(self._name)
                self._world.addCreature(newOrganism)
                return

