import pygame
from Models.Model import *
import ViewModels.LevelViewModel as lvm

class View:
    """
    - rysuje aktualny model, tworzy warstwę wizualną aplikacji (na podstawie modelu decyduje, który View Model jest rysowany) (self.model, self.surface + funkcja render)
    - tworzy View Modele (wszystkie)(funkcja __init__, self.levelviewmodel = lvm.LevelViewModel(self.model, self.unscaledSurface)), ale rysuje tylko jeden (na razie tylko jeden view model, ale beda wszystkie)
    """
    def __init__(self, model: Model):
        pygame.init()
        self.model = model # w przyszlosci informacje na temat wybranego widoku
        self.surface = pygame.display.set_mode((640, 480), pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.unscaledSurface = self.surface.copy()
        self.levelviewmodel = lvm.LevelViewModel(self.model, self.unscaledSurface) # na razie tylko jeden view model, ale beda wszystkie
        
    def render(self):
        """
        rysuje aktualny model
        1) wypełnia powierzchnię czarnym kolorem
        2) rysuje level na podstawie informacji zawartych w klasie Level
        3) powiększanie narysowanej powierzchni
        4) wyświetlenie narysowanej powierzchni
        *5) odsłonięcie kurtyny :)
        """
        self.unscaledSurface.fill(0)
        self.levelviewmodel.render()
        scaledSurface = pygame.transform.scale(self.unscaledSurface, (self.unscaledSurface.get_width() * self.model.scale, self.unscaledSurface.get_height() * self.model.scale))
        self.surface.blit(scaledSurface, (0,0))
        pygame.display.update()