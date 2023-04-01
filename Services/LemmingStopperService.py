from Services.LemmingBaseService import LemmingBaseService
from Models.Lemming import Lemming
from Attributes.LemmingAttributes import *
from Models.Model import *

class LemmingStopperService (LemmingBaseService):
    def __init__(self, model: Model):
        super().__init__(model)

    def _checkSpecialAbilityCondition(self, lemming: Lemming):
        return lemming.ability == LemmingAbility.Stopper and lemming.state != LemmingState.Fall

    def _invokeSpecialAbility(self, lemming: Lemming):
        pass
                    
        