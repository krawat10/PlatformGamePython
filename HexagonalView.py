import tkinter as tk
import World
from abc import ABCMeta, abstractmethod
import OrganismFactory
import tkinter.filedialog
import random
import View

class HexagonalView(View.View):
    def __init__(self):           
        View.View.__init__(self)
        self._numberOfFieldsAroundOne = 6
        self._gridOfCanvas = None

    def positionAround(self, x, y):        
        return self.getPositionAround(x, y, random.randint(0, 5))
  
    def _initFuncButtons(self):
        View.View._initFuncButtons(self)       
        self._save_button.place(x=1, y=20*(self._sizeY + 1))
        self._load_button.place(x=1, y=20*(self._sizeY+3))    
        self._tour_button.place(x=1, y=20*(self._sizeY+5))
        self._new_button.place(x=1, y=20*(self._sizeY+7))
        self._listbox.place(x=(self._sizeX)*self._sizeOfRectangle, y=(self._numberOfVisibleMessages + 4)*self._sizeOfRectangle)
    def _initMessages(self):
        for i in range(0, self._numberOfVisibleMessages):
            label = tk.Label(self._sGui, text="message")
            label.place(x=self._sizeOfRectangle + 10, y=25*(self._sizeY+i*3))       
            self._messages.append(label)
      


    def getPositionAround(self, x, y, indexOfField):
        p = (None,None)
        if y%2 == 0:
            if indexOfField == 0:
                p = (x, y - 2)
            elif indexOfField == 1:
                p = (x, y - 1)
            elif indexOfField == 2:
                p = (x, y + 1)
            elif indexOfField == 3: 
                p = (x, y + 2)
            elif indexOfField == 4:
                p = (x - 1, y + 1)
            elif indexOfField == 5:
                p = (x - 1, y - 1)
            else:
                p = (x, y)
        else:
            if indexOfField == 0:
                p = (x, y - 2)
            elif indexOfField == 1:
                p = (x + 1, y - 1)
            elif indexOfField == 2:
                p = (x + 1, y + 1)
            elif indexOfField == 3: 
                p = (x, y + 2)
            elif indexOfField == 4:
                p = (x, y + 1)
            elif indexOfField == 5:
                p = (x, y - 1)
            else:
                p = (x, y)

            
        return p
    
    def newDirection(self, x, y, key):        
        newFieldIndex = None

        if key == World.KeyName.UP:
                newFieldIndex = 0
        elif key == World.KeyName.DOWN:
                newFieldIndex = 3
        elif key == World.KeyName.LEFT:
                if y%2 == 0:
                    newFieldIndex = 4
                else:
                    newFieldIndex = 5
        elif key == World.KeyName.RIGHT:
                if y%2 == 0:
                    newFieldIndex = 2
                else:
                    newFieldIndex = 1
        else:
               newFieldIndex = -1
        newField = self.getPositionAround(x, y, newFieldIndex);        
        return newField

    def initButton(self):      
                          
        self._gridOfObject = [None] * self._sizeY * self._sizeX 
        self._gridOfCanvas = [None] * self._sizeY * self._sizeX 
        canvas = tk.Canvas(self._sGui)
        canvas.pack()
        for i in range(0, self._sizeY):
            for j in range(0, self._sizeX):
                button = tk.Button(self._sGui, text = '.', command = lambda idx = j, idy = i: self._addAtPosition(idx, idy))
                button.config(font=('helvetica', 5, 'underline italic'))
                a1 = canvas.create_polygon([30,3,10,3,0,20,10,37,30,37,40,20], outline='black', fill='gray', width=2)
                if i%2 == 0:
                    canvas.move(a1, 60*j, 35*i/2)
                    button.place(x=60*j+8, y=35*i/2+10, width=25, height=20)
                else:
                    canvas.move(a1, 60*j + 30, 35*i/2)
                    button.place(x=(60*j + 30)+8, y=35*i/2+10, width=25, height=20)
                self._gridOfButtons.append(button)
                self._gridOfObject[i*self._sizeX + j] = "."
