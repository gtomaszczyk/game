from Services.LemmingBaseService import LemmingBaseService
from Models.Lemming import Lemming
from Attributes.LemmingAttributes import *
from Attributes.MapAttributes import *
from Models.Model import *

class LemmingStopperService (LemmingBaseService):
    def __init__(self, model: Model):
        super().__init__(model)

    def _checkSpecialAbilityCondition(self, lemming: Lemming):
        return lemming.ability == LemmingAbility.Stopper and lemming.state != LemmingState.Fall

    def _invokeSpecialAbility(self, lemming: Lemming):
        if self.model.currentLevel.map[lemming.position[0]][lemming.position[1]]!=WallType.Stopper:
            for i in range(lemming.size[0]):
                for j in range(lemming.size[1]):
                    self.model.currentLevel.map[lemming.position[0]+i][lemming.position[1]+j]=WallType.Stopper

                    
        