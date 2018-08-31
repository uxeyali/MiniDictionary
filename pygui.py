import tkinter as tkr
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

            

class GUIstuff(tkr.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("Mini Dictionary")
        self.pack()
        self.create_entry()
        self.create_widgets()

    def create_entry(self):
        self.add = tkr.Entry(root)
        self.add.pack(side="top")


    def create_widgets(self):
        self.quit = tkr.Button(self, text="Exit", fg="red", command=root.destroy)
        self.quit.pack(side="right")

        self.save = tkr.Button(self)
        self.save["text"] = "Save"
        dict = Dictionary()
        ##self.save["command"] = dict.saveWord()
        self.save.pack(side="left")

        self.hi_there = tkr.Button(self)
        self.hi_there["text"] = "Check Definition"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="bottom")

    def say_hi(self):
        print("Definition: ")





root = tkr.Tk()
root.geometry("400x300")
app = GUIstuff(master=root)
app.mainloop()
