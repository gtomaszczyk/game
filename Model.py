class Model:
    __slots__ = ['x' , 'y', 'running']
    
    def __init__(self) -> None:
        self.x, self.y = 100, 100
        self.running = True
    