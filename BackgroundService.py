from Attributes.lemmingFaceDirection import LemmingFaceDirection
from Models.Model import Model
from Attributes.lemmingState import LemmingState
from Models.Lemming import Lemming

class BackgroundService:

    def __init__(self, model: Model):
        self.model = model
        
    def __isPositionAvailable(self, x, y):
        return x >= len(self.model.currentLevel.map) or y >= len(self.model.currentLevel.map[x]) or not self.model.currentLevel.map[x][y]
    
    def __availableYSpaceAboveGround(self, lemming: Lemming): #maksymalny dystans do ziemi jaki chcemy mierzyć to 3, w jednej klatce nie spadnie więcej niż 3 pozycje w dół
        availableYSpace = 3
        for x in range(lemming.position[0], lemming.position[0] + lemming.size[0]):
            lemmingYBottomSide = lemming.position[1] + lemming.size[1] - 1
            if (not self.__isPositionAvailable(x, lemmingYBottomSide + 1)):
                availableYSpace = min(availableYSpace, 0)
            if (not self.__isPositionAvailable(x, lemmingYBottomSide + 2)):
                availableYSpace = min(availableYSpace, 1)
            if (not self.__isPositionAvailable(x, lemmingYBottomSide + 3)):
                availableYSpace = min(availableYSpace, 2)
        return availableYSpace
    
    def __tryWalk(self, lemming: Lemming):
        if (lemming.state != LemmingState.Walk):
            return
        if (lemming.faceDirection == LemmingFaceDirection.Right):
            newRightXEdge = lemming.position[0] + lemming.size[0]
            if (self.__isPositionAvailable(newRightXEdge, lemming.position[1])): #nie ma ściany
                lemming.position[0] = lemming.position[0] + 1
            else:
                lemming.faceDirection = LemmingFaceDirection.Left
        if (lemming.faceDirection == LemmingFaceDirection.Left):
            newLeftXEdge  = lemming.position[0] - 1
            if (self.__isPositionAvailable(newLeftXEdge, lemming.position[1])):
                lemming.position[0] = lemming.position[0] - 1
            else:
                lemming.faceDirection = LemmingFaceDirection.Right
    
    def __tryFall(self, lemming: Lemming):
        availableYSpace = self.__availableYSpaceAboveGround(lemming)
        if (availableYSpace > 0):
            lemming.state = LemmingState.Fall
            lemming.position[1] += availableYSpace
        if (self.__availableYSpaceAboveGround(lemming) == 0):
            lemming.state = LemmingState.Walk

    def __updateLevelModel(self):
        for lemming in self.model.currentLevel.lemmings:
            self.__tryWalk(lemming)
            self.__tryFall(lemming)
    
    def updateModel(self):
        self.__updateLevelModel()

