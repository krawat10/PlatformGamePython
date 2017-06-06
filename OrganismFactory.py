import Wolf
import Antelope
import CyberSheep
import Fox
import Grass
import Guarana
import Human
import Sheep
import SosnowskyBorsch
import SowThistle
import Turtle
import Wolfberry



class OrganismFactory:

    def __init__(self, world = None, x = None, y = None):
        self.__x = x
        self.__y = y
        self.__world = world
        self.__names = [ "Wolf", "Fox", "Grass", "Guarana", "SosnowskyBorsch",
    "SowThistle", "Turtle", "Wolfberry", "Sheep", "CyberSheep", "Human", "Antelope"]
    
    def getNamesOfOrganisms(self):
        return self.__names

    def getInstance(self, x, y, name):
        self.x = x
        self.y = y
        return self.GetObject(name)        
    

    def GetObject(self, name):
        print(name)
        if name == "Wolf":
                return Wolf.Wolf(self.__x, self.__y, self.__world)
        elif name == "Fox":
                return Fox.Fox(self.__x, self.__y, self.__world)
        elif name == "Grass":
                print("It's grass!")
                return Grass.Grass(self.__x, self.__y, self.__world)
        elif name == "Guarana":
                return Guarana.Guarana(self.__x, self.__y, self.__world)
        elif name == "SosnowskyBorsch":
                return SosnowskyBorsch.SosnowskyBorsch(self.__x, self.__y, self.__world)
        elif name == "SowThistle":
                return SowThistle.SowThistle(self.__x, self.__y, self.__world)
        elif name == "Turtle":
                return Turtle.Turtle(self.__x, self.__y, self.__world)
        elif name == "Wolfberry":
                return Wolfberry.Wolfberry(self.__x, self.__y, self.__world)
        elif name == "Sheep":
                return Sheep.Sheep(self.__x, self.__y, self.__world)
        elif name == "CyberSheep":
                return CyberSheep.CyberSheep(self.__x, self.__y, self.__world)
        elif name == "Antelope":
                return Antelope.Antelope(self.__x, self.__y, self.__world)
        elif name == "Human":
                return Human.Human(self.__x, self.__y, self.__world)
                        
        
        return None
