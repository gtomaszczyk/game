from Models.Model import Model
from Attributes.LemmingAttributes import LemmingState,LemmingDirection
from Models.Lemming import Lemming
from Services.LemmingBaseService import LemmingBaseService
import datetime as dt

class BackgroundService:
    """
    spawnuje lemmingi sprawdza czy lemming jest w grze czy już skończył
    """
    def __init__(self, model: Model):
        self.model = model
        self.lemmingBaseService = LemmingBaseService(self.model)

    def __createNewLemming(self):
        self.model.currentLevel.lemmings.append(Lemming([x for x in self.model.currentLevel.startPosition]))


    def __updateLevelModel(self):
        if self.model.currentLevel.lastLemmingTime < dt.datetime.now()-self.model.currentLevel.LemmingInterval and len(self.model.currentLevel.lemmings)<self.model.currentLevel.allLemmingCount:
            self.__createNewLemming()
            self.model.currentLevel.lastLemmingTime=dt.datetime.now()
            
        
        lemmingsOnMap=[lem for lem in self.model.currentLevel.lemmings if lem.finished == False]
        for lemming in lemmingsOnMap:
        #for lemming in self.model.currentLevel.lemmings: #TODO: petla powinna isc tylko po lemmingach ktore maja finished == False; nie chcemy aktualizowac pozycji lemmingow ktore zakonczyly rozgrywke 
            self.lemmingBaseService.invokeLemmingAction(lemming)
        
        
    
    def updateModel(self):
        self.__updateLevelModel()