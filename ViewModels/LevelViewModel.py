import pygame
from Models.Model import *

class LevelViewModel:

    def __init__(self, model: Model, surface):
        self.model = model
        self.surface = surface
        self.walk = (pygame.image.load('Images\\Lemming\\walk1.png'),
                pygame.image.load('Images\\Lemming\\walk2.png'),
                pygame.image.load('Images\\Lemming\\walk3.png'),
                pygame.image.load('Images\\Lemming\\walk4.png'))

    def render(self):
        for lemming in self.model.currentLevel.lemmings:
            image = pygame.transform.scale(self.walk[lemming.actionMoment], (30,50))
            self.surface.blit(image, lemming.position)
            lemming.actionMoment = (lemming.actionMoment + 1) % len(self.walk)

        
