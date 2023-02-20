from Models.Lemming import *

class Level:
    """
    zawiera liste lemmingow
    """
    def __init__(self):
        self.lemmings = [Lemming()] #TODO: self.lemmings = [] - lemmingi beda tworzone w background service
        #TODO: czas pojawienia sie ostatniego lemminga jako datetime - zajecia numer 8
        #TODO: timedelta jako ilosc czasu ktora musi minac miedzy ostatnim lemmingiem a nowym - zajecia numer 8
        with open('Data/level1.txt', 'r') as file: #otwieranie pliku i przetwarzanie przerzucic do klasy obslugi plikow, docelowo self.map = map
            #TODO: zaczytanie pierwszej linii, pozycja startowa portalu (file.readline()), przypisanie do self.startPosition
            #TODO: druga linia, pozycja portalu koncowego, przypisanie do self.endPosition
            #TODO: trzecia linia, ilosc lemmingow, self.allLemmingCount
            lines = file.readlines()
            tempMap = [[] for x in range(len(lines[0]))]
            for line in lines:
                for y, char in enumerate(line):
                    tempMap[y].append(char == '1')
            self.map = tempMap