from Models.Model import Model
from Attributes.LemmingAttributes import LemmingState,LemmingDirection
from Models.Lemming import Lemming
from Services.LemmingBaseService import LemmingBaseService

class BackgroundService:

    def __init__(self, model: Model):
        self.model = model
        self.lemmingBaseService = LemmingBaseService(self.model)

    def __updateLevelModel(self):
        #TODO: jesli uplynal czas timedelta od czasu stworzenia ostatniego lemminga i ilosc lemmingow w tablicy jest mniejsza niz allLemmingCount to utworz lemminga nowego i zaktualizuj czas stworzenia ostatniego lemminga = datetime.now()
        for lemming in self.model.currentLevel.lemmings: #TODO: petla powinna isc tylko po lemmingach ktore maja finished == False; nie chcemy aktualizowac pozycji lemmingow ktore zakonczyly rozgrywke 
            self.lemmingBaseService.invokeLemmingAction(lemming)
    
    def updateModel(self):
        self.__updateLevelModel()
    

