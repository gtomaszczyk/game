from Models.Model import *
from pygame.event import Event
import pygame

class Controller:
    """
    na podstawie wydarzeń użytkownika (funkcje __processEvent(event) i __processKeys()) aktualizuje model (funkcja upadateModel)
    """
    __slots__ = ['model']
    
    def __init__(self, model: Model):
        self.model = model
        
    def __processEvent(self, event: Event):  
        """
        1. sprawdza czy został wykonany event wyjścia (quit) -> jeśli tak, strąca pierwsze domino żeby aplikacja się zamknęła 
        2. TODO
        """
        if event.type == pygame.QUIT:
            self.model.running = False
        #if event.type == pygame.KEYDOWN:
        
           
    def __processKeys(self):
        """
        sprawdza jakie klawisze zostały naciśnięte
        """
        keys = pygame.key.get_pressed()
        '''
        if keys[pygame.K_LEFT]:
            self.model.x -= 1
        if keys[pygame.K_RIGHT]:
            self.model.x += 1
        '''
    
         
    def updateModel(self):
        """
        aktualizuje model na podstawie zdarzeń
        """
        for event in pygame.event.get():
            self.__processEvent(event)
        self.__processKeys()
        
    
    