from Services.LemmingBaseService import LemmingBaseService
from Models.Lemming import Lemming
from Attributes.LemmingAttributes import *
from Attributes.MapAttributes import *
from Models.Model import *

class LemmingClimberService (LemmingBaseService):
    def __init__(self, model: Model):
        super().__init__(model)

    def _checkSpecialAbilityCondition(self, lemming: Lemming):
        newXEdge = lemming.position[0] + lemming.size[0] if lemming.direction == LemmingDirection.Right else lemming.position[0] - 1
        canMove, _ = self._canLemmingMove(lemming, newXEdge) 
        return not canMove
            

    def _invokeSpecialAbility(self, lemming: Lemming):
        if lemming.actionMoment == 0:
            yTopEdge = lemming.position[1] - 1
            xLeftEdge = lemming.position[0]
            
            allAir = True 
            for x in range(xLeftEdge, xLeftEdge + lemming.size[0]):
                for y in range(yTopEdge - 2, yTopEdge):
                    if self.model.currentLevel.map[x][y] != WallType.Air:
                        allAir = False
            if not allAir:
                lemming.state = LemmingState.Fall
                lemming.direction = LemmingDirection.Right if lemming.direction == LemmingDirection.Left else LemmingDirection.Left
            
            lemming.position[1] -= 2
