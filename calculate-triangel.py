from tkinter import ttk
from tkinter import *

#initiate the window
root = Tk()
root.geometry('800x600')

class  Window:
    def __init__(self, master):
        canvas = Canvas(master, bg='black', height=400, width=800).pack()
        #frame = Frame(master, height=200, width=800).pack()
        inputs = LabelFrame(master, text='User Inputs', bg='white', height=150, width=750).pack()
        
        self.submit_button = Button(inputs, text='submit')
        self.submit_button.pack()

display = Window(root)
        



root.mainloop()
