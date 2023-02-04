from Models.Lemming import *

class Level:
    """
    zawiera liste lemmingow
    """
    def __init__(self):
        self.lemmings = [Lemming()] # 1 leming tymczasowo, tu nie beda tworzone lemingi!

        with open('Data/level1.txt', 'r') as file: #otwieranie pliku i przetwarzanie przerzucic do klasy obslugi plikow, docelowo self.map = map
            lines = file.readlines()
            tempMap = [[] for x in range(len(lines[0]))]
            for line in lines:
                for y, char in enumerate(line):
                    tempMap[y].append(char == '1')
            self.map = tempMap