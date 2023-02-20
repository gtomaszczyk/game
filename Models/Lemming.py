from Attributes.LemmingAttributes import LemmingDirection, LemmingState

class Lemming:

    """
    przechowuje informacje na temat leminga, ale go NIE tworzy!
    """

    def __init__(self): #TODO: przy tworzeniu lemminga zawsze powinnismy podawac jego pozycje startową x i y
        self.size = (4,10)
        self.actionMoment = 1 # int, pole okreslajace ktora klatka jest wykorzystywana w danym momencie
        self.position = [5, 11] #TODO: zastapic x i y
        self.state = LemmingState.Walk
        self.direction = LemmingDirection.Right
        
