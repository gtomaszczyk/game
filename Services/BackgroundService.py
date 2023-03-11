from Models.Model import Model
from Attributes.LemmingAttributes import LemmingState,LemmingDirection
from Models.Lemming import Lemming
from Services.LemmingBaseService import LemmingBaseService
import datetime as dt

class BackgroundService:

    def __init__(self, model: Model):
        self.model = model
        self.lemmingBaseService = LemmingBaseService(self.model)

    def __updateLevelModel(self):
        #TODO: jesli uplynal czas timedelta od czasu stworzenia ostatniego lemminga i ilosc lemmingow w tablicy jest mniejsza niz allLemmingCount to utworz lemminga nowego i zaktualizuj czas stworzenia ostatniego lemminga = datetime.now()
        if self.model.currentLevel.lastLemmingTime < dt.datetime.now()-self.model.currentLevel.LemmingInterval and len(self.model.currentLevel.lemmings)<self.model.currentLevel.allLemmingCount:
            #create new lemming
            self.model.currentLevel.lemmings.append(Lemming([x for x in self.model.currentLevel.startPosition]))
            self.model.currentLevel.lastLemmingTime=dt.datetime.now()
            print(str(self.model.currentLevel.lastLemmingTime))
        
        #lista = [a**2 for a in range(10) if a%2 == 0]
        lemmingsOnMap=[lem for lem in self.model.currentLevel.lemmings if lem.finished == False]
        for lemming in lemmingsOnMap:
        #for lemming in self.model.currentLevel.lemmings: #TODO: petla powinna isc tylko po lemmingach ktore maja finished == False; nie chcemy aktualizowac pozycji lemmingow ktore zakonczyly rozgrywke 
            self.lemmingBaseService.invokeLemmingAction(lemming)
        
        
    
    def updateModel(self):
        self.__updateLevelModel()