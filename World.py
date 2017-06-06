import random
from enum import Enum
import GridView
import IOOperation
import OrganismFactory
import HexagonalView
class PositionStatus(Enum):
    FOBBIDEN = 1
    OPEN = 2
    MONSTER = 3

class KeyName(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    DISACTIVATED = 5
    SHIELD = 6

class World(IOOperation.IOOperation):
    def __init__(self, sizeX, sizeY):
        self.__sizeX = sizeX
        self.__sizeY = sizeY
        self.__organism = []
        self.__numberOfCreatures = 0
        self.__activeKey = KeyName.DISACTIVATED
        self.__view = HexagonalView.HexagonalView()
        self.__isHuman = False
        self.__initView()
        

    def __initView(self):
        self.__view.setWorld(self)
        self.__view.setSizeX(self.__sizeX)
        self.__view.setSizeY(self.__sizeY)
        self.__view.initViewSettings()
        

    def getCreature(self, x, y):
        for org in self.__organism:
            if (org.getX() == x) & (org.getY() == y):
                return org
        return None

    def clearDeadMonster(self):
        for org in self.__organism:
            if not org.getIsAlive():
                self.__numberOfCreatures -= 1
                self.__organism.remove(org)

    def tour(self):
        self.__organism.sort(key=lambda x: x.getStrength(), reverse=True)     

        duplicate = None
        
        for org in self.__organism:
            if(duplicate == org):
                continue
            org.action()
            duplicate = org
            self.clearDeadMonster()
        self.__activeKey = KeyName.DISACTIVATED

    def getFreeSpot(self):
        isInitalized = False
        randX = None
        randY = None
        rand = random.Random()
        while not isInitalized:
            randX = rand.randint(0, self.__sizeX - 1)
            randY = rand.randint(0, self.__sizeY - 1)
            if self.checkPosition(randX, randY) == PositionStatus.OPEN:
                isInitalized = True

        return (randX, randY)

    def attackMonsterAtPosition(self, x, y, attacker):
        print("attackMonsterAtPosition")
        isDefended = None
        for org in self.__organism:
            if (org.getX() == x) & (org.getY() == y):
                message = attacker.getName() + " attack " + org.getName()
                self.getView().setNewMessage(message)
                isDefended = org.isPushBackAttack(attacker)
                return not isDefended
        return False

    def getList(self):
        return self.__organism

    def getImput(self):
        return self.__activeKey

    def setImput(self, value):
        self.__activeKey = value

    def setNumberOfCreatures(self, value):
        self.__numberOfCreatures = value

    def getNumberOfCreature(self):
        return self.__numberOfCreatures

    def addCreature(self, org):
        self.__organism.append(org)

    def checkPosition(self, x, y):
        if ((x < 0) | (x > self.__sizeX - 1) | (y < 0) | (y > self.__sizeY - 1)):
            return PositionStatus.FOBBIDEN
        
        for org in self.__organism:
            if ((org.getX() == x) & (org.getY() == y)):
                return PositionStatus.MONSTER

        return PositionStatus.OPEN

    def getView(self):
        return self.__view

    def setIsHuman(self, value):
        self.__isHuman = value
    
    def getIsHuman(self):
        return self.__isHuman



    def Serialize(self, output):
        f = open(output, 'w')   
        gridName = self.__view.__class__.__name__
        f.write(gridName + '\n')
        f.write(str(self.__sizeX) + '\n')
        f.write(str(self.__sizeY) + '\n')
        f.write(str(len(self.__organism)) + '\n')
        for organism in self.__organism:
            if (organism.getIsAlive()):
                f.write(str(organism.__class__.__name__) + '\n')
                f.write(str(organism.getX()) + '\n')
                f.write(str(organism.getY()) + '\n')
            if (organism.getName() == "Human"):
                f.writeBoolean(str(True) + '\n')
                f.write(str(organism.getAzureShield()) + '\n')
                f.write(str(organism.getAzureShieldTour()) + '\n')
            else:
                f.write(str(False) + '\n')
        f.close()

    def Deserialize(self, input):
        f = open(input, 'r')   
        self.__organism.clear()
        self.__numberOfCreatures = 0
        
        gridName = f.readline().rstrip()
        self.__sizeX = int(f.readline().rstrip())
        self.__sizeY = int(f.readline().rstrip())
        self.__view.closeWindow()
        if (gridName == "GridView"):
            self.__view = GridView.GridView()
        else:
            self.__view = HexagonalView.HexagonalView()
        
        self.__view.setWorld(self)
        self.__view.setSizeX(self.__sizeX)
        self.__view.setSizeY(self.__sizeY)
        self.__view.initUI()
        count = int(f.readline())
        for j in range(0, count):
            name = f.readline().rstrip()
            sizeX = int(f.readline().rstrip())
            sizeY = int(f.readline().rstrip())
            isHuman = f.readline().rstrip()
            if isHuman == 'False': isHuman = False
            else: isHuman = True
            if (isHuman):
                AzureShield = bool(f.readline().rstrip())
                AzureShieldTour = int(f.readline().rstrip())
                human = OrganismFactory.OrganismFactory(self, sizeX, sizeY).GetObject(name) 
                human.setAzureShield(AzureShield)
                human.setAzureShieldTour(AzureShieldTour)
                self.addCreature(human)
            else:
                factory = OrganismFactory.OrganismFactory(self, sizeX, sizeY)
                obj = factory.getInstance(sizeX, sizeX, name)
                self.addCreature(obj)
            print(name)
            self.__numberOfCreatures += 1
        f.close()
        self.__view.initLoop()

    def newGame(self, sizeX, sizeY, view):
        self.__organism.clear()
        self.__numberOfCreatures = 0
        self.__sizeX = sizeX
        self.__sizeY = sizeY
        self.__view.closeWindow()
        if (view == "GridView"):
            self.__view = GridView.GridView()
        else:
            self.__view = HexagonalView.HexagonalView()
        self.__view.setWorld(self)
        self.__view.setSizeX(self.__sizeX)
        self.__view.setSizeY(self.__sizeY)
        self.__view.initUI()
        self.__view.initLoop()
