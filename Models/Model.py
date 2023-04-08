from Models.Level import *

class Model:
    """
    przechowuje wszystkie dane gry
    przechowuje informacje na temat stanu aplikacji - czy aplikacja jest uruchomiona 
    + przetrzymuje scale of the surface
    + tymczasowo tworzy model Level
    """
    def __init__(self):
        self.running = True
        self.scale = 4
        self.currentLevel = Level() # tymczasowo, model nie bedzie tu tworzony
    