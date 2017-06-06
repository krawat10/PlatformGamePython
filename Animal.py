import World
import Organism

class Animal(Organism.Organism):   
    
    def __init__(self, x, y, world):
        Organism.Organism.__init__(self, x, y, world)
        
    def action(self):
        isMoved = False
        count = 20
        while (not isMoved & (count - 1 > 0)):
            self._newXY = self.newRandomPositionAround()
            isMoved = self._move()


    def _move(self):
        if (self._world.checkPosition(self._newXY[0], self._newXY[1]) == World.PositionStatus.OPEN):
            self._draw(self._newXY[0], self._newXY[1])
            return True
        elif (self._world.checkPosition(self._newXY[0], self._newXY[1]) == World.PositionStatus.MONSTER):
            print("attack")
            if (self._attack(self._newXY[0], self._newXY[1])):
                self._draw(self._newXY[0], self._newXY[1])
                return True
            else:
                return True
        return False

    def _moveToOpenPosition(self):
        if (self._world.checkPosition(self._newXY[0], self._newXY[1]) == World.PositionStatus.OPEN):
            self._draw(self._newXY[0], self._newXY[1])
            return True
        
        return False
    

    def _attack(self, enemyX, enemyY):
        return self._world.attackMonsterAtPosition(enemyX, enemyY, self)
    

    def isPushBackAttack(self, attacker):
        print("animal pushback")
        if (attacker.getName() == self._name):
            self.multiplication()
            return True
        else: 
            return Organism.Organism.isPushBackAttack(self, attacker)
        
