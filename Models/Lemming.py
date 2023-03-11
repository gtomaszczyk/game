from Attributes.LemmingAttributes import LemmingDirection, LemmingState


class Lemming:
    def __init__(self,pos): #pos - pozycja początkowa (x,y)
        self.size = (4,10)
        self.actionMoment = 1 # int, pole okreslajace ktora klatka jest wykorzystywana w danym momencie
        self.finished = False
        self.position = pos
        self.state = LemmingState.Walk
        self.direction = LemmingDirection.Right

   