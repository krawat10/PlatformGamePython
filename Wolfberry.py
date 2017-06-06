import Plant

class Wolfberry(Plant.Plant):

    def __init__(self, x, y, world):
        Plant.Plant.__init__(self, x, y, world)

    def _initFeatures(self):
        Plant.Plant._initFeatures(self)
        self._name = "Wolfberry"
        self._strength = 99

    def isPushBackAttack(self, attacker):        
        self.setIsAlive(False);           
        attacker.setIsAlive(False)
        return True        

