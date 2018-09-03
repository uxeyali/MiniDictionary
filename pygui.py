import tkinter as tkr
import pandas as pd
from tkinter import messagebox
from tkinter import Label

class Dictionary:
    df = None
    wordName = None
    partOfSpeech = None
    definition = None

    def __init__(self):
        data = pd.read_csv("Dictionary.csv", header=0)
        self.df = pd.DataFrame(data)
        # print(self.df)

    def retrieveword(self, word):
        row = self.df.loc[self.df['Word'] == word]
        if row.empty is False:
            wordName = row['Word'].to_string(index=False)
            definition = row["Definition"].to_string(index=False)
            partOfSpeech = row["PartOfSpeech"].to_string(index=False)
            lines = ["Word: wordName", wordName,"", 'Definition: ', definition,"", "Part of speech: ", partOfSpeech]
            messagebox.showinfo(wordName, "\n".join(lines))
            # print()
            # print("The word is: ", wordName)
            # print("The meaning of the word is: ", definition)
            # print("And it's part of speech value is: ", partOfSpeech)
        else:
            # print()
            messagebox.showinfo("Error", "Error: Word does not exist")

    def saveWord(self, word, partOfSpeech, definition):
        row = self.df.loc[self.df['Word'] == word]
        if row.empty is True:
            row = pd.DataFrame({'Word': [word], 'PartOfSpeech': [partOfSpeech], 'Definition': [definition]})
            self.df = self.df.append(row, sort = False)
            # print(self.df)
            with open("Dictionary.csv", 'w') as f:
                self.df.to_csv(f, header=True, index=False)
                messagebox.showinfo("Added","Word added to dictionary.")
        else:
            # print()
            messagebox.showinfo("Error", "Word already exists in the dictionary")

#
class GUIstuff(tkr.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()


    def create_widgets(self):
        dict = Dictionary()

        # Retrieve
        self.retrieve = tkr.Entry(root)
        self.retrieve.insert(0, "Type in the word you want to add")
        self.retrieve.pack(side="right", fill='x', expand=True, padx=50, pady=4)

        # Exit button
        self.quit = tkr.Button(self, text="Exit", fg="red", command=root.destroy)
        self.quit.pack(side="right", fill='both', expand=True, padx=4, pady=4)

        # Add button
        self.add = tkr.Button(self)
        self.add["text"] = "Add"
        self.add.pack(side="right", fill='both', expand=True, padx=4, pady=4)
        self.add["command"] = self.hide_main

        # Check definition
        self.check = tkr.Button(self)
        self.check["text"] = "Check Definition"
        self.check.pack(side="bottom", fill='both', expand=True, padx=4, pady=4)
        self.check["command"] = lambda: dict.retrieveword(self.retrieve.get())

    def hide_main(self):
        self.retrieve.forget()
        self.add.pack_forget()
        self.check.pack_forget()
        self.quit.pack_forget()
        self.add_word()

    def hide_add(self):
        # Save button
        self.save.pack_forget()
        self.word.forget()
        self.pos.forget()
        self.defi.forget()
        self.back.pack_forget()
        # Exit
        self.quit.pack_forget()
        self.create_widgets()


    def add_word(self):

        dict = Dictionary()

        # Exit button
        self.quit = tkr.Button(self, text="Exit", fg="red", command=root.destroy)
        self.quit.pack(side="right", fill='both', expand=True, padx=4, pady=4)

        # Save button
        self.save = tkr.Button(self)
        self.save["text"] = "Save"
        self.save["command"] = lambda: self.dict.saveWord(self.word.get(), self.pos.get(), self.defi.get())
        self.save.pack(side="right", fill='x', expand=True, padx=50, pady=4)

        # Back button
        self.back = tkr.Button(self)
        self.back["text"] = "Back"
        self.back["command"] = lambda: self.hide_add()
        self.back.pack(side="right", fill='x', expand=True, padx=50, pady=4)

        # Word
        self.word = tkr.Entry(root)
        self.word.insert(0, "Type in the word you want to add")
        self.word.pack(side="top", fill='x', expand=True, padx=50, pady=2)

        # PoS
        self.pos = tkr.Entry(root)
        self.pos.insert(0, "Type the part of speech")
        self.pos.place(x=150, y=150, width=100, height=25)
        self.pos.pack(side="top", fill='x', expand=True, padx=50, pady=2)

        # Definition
        self.defi = tkr.Entry(root)
        self.defi.insert(0, "Type the defintion")
        self.defi.place(x=150, y=200, width=100, height=25)
        self.defi.pack(side="top", fill='x', expand=True, padx=50, pady=2)



root = tkr.Tk()
root.geometry("400x300")
app = GUIstuff(master=root)
app.mainloop()