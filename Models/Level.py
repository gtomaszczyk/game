from Models.Lemming import *
import datetime as dt

class Level:
    """
    zawiera liste lemmingow
    """
    def __init__(self):
        self.lemmings = [Lemming()] #TODO: self.lemmings = [] - lemmingi beda tworzone w background service
        #TODO: czas pojawienia sie ostatniego lemminga jako datetime - zajecia numer 8
        self.lastLemmingTime=dt.datetime.now()
        #TODO: timedelta jako ilosc czasu ktora musi minac miedzy ostatnim lemmingiem a nowym - zajecia numer 8
        LemmingInterval=dt.timedelta(seconds=1)
        # poniższe pójdzie do Background
        #if self.lastLemmingTime+LemmingInterval > dt.datetime.now():
        #    #create new lemming
        #    self.lastLemmingTime=dt.datetime.now()
        #    print(str(self.lastLemmingTime))

        with open('Data/level1.txt', 'r') as file: #otwieranie pliku i przetwarzanie przerzucic do klasy obslugi plikow, docelowo self.map = map
            #TODO: zaczytanie pierwszej linii, pozycja startowa portalu (file.readline()), przypisanie do self.startPosition
            self.startPosition=file.readline().split()
            #TODO: druga linia, pozycja portalu koncowego, przypisanie do self.endPosition
            self.endPosition=file.readline().split()
            #TODO: trzecia linia, ilosc lemmingow, self.allLemmingCount
            self.allLemminCount=file.readline()
            lines = file.readlines()
            tempMap = [[] for x in range(len(lines[0]))]
            for line in lines:
                for y, char in enumerate(line):
                    tempMap[y].append(char == '1')
            self.map = tempMap