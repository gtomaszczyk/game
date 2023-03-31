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
        if event.type == pygame.MOUSEBUTTONDOWN:
            #print("klik",pygame.mouse.get_pos())
            print("mouse klik",round(pygame.mouse.get_pos()[0]/self.model.scale),round(pygame.mouse.get_pos()[1]/self.model.scale))
            mx=round(pygame.mouse.get_pos()[0]/self.model.scale)
            my=round(pygame.mouse.get_pos()[1]/self.model.scale)
            #print("lemming",self.model.currentLevel.lemmings[0].position[0],self.model.currentLevel.lemmings[0].position[1])
            for i in range(len(self.model.currentLevel.lemmings)):
                lemX=self.model.currentLevel.lemmings[i].position[0]
                lemY=self.model.currentLevel.lemmings[i].position[1]
                lemsize=self.model.currentLevel.lemmings[i].size
                
                print("lem",i,lemX,lemY)
                if mx>=lemX and mx <=lemX+lemsize[0] and my >=lemY and my <= lemY+lemsize[1]:
                    print("!!! click lemming :",i)
                    self.model.currentLevel.lemmings[i].state=LemmingState.SpecialAbility
                    #self.model.currentLevel.lemmings[i].ability=LemmingAbility.Stopper
        
           
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
        
    
    