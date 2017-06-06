import Animal


class CyberSheep(Animal.Animal):

    def __init__(self, x, y, world):
        Animal.Animal.__init__(self, x, y, world)  
    
    def action(self):
        currentDirectionX = None
        currentDirectionY = None
        organism_list = self._world.getList()


        for organism in organism_list:
            if organism.getName() == "SosnowskyBorsch":
                currentDirectionX = 0
                currentDirectionY = 0			
                if (self.getX() != organism.getX()):
                    if(self.getX() > organism.getX()):
                        currentDirectionX = -1
                    else:
                        currentDirectionX = 1
                if (self.getY() != organism.getY()):
                    if(self.getY() > organism.getY()):
                        currentDirectionY = -1
                    else:
                        currentDirectionY = 1

                self._newXY = (self.getX() + currentDirectionX, self.getY() + currentDirectionY) 
                self._move()
                return
        Animal.Animal.action(self)

    def _initFeatures(self):
        self._name = "CyberSheep"
        self._initative = 4
        self._strength = 11

