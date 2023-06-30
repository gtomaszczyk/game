from Models.Model import Model
from Attributes.LemmingAttributes import *
from Models.Lemming import Lemming
from Services.LemmingBaseService import LemmingBaseService
from Services.LemmingStopperService import LemmingStopperService
from Services.LemmingDiggerService import LemmingDiggerService
import datetime as dt

class BackgroundService:
    """
    automatyczna obsługa zdarzeń (użytkownik nie ma wpływu), np. chodzenie lemminga
    """
    def __init__(self, model: Model):
        self.model = model
        self.lemmingBaseService = LemmingBaseService(self.model)
        self.lemmingStopperService = LemmingStopperService(self.model)
        self.lemmingDiggerService = LemmingDiggerService(self.model)

    def __createNewLemming(self):
        """
        tworzymy lemminga w portalu początkowym 
        """
        self.model.currentLevel.lemmings.append(Lemming([x for x in self.model.currentLevel.startPosition]))


    def __updateLevelModel(self):
        """
        1. tworzy kolejne lemmingi po upływie zadanego czasu
        2. automatyczna obsługa zdarzeń dla każdego aktywnego (widocznego) lemminga
        """
        if self.model.currentLevel.lastLemmingTime < dt.datetime.now()-self.model.currentLevel.LemmingInterval and len(self.model.currentLevel.lemmings)<self.model.currentLevel.allLemmingCount:
            self.__createNewLemming()
            self.model.currentLevel.lastLemmingTime=dt.datetime.now()
            
        
        lemmingsOnMap=[lem for lem in self.model.currentLevel.lemmings if lem.finished == False]
        for lemming in lemmingsOnMap:
        #for lemming in self.model.currentLevel.lemmings: #TODO: petla powinna isc tylko po lemmingach ktore maja finished == False; nie chcemy aktualizowac pozycji lemmingow ktore zakonczyly rozgrywke 
            if lemming.ability == LemmingAbility.Walker:
                self.lemmingBaseService.invokeLemmingAction(lemming)
            elif lemming.ability == LemmingAbility.Stopper:
                self.lemmingStopperService.invokeLemmingAction(lemming)
            elif lemming.ability == LemmingAbility.Digger:
                self.lemmingDiggerService.invokeLemmingAction(lemming)
        
        
    
    def updateModel(self):
        self.__updateLevelModel()