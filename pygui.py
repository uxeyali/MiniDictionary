
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

    def retrieveword(self, word):
        row = self.df.loc[self.df['Word'] == word]
        if row.empty is False:
            wordName = row['Word'].to_string(index=False)
            definition = row["Definition"].to_string(index=False)
            partOfSpeech = row["PartOfSpeech"].to_string(index=False)
            lines = ["Word: wordName", wordName,"", 'Definition: ', definition,"", "Part of speech: ", partOfSpeech]
            messagebox.showinfo(wordName, "\n".join(lines))
        else:
            messagebox.showinfo("Error", "Error: Word does not exist")

    def saveWord(self, word, partOfSpeech, definition):
        row = self.df.loc[self.df['Word'] == word]
        if row.empty is True:
            row = pd.DataFrame({'Word': [word], 'PartOfSpeech': [partOfSpeech], 'Definition': [definition]})
            self.df = self.df.append(row, sorted = False)
            with open("Dictionary.csv", 'w') as f:
                self.df.to_csv(f, header=True, index=False)
                messagebox.showinfo("Added","Word added to dictionary.")
        else:
            messagebox.showinfo("Error", "Word already exists in the dictionary")

#
class GUIstuff(tkr.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        dict = Dictionary()

        self.winfo_toplevel().title("Mini Dictionary")

        self.labelText = tkr.StringVar()
        self.labelText.set("Retrieve word:")
        self.labelDir = Label(root, textvariable=self.labelText, height=0)
        self.labelDir.pack(side="top")

        # Retrieve
        self.retrieve = tkr.Entry(root)
        self.retrieve.insert(0, "Type in the word you want to add")
        self.retrieve.pack(side="top", fill='x', padx=30)

        # Check definition
        self.check = tkr.Button(root)
        self.check["text"] = "Definition"
        self.check.pack(side="top", padx=10, pady=20)
        self.check["command"] = lambda: dict.retrieveword(self.retrieve.get())


        # Exit button
        self.quit = tkr.Button(self, text="Exit", fg="red", command=root.destroy)
        self.quit.pack(side="right", expand=True, padx=4, pady=30)

        # Add button
        self.add = tkr.Button(self)
        self.add["text"] = "Add Word to Dictionary"
        self.add.pack(side="right", expand=True, padx=4, pady=0)
        self.add["command"] = self.hide_main



    def hide_main(self):
        self.retrieve.forget()
        self.add.pack_forget()
        self.check.pack_forget()
        self.quit.pack_forget()
        self.labelDir.forget()
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
        self.wordDir.forget()
        self.posDir.forget()
        self.defiDir.forget()


    def add_word(self):

        dict = Dictionary()

        # Exit button
        self.quit = tkr.Button(self, text="Exit", fg="red", command=root.destroy)
        self.quit.pack(side="right", expand=True, padx=4, pady=20)

        # Save button
        self.save = tkr.Button(self)
        self.save["text"] = "Save"
        self.save["command"] = lambda: dict.saveWord(self.word.get(), self.pos.get(), self.defi.get())
        self.save.pack(side="right",expand=True, padx=4, pady=0)

        # Back button
        self.back = tkr.Button(self)
        self.back["text"] = "Back"
        self.back["command"] = lambda: self.hide_add()
        self.back.pack(side="right", expand=True, padx=4, pady=0)

        # Word
        self.wordLabel = tkr.StringVar()
        self.wordLabel.set("Word:")
        self.wordDir = Label(root, textvariable=self.wordLabel, height=0)
        self.wordDir.pack(side="top")

        self.word = tkr.Entry(root)
        self.word.insert(0, "Type in the word you want to add")
        self.word.pack(side="top", fill='x', expand=True, padx=30, pady=0)

        # PoS
        self.posLabel = tkr.StringVar()
        self.posLabel.set("Part of Speech:")
        self.posDir = Label(root, textvariable=self.posLabel, height=0)
        self.posDir.pack(side="top")

        self.pos = tkr.Entry(root)
        self.pos.insert(0, "Type the part of speech")
        self.pos.place(x=150, y=150, width=100, height=25)
        self.pos.pack(side="top", fill='x', expand=True, padx=30, pady=0)

        # Definition
        self.defiLabel = tkr.StringVar()
        self.defiLabel.set("Defintion")
        self.defiDir = Label(root, textvariable=self.defiLabel, height=0)
        self.defiDir.pack(side="top")

        self.defi = tkr.Entry(root)
        self.defi.insert(0, "Type the defintion")
        self.defi.place(x=150, y=200, width=100, height=25)
        self.defi.pack(side="top", fill='x', expand=True, padx=30, pady=0)

root = tkr.Tk()
root.geometry("400x300")
app = GUIstuff(master=root)
app.mainloop()