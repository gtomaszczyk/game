class Lemming:

    """
    przechowuje informacje na temat leminga, ale go NIE tworzy!
    """

    def __init__(self):
        self.actionMoment = 1 # int, pole okreslajace ktora klatka jest wykorzystywana w danym momencie
        self.position = (100, 100) # tymczasowo, potem zastapimy (x, y)
