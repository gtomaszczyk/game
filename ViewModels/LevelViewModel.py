import pygame
from Attributes.MapAttributes import WallType
from Models.Model import *

class LevelViewModel:
    """
    rysuje obecny model
    ładuje grafikę
    """
    def __init__(self, model: Model, surface: pygame.Surface):
        self.model = model
        self.surface = surface
        self.walk = [pygame.image.load('Images\\Lemming\\' + imageName) for imageName in ['walk1.png','walk2.png','walk3.png','walk4.png']]
        self.walkOffset = [-1,0]
        self.fall = [pygame.image.load('Images\\Lemming\\' + imageName) for imageName in ['fall1.png','fall2.png','fall3.png','fall4.png']]
        self.fallOffset = [0,0]
        self.fallOffset2 = [-2,0]
        self.stop = [pygame.image.load('Images\\Lemming\\' + imageName) for imageName in ['stopper1.png', 'stopper2.png', 'stopper3.png', 'stopper4.png', 'stopper5.png', 'stopper5.png', 'stopper4.png', 'stopper3.png', 'stopper2.png', ]]
        self.stopOffset = [-2,0] #?
        self.dig = [pygame.image.load('Images\\Lemming\\' + imageName) for imageName in ['dig1.png','dig2.png','dig3.png','dig4.png','dig5.png','dig6.png','dig7.png','dig8.png']]
        self.digOffset = [-2, 3]
        self.climb = [pygame.image.load('Images\\Lemming\\' + imageName) for imageName in ['climb1.png','climb2.png','climb3.png','climb4.png','climb5.png','climb6.png','climb7.png','climb8.png']]
        self.walk2 = [pygame.transform.flip(x, True, False) for x in self.walk]
        self.fall2 = [pygame.transform.flip(x, True, False) for x in self.fall]
        self.startportal = pygame.image.load('Images\\start-portal.png')
        self.startportal = pygame.transform.scale(self.startportal, (14, 10))
        self.startportalOffset = [-5, -2]
        self.endportal = pygame.image.load('Images\\end-portal.png')
        self.endportal = pygame.transform.scale(self.endportal, (17, 14))
        self.endportalOffset = [-9, -12]
        self.font = pygame.font.SysFont(None, 14) # inicjalizacja czcionki
        
    def __drawLemmingAbilityButtons(self):
        buttonWidth = 22
        xLemmingAbilityButton = self.surface.get_width() / self.model.scale - buttonWidth
        buttonHeight = 14
        white = (255,255,255)
        red = (255, 0, 0)
        # digger button
        pygame.draw.rect(self.surface, red if self.model.currentLevel.selectedLemmingAbility == LemmingAbility.Digger else white, (xLemmingAbilityButton, 0, buttonWidth, buttonHeight), width= 1)
        self.surface.blit(self.font.render("1", False, white), (xLemmingAbilityButton + 3,2))
        self.surface.blit(self.dig[0], (xLemmingAbilityButton + 12 + self.digOffset[0], 2 + self.digOffset[1]))
        # stopper button
        pygame.draw.rect(self.surface, red if self.model.currentLevel.selectedLemmingAbility == LemmingAbility.Stopper else white, (xLemmingAbilityButton, buttonHeight, buttonWidth, buttonHeight), width= 1)
        self.surface.blit(self.font.render("2", False, white), (xLemmingAbilityButton + 3, buttonHeight + 2))
        # TODO: Gabi, zmienic self.walk na self.stop i self.walkOffset'y na self.stopOffset'y
        self.surface.blit(self.stop[0], (xLemmingAbilityButton + 12 + self.stopOffset[0], buttonHeight + 2 + self.stopOffset[1]))

    def render(self):
        """
        1. rysuje mapę
        2. rysuje portale
        3. rysuje aktywne lemmingi w odpowiednim stanie i kierunku
        """
        for x, column in enumerate(self.model.currentLevel.map):
            for y, value in enumerate(column):
                if value == WallType.Solid or value == WallType.Dirt:
                    self.surface.set_at((x, y), (255, 255, 255))


        self.surface.set_at((self.model.currentLevel.endPosition[0],self.model.currentLevel.endPosition[1]), (255, 255, 255))
        self.surface.blit(self.endportal, (self.model.currentLevel.endPosition[0] + self.endportalOffset[0], self.model.currentLevel.endPosition[1] + self.endportalOffset[1]))

        self.surface.set_at((self.model.currentLevel.startPosition[0],self.model.currentLevel.startPosition[1]), (255, 255, 255))
        self.surface.blit(self.startportal, (self.model.currentLevel.startPosition[0] + self.startportalOffset[0], self.model.currentLevel.startPosition[1] + self.startportalOffset[1]))

        #TODO: to samo co w background service, nie chcemy rysowac lemmingow ktore skonczyly rozgrywke
        #q: zrobione
        lemmingsOnMap=[lem for lem in self.model.currentLevel.lemmings if lem.finished == False]
        for lemming in lemmingsOnMap:
        #for lemming in self.model.currentLevel.lemmings: 
            if (lemming.state == LemmingState.Walk):
                if (lemming.direction == LemmingDirection.Right):
                    image = self.walk[lemming.actionMoment] 
                    self.surface.blit(image, (lemming.position[0] + self.walkOffset[0], lemming.position[1] + self.walkOffset[1]))
                    lemming.actionMoment = (lemming.actionMoment + 1) % len(self.walk)
                if (lemming.direction == LemmingDirection.Left):
                    image = self.walk2[lemming.actionMoment] 
                    self.surface.blit(image, (lemming.position[0] + self.walkOffset[0], lemming.position[1] + self.walkOffset[1]))
                    lemming.actionMoment = (lemming.actionMoment + 1) % len(self.walk) 
            elif (lemming.state == LemmingState.Fall):
                if (lemming.direction == LemmingDirection.Right):
                    image = self.fall[lemming.actionMoment] 
                    self.surface.blit(image, (lemming.position[0] + self.fallOffset[0], lemming.position[1] + self.fallOffset[1]))
                    lemming.actionMoment = (lemming.actionMoment + 1) % len(self.fall)
                if (lemming.direction == LemmingDirection.Left):
                    image = self.fall2[lemming.actionMoment] 
                    self.surface.blit(image, (lemming.position[0] + self.fallOffset2[0], lemming.position[1] + self.fallOffset2[1]))
                    lemming.actionMoment = (lemming.actionMoment + 1) % len(self.fall)
            elif (lemming.state == LemmingState.SpecialAbility):
                if (lemming.ability == LemmingAbility.Stopper):
                    image = self.stop[lemming.actionMoment] 
                    self.surface.blit(image, (lemming.position[0] + self.stopOffset[0], lemming.position[1] + self.stopOffset[1]))
                    lemming.actionMoment = (lemming.actionMoment + 1) % len(self.stop)
                elif (lemming.ability == LemmingAbility.Digger):
                    image = self.dig[lemming.actionMoment] 
                    self.surface.blit(image, (lemming.position[0] + self.digOffset[0], lemming.position[1] + self.digOffset[1]))
                    lemming.actionMoment = (lemming.actionMoment + 1) % len(self.dig)
        self.__drawLemmingAbilityButtons()