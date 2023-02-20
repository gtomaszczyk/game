from Models.Model import Model
from Attributes.LemmingAttributes import LemmingState,LemmingDirection
from Models.Lemming import Lemming

class LemmingBaseService:
    
    def __init__(self, model: Model):
        self.model = model
        
    def _isPositionAvailable(self, x, y):
        return x >= len(self.model.currentLevel.map) or y >= len(self.model.currentLevel.map[x]) or not self.model.currentLevel.map[x][y]
    
    def _isStandingOnGround(self, lemming: Lemming):
        lemmingYBottomSide = lemming.position[1] + lemming.size[1] - 1
        for x in range(lemming.position[0], lemming.position[0] + lemming.size[0]):
            if (not self._isPositionAvailable(x, lemmingYBottomSide + 1)):
                return True
        return False
    
    def _updatePosition(self, lemming: Lemming):
        if not self._isStandingOnGround(lemming):
            lemming.state = LemmingState.Fall
            lemming.position[1] = lemming.position[1] + 1
        else: 
            lemming.state = LemmingState.Walk
            if (lemming.direction == LemmingDirection.Right):
                newRightXEdge = lemming.position[0] + lemming.size[0]
                if self._isPositionAvailable(newRightXEdge, lemming.position[1]):
                    lemming.position[0] = lemming.position[0] + 1
                else:
                    lemming.direction = LemmingDirection.Left 
            elif (lemming.direction == LemmingDirection.Left):
                newLeftXEdge  = lemming.position[0] - 1
                if self._isPositionAvailable(newLeftXEdge, lemming.position[1]):
                    lemming.position[0] = lemming.position[0] - 1
                else:
                    lemming.direction = LemmingDirection.Right
                    
    def _checkSpecialAbilityCondition(self, lemming: Lemming):
        return False
        
    def _invokeSpecialAbility(self, lemming: Lemming):
        pass         
    
    def invokeLemmingAction(self, lemming: Lemming):
        if self._checkSpecialAbilityCondition(lemming):
            lemming.state = LemmingState.SpecialAbility
            self._invokeSpecialAbility(lemming)
        else:
            self._updatePosition(lemming)
            

        
    

