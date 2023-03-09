import pygame
from Models.Model import *

class LevelViewModel:

    def __init__(self, model: Model, surface):
        self.model = model
        self.surface = surface
        #TODO Gabi: zaladowanie obrazkow spadania
        self.walk = [pygame.image.load('Images\\Lemming\\' + imageName) for imageName in ['walk1.png','walk2.png','walk3.png','walk4.png']]
        self.walkOffset = [-1,0]
        self.fall = [pygame.image.load('Images\\Lemming\\' + imageName) for imageName in ['fall1.png','fall2.png','fall3.png','fall4.png']]
        #TODO Gabi: stworzyc fallOffset odpowiedni, bedzie identyczny jak walkOffset, ale zeby zachowac konwencje to nalezaloby dodac
        self.fallOffset = [0,0]
        self.fallOffset2 = [-2,0]
        self.dig = [pygame.image.load('Images\\Lemming\\' + imageName) for imageName in ['dig1.png','dig2.png','dig3.png','dig4.png','dig5.png','dig6.png','dig7.png','dig8.png']]
        self.climb = [pygame.image.load('Images\\Lemming\\' + imageName) for imageName in ['climb1.png','climb2.png','climb3.png','climb4.png','climb5.png','climb6.png','climb7.png','climb8.png']]
        self.walk2 = [pygame.transform.flip(x, True, False) for x in self.walk]
        self.fall2 = [pygame.transform.flip(x, True, False) for x in self.fall]

    def render(self):
        for x, column in enumerate(self.model.currentLevel.map):
            for y, value in enumerate(column):
                self.surface.set_at((x, y), (255, 255, 255) if value else (0,0,0))

        for lemming in self.model.currentLevel.lemmings: 
            #TODO Gabi: caly ponizszy kod (linie 24-31) powinnien byc sprawdzany czy lemming jest aktualnie w stanie chodzenia
            if lemming.state == LemmingState.Walk:
                if (lemming.direction == LemmingDirection.Right):
                    image = self.walk[lemming.actionMoment] 
                    self.surface.blit(image, (lemming.position[0] + self.walkOffset[0], lemming.position[1] + self.walkOffset[1]))
                    lemming.actionMoment = (lemming.actionMoment + 1) % len(self.walk)
                if (lemming.direction == LemmingDirection.Left):
                    image = self.walk2[lemming.actionMoment] 
                    self.surface.blit(image, (lemming.position[0] + self.walkOffset[0], lemming.position[1] + self.walkOffset[1]))
                    lemming.actionMoment = (lemming.actionMoment + 1) % len(self.walk)
            #TODO Gabi: jesli lemming spada, to animacja wybierz obrazek z animacji spadania i narysuj 
            elif lemming.state == LemmingState.Fall:
                if (lemming.direction == LemmingDirection.Right):
                    image = self.fall[lemming.actionMoment] 
                    self.surface.blit(image, (lemming.position[0] + self.fallOffset[0], lemming.position[1] + self.fallOffset[1]))
                    lemming.actionMoment = (lemming.actionMoment + 1) % len(self.fall)
                if (lemming.direction == LemmingDirection.Left):
                    image = self.fall2[lemming.actionMoment] 
                    self.surface.blit(image, (lemming.position[0] + self.fallOffset2[0], lemming.position[1] + self.fallOffset2[1]))
                    lemming.actionMoment = (lemming.actionMoment + 1) % len(self.fall)