
import pandas as pd


class Dictionary:
    df = None
    wordName = None
    partOfSpeech = None
    definition = None

    def __init__(self):
        data = pd.read_csv("Dictionary.csv", header=0)
        self.df = pd.DataFrame(data)
        print(self.df)

    def retrieveword(self, word):
        row = self.df.loc[self.df['Word'] == word]
        if row.empty is False:
            wordName = row['Word'].to_string(index=False)
            definition = row["Definition"].to_string(index=False)
            partOfSpeech = row["PartOfSpeech"].to_string(index=False)
            print()
            print("The word is: ", wordName)
            print("The meaning of the word is: ", definition)
            print("And it's part of speech value is: ", partOfSpeech)
        else:
            print()
            print("Error: Word does not exist")

    def saveWord(self, word, partOfSpeech, definition):
        row = self.df.loc[self.df['Word'] == word]
        if row.empty is True:
            row = pd.DataFrame({'Word': [word], 'PartOfSpeech': [partOfSpeech], 'Definition': [definition]})
            self.df = self.df.append(row, sort = False)
            print(self.df)
            with open("Dictionary.csv", 'w') as f:
                self.df.to_csv(f, header=True, index=False)
        else:
            print()
            print("Error: Word already exists")




dict = Dictionary()
dict.retrieveword("Chicken")
# dict.saveWord("Monkey", "Noun", "An animal")

dict.retrieveword("Monkey")
# dict.saveWord("Book","Noun", "Something to read")
dict.retrieveword("Book")

dict.saveWord("Book","Noun", "Something to read")
dict.retrieveword("Poop")
