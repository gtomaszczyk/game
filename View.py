import pygame
from Model import *

class View:
    def __init__(self, model: Model) -> None:
        pygame.init()
        self.model = model
        self.surface = pygame.display.set_mode((640, 480), pygame.HWSURFACE | pygame.DOUBLEBUF)
        
    def render(self):
        self.surface.fill(0)
        self.surface.set_at((self.model.x, self.model.y), (255, 255, 255))
        pygame.display.update()