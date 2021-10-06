#imports
from tkinter import *
from tkinter import ttk

import sqlite3
import os

root = Tk()

class logreg_screen:
        #First screen 
        def __init__(self, root ):
                # Login and register screen
                self.root = root
                self.titlesize =("1000x600")
               

        def logregscreen():
                logreg_root.geometry(self.titlesize)
                logreg_root.title("Vegetation simulation")
                Label(text = "Vegetation simulation\nuser portal", background ="grey", foreground ="white" ,height = "2", width = "35").pack()
                #buttons
                Label(text="").pack()
                Button(text = "Login", command = login_screen, height = "1", width = "15",background ="grey", foreground ="white").pack()

                Label(text= "").pack()
                Button(text = "Register", command = register_screen, height = "1", width = "15", background ="grey", foreground ="white").pack()
        
                Label(text="").pack()
                Button(text="Exit program", command= logreg_root.destroy, height="1", width="15", background ="grey", foreground ="white").pack()

                logreg_root.mainloop()
                

        




