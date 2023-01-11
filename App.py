import pygame
from Models.Model import *
from Controller import *
from View import *

class App:
    def __init__(self):
        self.model = Model()
        self.controller = Controller(self.model)
        self.view = View(self.model)
        self.clock = pygame.time.Clock() 
    
    def cleanup(self):
        pygame.quit()
 
    def start(self):
        while(self.model.running):
            self.clock.tick(10)

            self.controller.updateModel()
            self.view.render()
        self.cleanup()