from Models.Lemming import *
import datetime as dt

class Level:
    def __init__(self):
        self.lemmings = [] #pusta tablica - lemmingi tworzone sa w backgroundService w metodzie __updateLevelModel
        self.lastLemmingTime=dt.datetime.now()
        self.LemmingInterval=dt.timedelta(seconds=5)

        with open('Data/level1.txt', 'r') as file: #otwieranie pliku w trybie odczytu - 'r' - read (nie mozna w tym trybie edytowac pliku)
            self.startPosition= [int(el) for el in file.readline().split()]
            self.endPosition=[int(el) for el in file.readline().split()]
            self.allLemmingCount=int(file.readline())
            
            lines = file.readlines()
            tempMap = [[] for x in range(len(lines[0]))]
            for line in lines:
                for y, char in enumerate(line):
                    tempMap[y].append(char == '1')
            self.map = tempMap