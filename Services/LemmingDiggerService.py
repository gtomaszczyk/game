from Services.LemmingBaseService import LemmingBaseService
from Models.Lemming import Lemming
from Attributes.LemmingAttributes import *
from Attributes.MapAttributes import *
from Models.Model import *

class LemmingDiggerService (LemmingBaseService):
    def __init__(self, model: Model):
        super().__init__(model)

    def _checkSpecialAbilityCondition(self, lemming: Lemming):
        if (lemming.state == LemmingState.SpecialAbility):
            return True
        yDigEdge = lemming.position[1] + lemming.size[1] 
        map = self.model.currentLevel.map
        lemming.state != LemmingState.Fall 
        for i in range(lemming.size[0]):
            if map[lemming.position[0] + i][yDigEdge] == WallType.Dirt:
                return True
        return False 
    
    def _invokeSpecialAbility(self, lemming: Lemming):
        if lemming.actionMoment == 0:
            yDigEdge = lemming.position[1] + lemming.size[1]
            xDigLeftEdge = lemming.position[0] - 1
            digWidth = lemming.size[0] + 2 
            map = self.model.currentLevel.map
            allAir = True 
            for i in range(digWidth):
                if map[xDigLeftEdge + i][yDigEdge] != WallType.Air:
                    allAir = False
            if allAir:
                lemming.ability = LemmingAbility.Walker
            else:    
                for i in range(digWidth):
                    map[xDigLeftEdge + i][yDigEdge] = WallType.Air
                lemming.position[1] = lemming.position[1] + 1