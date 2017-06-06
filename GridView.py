import View 
import tkinter as tk
import World
import random


class GridView(View.View):
    
    def __init__(self):           
        View.View.__init__(self)
        self._numberOfFieldsAroundOne = 8


    def positionAround(self, x, y):        

        return self.getPositionAround(x, y, random.randint(0, 7))

    def _initFuncButtons(self):
        View.View._initFuncButtons(self)
        self._save_button.place(x=(self._sizeX + 1)*self._sizeOfRectangle, y=(self._numberOfVisibleMessages)*self._sizeOfRectangle)
        self._load_button.place(x=(self._sizeX + 1)*self._sizeOfRectangle, y=(self._numberOfVisibleMessages + 1)*self._sizeOfRectangle)
        self._tour_button.place(x=(self._sizeX + 1)*self._sizeOfRectangle, y=(self._numberOfVisibleMessages + 2)*self._sizeOfRectangle)
        self._new_button.place(x=(self._sizeX + 1)*self._sizeOfRectangle, y=(self._numberOfVisibleMessages + 3)*self._sizeOfRectangle)
        self._listbox.place(x=(self._sizeX)*self._sizeOfRectangle, y=(self._numberOfVisibleMessages + 4)*self._sizeOfRectangle)
        
    def initButton(self):                
        self._gridOfObject = [None] * self._sizeY * self._sizeX 
        for i in range(0, self._sizeY):
            for j in range(0, self._sizeX):
                button = tk.Button(self._sGui, text = '.', command = lambda idx = j, idy = i: self._addAtPosition(idx, idy))
                button.config(font=('helvetica', 5, 'underline italic'))
                button.place(x=self._sizeOfRectangle*j, y=self._sizeOfRectangle*i, width=self._sizeOfRectangle, height=self._sizeOfRectangle)
                self._gridOfButtons.append(button)
                self._gridOfObject[i*self._sizeX + j] = "."
    
    def getPositionAround(self, x, y, indexOfField):
        p = (None,None)
        if indexOfField == 0:
            p = (x, y + 1)
        elif indexOfField == 1:
            p = (x + 1, y + 1)
        elif indexOfField == 2:
            p = (x + 1, y)
        elif indexOfField == 3: 
            p = (x + 1, y - 1)
        elif indexOfField == 4:
            p = (x, y - 1)
        elif indexOfField == 5:
            p = (x - 1, y - 1)
        elif indexOfField == 6:
            p = (x - 1, y)
        elif indexOfField == 7:
            p = (x - 1, y + 1)
        return p
    
    def newDirection(self, x, y, key):        
        newFieldIndex = None

        if key == World.KeyName.UP:
                newFieldIndex = 4
        elif key == World.KeyName.DOWN:
                newFieldIndex = 0
        elif key == World.KeyName.LEFT:
                newFieldIndex = 6
        elif key == World.KeyName.RIGHT:
                newFieldIndex = 2
        else:
               newFieldIndex = -1

        newField = self.getPositionAround(x, y, newFieldIndex);        
        return newField

