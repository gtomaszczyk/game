from Models.Model import *
from pygame.event import Event
import pygame

class Controller:
    __slots__ = ['x' , 'y', 'model']
    
    def __init__(self, model: Model):
        self.model = model
        
    def __processEvent(self, event: Event):  
        if event.type == pygame.QUIT:
            self.model.running = False
        #if event.type == pygame.KEYDOWN:
        
            
    def __processKeys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.model.y -= 1
        if keys[pygame.K_DOWN]:
            self.model.y += 1
        if keys[pygame.K_LEFT]:
            self.model.x -= 1
        if keys[pygame.K_RIGHT]:
            self.model.x += 1
         
    def updateModel(self):
        for event in pygame.event.get():
            self.__processEvent(event)
        self.__processKeys()
        
    
    