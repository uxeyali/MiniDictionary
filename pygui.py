import os, sys

import tkinter as tkr
from os.path import join

import pandas as pd
from tkinter import messagebox
from tkinter import Label
import os

import sys
if getattr( sys, 'frozen', False ) :
    # we are running in a bundle
    frozen = 'ever so'
    bundle_dir = sys._MEIPASS
else :
    bundle_dir = os.path.dirname(os.path.abspath(__file__))
    print(bundle_dir)

class Dictionary:
    df = None
    wordName = None
    partOfSpeech = None
    definition = None

    def __init__(self):
        # Pulling the data from the dictionary
        data = pd.read_csv(os.path.join(bundle_dir, "Dictionary.csv"), header=0)
        self.df = pd.DataFrame(data)

    # This function will retrieve the word from the dictionary when called.
    def retrieveword(self, word):
        # Get the row of the word sent into the function. If it doesnt exist, it is going to be empty.
        row = self.df.loc[self.df['Word'] == word]

        # If the word exists in the dictionary, retrieve the row.
        if row.empty is False:

            # Retrieve the wordname, definition, and part of speech.
            wordName = row['Word'].to_string(index=False)
            definition = row["Definition"].to_string(index=False)
            partOfSpeech = row["PartOfSpeech"].to_string(index=False)

            # Put it into an array
            lines = ["Word: wordName", wordName,"", 'Definition: ', definition,"", "Part of speech: ", partOfSpeech]

            # Display the information as a messagebox
            messagebox.showinfo(wordName, "\n".join(lines))

        # If the row is empty
        else:
            # Display error
            messagebox.showinfo("Error", "Error: Word does not exist")

    # This function will save the word to the file
    def saveWord(self, word, partOfSpeech, definition):

        # Find the word if it exists in the dictionary
        row = self.df.loc[self.df['Word'] == word]

        # If the word doesnt exist, save it
        if row.empty is True:

            # Make row with the arguments sent into the function
            row = pd.DataFrame({'Word': [word], 'PartOfSpeech': [partOfSpeech], 'Definition': [definition]})

            # Append it to the dictionary information we already have
            self.df = self.df.append(row, sort = False)

            # write over the current Dictionary info with the new information
            with open("Dictionary.csv", 'w') as f:
                self.df.to_csv(f, header=True, index=False)

                # confirm addition
                messagebox.showinfo("Added","Word added to dictionary.")

        # If word exists, display error message
        else:
            messagebox.showinfo("Error", "Word already exists in the dictionary")

#
class GUIstuff(tkr.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    # The main page called when initialized
    def create_widgets(self):
        dict = Dictionary()

        # Title of window
        self.winfo_toplevel().title("Mini Dictionary")

        # Label for the Entry for Retrieving the word.
        self.labelText = tkr.StringVar()
        self.labelText.set("Retrieve word:")
        self.labelDir = Label(root, textvariable=self.labelText, height=0)
        self.labelDir.pack(side="top")

        # Retrieving input
        self.retrieve = tkr.Entry(root)
        self.retrieve.insert(0, "Type in the word you want to add")
        self.retrieve.pack(side="top", fill='x', padx=30)

        # Check definition - button
        self.check = tkr.Button(root)
        self.check["text"] = "Definition"
        self.check.pack(side="top", padx=10, pady=20)
        self.check["command"] = lambda: dict.retrieveword(self.retrieve.get())


        # Exit - button
        self.quit = tkr.Button(self, text="Exit", fg="red", bg="black", command=root.destroy)
        self.quit.pack(side="right", expand=True, padx=4, pady=30)

        # Add - button
        self.add = tkr.Button(self)
        self.add["text"] = "Add Word to Dictionary"
        self.add.pack(side="right", expand=True, padx=4, pady=0)
        self.add["command"] = self.hide_main


    # Hides the main page when Add button is clicked
    def hide_main(self):
        self.retrieve.forget()
        self.add.pack_forget()
        self.check.pack_forget()
        self.quit.pack_forget()
        self.labelDir.forget()
        self.add_word()

    # Hids the Add page when the Back button is clicked
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

    # Add word screen.
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

        # Word - label and input
        # Label
        self.wordLabel = tkr.StringVar()
        self.wordLabel.set("Word:")
        self.wordDir = Label(root, textvariable=self.wordLabel, height=0)
        self.wordDir.pack(side="top")

        # Input
        self.word = tkr.Entry(root)
        self.word.insert(0, "Type in the word you want to add")
        self.word.pack(side="top", fill='x', expand=True, padx=30, pady=0)

        # PoS - label and input
        # Label
        self.posLabel = tkr.StringVar()
        self.posLabel.set("Part of Speech:")
        self.posDir = Label(root, textvariable=self.posLabel, height=0)
        self.posDir.pack(side="top")

        # Input
        self.pos = tkr.Entry(root)
        self.pos.insert(0, "Type the part of speech")
        self.pos.place(x=150, y=150, width=100, height=25)
        self.pos.pack(side="top", fill='x', expand=True, padx=30, pady=0)

        # Definition - label and input
        # Label
        self.defiLabel = tkr.StringVar()
        self.defiLabel.set("Defintion")
        self.defiDir = Label(root, textvariable=self.defiLabel, height=0)
        self.defiDir.pack(side="top")

        # Input
        self.defi = tkr.Entry(root)
        self.defi.insert(0, "Type the defintion")
        self.defi.place(x=150, y=200, width=100, height=25)
        self.defi.pack(side="top", fill='x', expand=True, padx=30, pady=0)

root = tkr.Tk()
root.geometry("400x300")
app = GUIstuff(master=root)
app.mainloop()

