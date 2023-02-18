import pygame
from Models.Model import *

class LevelViewModel:

    def __init__(self, model: Model, surface):
        self.model = model
        self.surface = surface
        self.stateImages = {
            LemmingState.Walk: [pygame.image.load('Images\\Lemming\\' + imageName) for imageName in ['walk1.png','walk2.png','walk3.png','walk4.png']],
            LemmingState.Fall: [pygame.image.load(f'Images\\Lemming\\fall{i}.png') for i in range(1,5)]
        }
        self.imageOffsets = {
            LemmingState.Walk: [-1, 0],
            LemmingState.Fall: [-1, 0]
        }

    def render(self):
        for x, column in enumerate(self.model.currentLevel.map):
            for y, value in enumerate(column):
                self.surface.set_at((x, y), (255, 255, 255) if value else (0,0,0))

        for lemming in self.model.currentLevel.lemmings:
            images = self.stateImages[lemming.state]
            image = images[lemming.actionMoment] # pygame.transform.flip
            self.surface.blit(image, (lemming.position[0] + self.imageOffsets[lemming.state][0], lemming.position[1] + self.imageOffsets[lemming.state][1]))
            lemming.actionMoment = (lemming.actionMoment + 1) % len(images)

        
