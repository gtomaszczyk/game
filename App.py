import pygame
from Models.Model import *
from Controller import *
from View import *
from Services.BackgroundService import BackgroundService

class App:
    """
    dowodzi, wszystko tworzy
    """
    def __init__(self):
        self.model = Model()
        self.backgroundService = BackgroundService(self.model)
        self.controller = Controller(self.model)
        self.view = View(self.model)
        self.clock = pygame.time.Clock()
        
    def cleanup(self):
        """
        pozbywa się zasobów przed wyłączeniem gry
        """
        pygame.quit()
 
    def start(self):
        """
        nieskończona pętla generująca kolejne klatki aplikacji
        """
        while(self.model.running):
            self.clock.tick(10)
            self.backgroundService.updateModel()
            self.controller.updateModel()
            self.view.render()
        self.cleanup()