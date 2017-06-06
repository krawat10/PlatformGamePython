import Animal
import World

class Human(Animal.Animal):

    def __init__(self, x, y, world):
        self._alzureShieldTour = 0
        self._alzureShield = False
        Animal.Animal.__init__(self, x, y, world)
    
    
    def _initFeatures(self):
        self._name = "Human"
        self._initative = 4
        self._strength = 5
    
    def getAzureShield(self):
        return self._alzureShield


    def getAzureShieldTour(self):
        return self._alzureShieldTour

    def setAzureShield(self, alzureShield):
        self._alzureShield = alzureShield

    def setAzureShieldTour(self, tours):
        self._alzureShieldTour = tours

    def isPushBackAttack(self, attacker):
        if (self._alzureShield):
            isNewSpot = False
            for i in range (0, 9):
                self._newXY = self.newRandomPositionAround()
                if (self._world.checkPosition(self._newXY[0], self._newXY[1]) == World.PositionStatus.OPEN):
                    attacker.draw(self._newXY[0], self._newXY[1])
                    break
            return True
        else:
            return Animal.Animal.isPushBackAttack(self, attacker)


    def action(self):
        direction = self._world.getImput()
        if (direction == World.KeyName.DISACTIVATED):
            return
        self._alzureShieldTour -= 1
        if ((self._alzureShieldTour == 0) & self._alzureShield):
            self._alzureShield = False
            self._world.getView().setNewMessage("Alzure Shield deactivated.")
        if (direction == World.KeyName.SHIELD):
            if (self._alzureShieldTour < 0):
                self._alzureShield = True
                self._alzureShieldTour = 5
                self._world.getView().setNewMessage("Azure shield activated!")
            return
        else:
            self._newXY = self._world.getView().newDirection(self._x, self._y, direction)
            

        if (self._world.checkPosition(self._newXY[0], self._newXY[1]) == World.PositionStatus.OPEN):
            self._draw(self._newXY[0], self._newXY[1])
        elif (self._world.checkPosition(self._newXY[0], self._newXY[1]) == World.PositionStatus.MONSTER):
            if (self._attack(self._newXY[0], self._newXY[1])):
                self._draw(self._newXY[0], self._newXY[1])
            else:
                if(not self._isAlive):
                    self.setIsAlive(False)
                return
        