import tkinter as tk
import World
from abc import ABCMeta, abstractmethod
import OrganismFactory
import tkinter.filedialog

class View:
    def __init__(self):                    
        self._sizeOfRectangle = 40
        self._numberOfVisibleMessages = 3
        self._gridOfButtons = []
        self._gridOfObject = None
        self._messages = []
        self._listbox_count = 0
        self._sGui = None
        self._save_button = None

    def closeWindow(self):
        self._sGui.destroy()

    def setWorld(self, world):
        self.__world = world
    
    @abstractmethod
    def positionAround(self, x, y):
        pass
    
    @abstractmethod
    def newDirection(self, x, y, key):
        pass

    def setSizeX(self, x):
        self._sizeX = x

    def setSizeY(self, y):
        self._sizeY = y

    def getNumberOfFieldsAroundOne(self):
        return self._numberOfFieldsAroundOne
        
     
    
    def _initMessages(self):
        for i in range(0, self._numberOfVisibleMessages):
            label = tk.Label(self._sGui, text="message")
            label.place(x=(self._sizeX)*self._sizeOfRectangle, y=i*self._sizeOfRectangle)       
            self._messages.append(label)
    
    def _initFuncButtons(self):
        self._save_button = tk.Button(self._sGui, text="Save", command=self.Save)
        self._load_button = tk.Button(self._sGui, text="Load", command=self.Load)
        self._tour_button = tk.Button(self._sGui, text="Tour", command=self._newTour)
        self._new_button = tk.Button(self._sGui, text="New", command=self.New)
        self._listbox = tk.Listbox(self._sGui)
        
        

    def __initListbox(self):
        factory = OrganismFactory.OrganismFactory()
        organism_list = factory.getNamesOfOrganisms()
        for name in organism_list:
            self.addItemToListbox(name)

    def addItemToListbox(self, item):
        self._listbox.insert(self._listbox_count, item)
        self._listbox_count += 1

    def initViewSettings(self):
        self.initUI()
        self._sGui.mainloop()
    
    def initLoop(self):
        self._sGui.mainloop()

    def initUI(self):
        self._sGui = tk.Tk()
        XSizeWindow = self._sizeOfRectangle * self._sizeX + 160
        YSizeWindow = 500
        self._sGui.geometry(str(XSizeWindow) +'x' + str(YSizeWindow))
        self._sGui.bind("<Left>", self.__key_pressed)
        self._sGui.bind("<Right>", self.__key_pressed)
        self._sGui.bind("<Up>", self.__key_pressed)
        self._sGui.bind("<Down>", self.__key_pressed)
        self._sGui.bind("<F1>", self.__key_pressed)
        self._sGui.bind("<Delete>", self.__key_pressed)
        self.initButton()        
        self._initMessages()        
        self._initFuncButtons()
        self.__initListbox()
        self._sGui.title('platform game')
        self.dotGrid()
        self.__exit_button = tk.Button(self._sGui, text = 'click!')        
        #self.gridOfButtons[1*self.sizeY + 2]["text"] = "sas"
        #self.messages[1].config(text='change the value')
        self._sGui.after(100, self.dotGrid)
    @abstractmethod
    def initButton(self):                
        pass

    def _addAtPosition(self, x, y):
        name = self.__getSelectedItem()
        print(str(x) + str(y))
        organism = OrganismFactory.OrganismFactory(self.__world, x, y).GetObject(name)
        if organism != None:
            self.__world.addCreature(organism)
        
    def _newTour(self):
        self.__world.tour()

    def __key_pressed(self, key):
        print(key.keysym)
        keyEnum = World.KeyName.DISACTIVATED
        if key.keysym == "Right": keyEnum = World.KeyName.RIGHT
        elif key.keysym == "Left": keyEnum = World.KeyName.LEFT
        elif key.keysym == "Up": keyEnum = World.KeyName.UP
        elif key.keysym == "Down": keyEnum = World.KeyName.DOWN
        elif key.keysym == "F1": keyEnum = World.KeyName.SHIELD
        elif key.keysym == "Delete": keyEnum = World.KeyName.DISACTIVATED
        self.__world.setImput(keyEnum)  
    

    def __getSelectedItem(self):
        index = self._listbox.curselection()
        return self._listbox.get(index)

    def setNewMessage(self, message):
        for i in range(self._numberOfVisibleMessages-1, 0, -1):
           self._messages[i]["text"] = self._messages[i-1]["text"]
        self._messages[0]["text"] = message

    def deleteObject(self, j, i):
        self._gridOfObject[i*self._sizeX + j] = "."
        

    def drawObject(self, j, i, name):
        self._gridOfObject[i*self._sizeX + j] = name
        self._sGui.after(100, self.dotGrid)

    def dotGrid(self):
        for x in range(0, self._sizeX):
            for y in range(0, self._sizeY):                
                self._gridOfButtons[y*self._sizeX + x]["text"] = self._gridOfObject[y*self._sizeX + x]
        
        
    def Save(self):
        filename = tk.filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
        self.__world.Serialize(filename)

    def Load(self):
        filename =  tk.filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
        self.__world.Deserialize(filename)

    def New(self):
        Gui = tk.Tk()
        Gui.geometry("200x200")
        sx = tk.StringVar()
        sx.set("<Set width>")
        sy = tk.StringVar()
        sy.set("<Set heigth>")
        self.e = tk.Entry(Gui, textvariable=sx)
        self.e.pack()
        self.c = tk.Entry(Gui, textvariable=sy)
        self.c.pack()
        b1 = tk.Button(Gui, text="Grid", width=10, command = lambda idx = Gui, view = "GridView" : self.newsize(idx, view)).pack()
        b2 = tk.Button(Gui, text="Hex", width=10, command = lambda idx = Gui, view = "HexagonalView" : self.newsize(idx, view)).pack()

    

    def newsize(self, widget, view):
        x = int(self.e.get())
        y = int(self.c.get())
        widget.destroy()
        self.__world.newGame(x, y, view)
