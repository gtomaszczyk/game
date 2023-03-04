import pygame
from Models.Model import *

class LevelViewModel:

    def __init__(self, model: Model, surface):
        self.model = model
        self.surface = surface
        #TODO: zaladowanie obrazka portalu startowego
        #TODO Gabi: zaladowanie obrazkow spadania
        self.walk = [pygame.image.load('Images\\Lemming\\' + imageName) for imageName in ['walk1.png','walk2.png','walk3.png','walk4.png']]
        self.walkOffset = [-1,0]
        #TODO Gabi: stworzyc fallOffset odpowiedni, bedzie identyczny jak walkOffset, ale zeby zachowac konwencje to nalezaloby dodac
        self.walk2 = [pygame.transform.flip(x, True, False) for x in self.walk]

    def render(self):
        for x, column in enumerate(self.model.currentLevel.map):
            for y, value in enumerate(column):
                self.surface.set_at((x, y), (255, 255, 255) if value else (0,0,0))

        #TODO: narysowanie portalu blit'em
        #q: kropka na exit'cie
        self.surface.set_at((self.model.currentLevel.endPosition[0],self.model.currentLevel.endPosition[1]), (255, 255, 255))

        #TODO: to samo co w background service, nie chcemy rysowac lemmingow ktore skonczyly rozgrywke
        #q: zrobione
        lemmingsOnMap=[lem for lem in self.model.currentLevel.lemmings if lem.finished == False]
        for lemming in lemmingsOnMap:
        #for lemming in self.model.currentLevel.lemmings: 
            #TODO Gabi: caly ponizszy kod (linie 24-31) powinnien byc sprawdzany czy lemming jest aktualnie w stanie chodzenia
            if (lemming.direction == LemmingDirection.Right):
                image = self.walk[lemming.actionMoment] # pygame.transform.flip
                self.surface.blit(image, (lemming.position[0] + self.walkOffset[0], lemming.position[1] + self.walkOffset[1]))
                lemming.actionMoment = (lemming.actionMoment + 1) % len(self.walk)
            if (lemming.direction == LemmingDirection.Left):
                image = self.walk2[lemming.actionMoment] # pygame.transform.flip
                self.surface.blit(image, (lemming.position[0] + self.walkOffset[0], lemming.position[1] + self.walkOffset[1]))
                lemming.actionMoment = (lemming.actionMoment + 1) % len(self.walk)
            #TODO Gabi: jesli lemming spada, to animacja wybierz obrazek z animacji spadania i narysuj 