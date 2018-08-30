
import pandas as pd

class Word:
    def __init__(self, wordName, partOfSpeech, definition):
        # population array
        self.wordName = wordName
        self.partOfSpeech = partOfSpeech
        self.definition = definition

class Dictionary:
    df = None

    def __init__(self):
        data = pd.read_csv("Dictionary.csv", header=0)
        self.df = pd.DataFrame(data)

    def retrieveword(self, word):
        row = self.df.loc[self.df['Word'] == word]
        # print(row)
        if row is not None:
            word = Word(row["Word"], row["PartOfSpeech"], row["Definition"])
            print()
            print("The word is: ", word.wordName[0])
            print("The meaning of the word is: ", word.definition[0])
            print("And it's part of speech value is: ", word.partOfSpeech[0])

    def saveWord(self, word, partOfSpeech, definition):
        row = pd.DataFrame({'Word': [word], 'PartOfSpeech': [partOfSpeech], 'Definition': [definition]})
        # print(row)
        self.df = self.df.append(row)
        print(self.df)



    # def addWord(self):




dict = Dictionary()
dict.retrieveword("Chicken")
dict.saveWord("Monkey", "Noun", "An animal")