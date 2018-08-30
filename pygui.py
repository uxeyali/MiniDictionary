

import tkinter as tkr

class Dictionary(tkr.Frame):
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
        self.quit.pack(side="bottom")
        
        self.add = tkr.Button(self)
        self.add["text"] = "Add a Word"
        self.add.pack(side="top")
       
        self.save = tkr.Button(self)
        self.save["text"] = "Save"
        self.save.pack(side="top")
       
        
    def say_hi(self):
        print("Definition:")
        
root = tkr.Tk()
root.geometry("500x500")
app = Dictionary(master=root)
app.mainloop()