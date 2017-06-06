import Animal
import World

class Fox(Animal.Animal):
    def __init__(self, x, y, world):
        Animal.Animal.__init__(self, x, y, world)
    
    def _isStronger(self):
        if (self._world.getCreature(self._newXY[0], self._newXY[1]).getName() == self._name):   
            return True
        elif (self.getStrength() > self._world.getCreature(self._newXY[0], self._newXY[1]).getStrength()):
            return True
        else: 
            self._world.getView().setNewMessage("Fox is running from bigger animals")
            return False
    
    def _move(self):
        if (self._world.checkPosition(self._newXY[0], self._newXY[1]) == World.PositionStatus.OPEN):
            self._draw(self._newXY[0], self._newXY[1])
            return True
        elif (self._world.checkPosition(self._newXY[0], self._newXY[1]) == World.PositionStatus.MONSTER):
            if (self._isStronger()):
                if (self._attack(self._newXY[0], self._newXY[1])):
                    self._draw(self._newXY[0], self._newXY[1])
                    return True
                else:                
                    return True
        return False
    
    def _initFeatures(self):
        self._name = "Fox"
        self._initative = 7
        self._strength = 3
