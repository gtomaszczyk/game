from Models.Level import *

class Model:
    
    def __init__(self):
        self.running = True
        self.scale = 5
        self.currentLevel = Level() # tymczasowo, model nie bedzie tu tworzony
    