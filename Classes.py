import pandas as pd

class Word:
    def __init__(self, wordName, partOfSpeech, definition):
        # population array
        self.wordName = wordName
        self.partOfSpeech = partOfSpeech
        self.definition = definition

class Dictionary:
    def __init__(self):
        data = pd.read_csv("Dictionary.csv", header=0)
        df = pd.DataFrame(data)

    def addWord(self, word):


    def retrieveWord(self, word):

    def saveWord(self, word):