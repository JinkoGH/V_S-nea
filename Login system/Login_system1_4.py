#imports
from tkinter import *
import sqlite3
import os

root = Tk()

class GUI:
        def __init__(self, root, screensize, title, label, button):
                # Login and register screen
                self.root = root
                self.screensize = root.geometry
                self.title = self.root.title
                self.label = Label(root)
                self.button = Button(root)
                self.root.mainloop()
        def logreg_screen():
                root.geometry("500x1000")
                self.title("Vegetation simulation")
                Label(text = "Vegetation simulation\nuser portal", background ="grey", foreground ="white" ,height = "2", width = "35").pack()
                #buttons
                self.label(text="").pack()
                self.button(text = "Login" , height = "1", width = "15",background ="grey", foreground ="white").pack()

                self.label(text= "").pack()
                self.button(text = "Register" , height = "1", width = "15", background ="grey", foreground ="white").pack()

                self.label(text="").pack()
                self.button(text="Exit program", command= logreg_root.destroy, height="1", width="15", background ="grey", foreground ="white").pack()

                logreg_root.mainloop()
                

        




