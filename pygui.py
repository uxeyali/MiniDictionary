import tkinter as tkr
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
        print(self.df)

    def retrieveword(self, word):
        row = self.df.loc[self.df['Word'] == word]
        # print(row)
        if row is not None:
            word = Word(row["Word"], row["PartOfSpeech"], row["Definition"])
            print()
            print("The word is: ", word.wordName[0])
            print("The meaning of the word is: ", word.definition[0])
            print("And it's part of speech value is: ", word.partOfSpeech[0])
        else:
            print("Error")

    def saveWord(self, word, partOfSpeech, definition):
        row = pd.DataFrame({'Word': [word], 'PartOfSpeech': [partOfSpeech], 'Definition': [definition]})
        self.df = self.df.append(row)
        print(self.df)
        with open("Dictionary.csv", 'w') as f:
            self.df.to_csv(f, header=True)
            

class GUIstuff(tkr.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        
    
    def create_widgets(self):
        self.hi_there = tkr.Button(self)
        self.hi_there["text"] = "Check Definition"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        
        self.quit = tkr.Button(self, text="Exit", fg="red", command=root.destroy)
        self.quit.pack(side="right")
        
        
        self.add = tkr.Entry(root)
        self.add.pack(side = "top")
        
        
        self.save = tkr.Button(self)
        self.save["text"] = "Save"
        dict = Dictionary()
        ##self.save["command"] = dict.saveWord()
        self.save.pack(side="left")
        
        
        
        
        
        
    
       

       
        
    def say_hi(self):
        print("Definition: ")
        


        
        
root = tkr.Tk()
root.geometry("400x300")
app = GUIstuff(master=root)
app.mainloop()
