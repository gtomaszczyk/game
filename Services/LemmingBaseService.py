from Attributes.MapAttributes import WallType
from Models.Model import Model
from Attributes.LemmingAttributes import LemmingState,LemmingDirection
from Models.Lemming import Lemming

class LemmingBaseService:
    """
    automatyczna obsługa zdarzeń dla lemminga o domyślnym typie (walk+fall)
    """
    def __init__(self, model: Model):
        self.model = model
        
    def _isPositionAvailable(self, x, y):
        """
        sprawdza czy ruch jest możliwy, dla chodzenia i spadania
        """
        return x >= len(self.model.currentLevel.map) or y >= len(self.model.currentLevel.map[x]) or (self.model.currentLevel.map[x][y] == WallType.Air)
    
    def _isStandingOnGround(self, lemming: Lemming):
        """
        sprawdza czy pod lemmingiem jest podłoga
        """
        lemmingYBottomSide = lemming.position[1] + lemming.size[1] - 1
        for x in range(lemming.position[0], lemming.position[0] + lemming.size[0]):
            if (not self._isPositionAvailable(x, lemmingYBottomSide + 1)):
                return True
        return False
    
    def _updatePosition(self, lemming: Lemming):
        """
        1. jeśli nie ma pod nim podłogi -> spada
        2. jeśli jest pod nim podłoga -> zawsze idzie
        3. przed nim ściana -> zawraca
        4. jeśli dotrze do portalu końcowego -> lemming finished
        """
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
        #testowo finishowanie leminga
        if lemming.position[1] + lemming.size[1] > self.model.currentLevel.endPosition[1] and lemming.position[0] + lemming.size[0] > self.model.currentLevel.endPosition[0]:
            lemming.finished = True
            

        #testowo pokazywanie pozycji leminga
        #print(lemming.position[0],lemming.position[1])
                    
    def _checkSpecialAbilityCondition(self, lemming: Lemming):
        """
        sprawdza ability lemminga
        """
        return False
        
    def _invokeSpecialAbility(self, lemming: Lemming):
        """
        wywołuje ability lemminga
        """
        pass         
    
    def invokeLemmingAction(self, lemming: Lemming):
        """
        w zależności od ability lemminga wywołuje odpowiednią akcję
        """
        if self._checkSpecialAbilityCondition(lemming):
            #lemming.state = LemmingState.SpecialAbility
            self._invokeSpecialAbility(lemming)
        else:
            self._updatePosition(lemming)