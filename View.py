import pygame
from Models.Model import *
import ViewModels.LevelViewModel as lvm

class View:
    def __init__(self, model: Model):
        pygame.init()
        self.model = model # w przyszlosci informacje na temat wybranego widoku
        self.surface = pygame.display.set_mode((640, 480), pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.levelviewmodel = lvm.LevelViewModel(self.model, self.surface) # na razie tylko jeden view model, ale beda wszystkie
        
    def render(self):
        self.surface.fill(0)
        self.levelviewmodel.render()
        pygame.display.update()