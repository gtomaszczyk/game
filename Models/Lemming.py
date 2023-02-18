from Attributes.lemmingFaceDirection import LemmingFaceDirection
from Attributes.lemmingState import LemmingState

class Lemming:

    """
    przechowuje informacje na temat leminga, ale go NIE tworzy!
    """

    def __init__(self):
        self.size = (4,10)
        self.actionMoment = 1 # int, pole okreslajace ktora klatka jest wykorzystywana w danym momencie
        self.position = [5, 11] # tymczasowo, potem zastapimy (x, y)
        self._state = LemmingState.Walk
        self.faceDirection = LemmingFaceDirection.Right
    
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        if (self._state != value):
            self.actionMoment = 1
            self._state = value
        
