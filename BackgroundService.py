from Models.Model import Model
from Attributes.lemmingState import LemmingState
from Models.Lemming import Lemming

class BackgroundService:

    def __init__(self, model: Model):
        self.model = model
    
    def __tryUpdateLemmingPosition(self, lemming: Lemming):
        if (lemming.state == LemmingState.WalkRight):
            newRightXEdge = lemming.position[0] + lemming.size[0]
            if (self.model.currentLevel.map[newRightXEdge][lemming.position[1]] == False): #nie ma ściany
                lemming.position[0] = lemming.position[0] + 1
            else:
                lemming.state = LemmingState.WalkLeft
        if (lemming.state == LemmingState.WalkLeft):
            newLeftXEdge  = lemming.position[0] - 1
            if (self.model.currentLevel.map[newLeftXEdge][lemming.position[1]] == False):
                lemming.position[0] = lemming.position[0] - 1
            else:
                lemming.state = LemmingState.WalkRight

    def __updateLevelModel(self):
        for lemming in self.model.currentLevel.lemmings:
            self.__tryUpdateLemmingPosition(lemming)
    
    def updateModel(self):
        self.__updateLevelModel()

