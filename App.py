import pygame
from Model import *
from Controller import *
from View import *

class App:
    def __init__(self):
        self.model = Model()
        self.controller = Controller(self.model)
        self.view = View(self.model)
    
    def cleanup(self):
        pygame.quit()
 
    def start(self):
        while(self.model.running):
            self.controller.updateModel()
            self.view.render()
        self.cleanup()