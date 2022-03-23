"""Main hub for navigation of gui. (After user logs in)"""
"""level3"""
#imports
import tkinter as tk
import os

# Importing classes
from V_S_Lsetting import Setting
# Getting preset integers
from V_S_Lsettings import *

class Main_screen(tk.Frame):
    def __init__(self, master, controller):
        self.controller = controller
        tk.Frame.__init__(self, master)

        # Background
        self.light_bg = tk.PhotoImage(file="Images/Light bg.png")
        # self.dark_bg = tk.PhotoImage(file="Image/Dark bg.png")
        self.bg = tk.Label(self, image=self.light_bg)
        # Title
        self.title = tk.Label(self, text="Vegetation simulation\nmain menu",
                              height=titleH, width=titleW)
        # buttons
        self.space = tk.Label(self, text="")
        self.button = tk.Button(self, text="Load/create save", command=self.open_loadcreatesave,
                                height=buttonH, width=buttonW)

        self.space1 = tk.Label(self, text="")
        self.button1 = tk.Button(self, text="Settings", command=self.open_setting,
                                 height=buttonH, width=buttonW)
        self.space2 = tk.Label(self, text="")
        self.button2 = tk.Button(self, text="Instruction",
                                 height=buttonH, width=buttonW)
        self.space3 = tk.Label(self, text="")
        self.button3 = tk.Button(self, text="Gallery",
                                 bg="grey", fg="white", height=buttonH, width=buttonW)
        self.space4 = tk.Label(self, text="")
        self.return_button = tk.Button(self, text="Log out", command=self.return_screen,
                                       height=buttonH, width=buttonW)
        # Applying colour attributes to widgets and the frame
        self.colour_theme()
        # Giving the widgets position via grid
        self.title.grid(row=0)
        self.space.grid(row=1)
        self.space1.grid(row=3)
        self.space2.grid(row=5)
        self.space3.grid(row=7)
        self.space4.grid(row=9)
        self.button.grid(row=2)
        self.button1.grid(row=4)
        self.button2.grid(row=6)
        self.button3.grid(row=8)
        self.return_button.grid(row=10)
        # Placing the label holding the image
        self.bg.place(x=0, y=0, relwidth=1, relheight=1)

    def colour_theme(self):
        self.title.config(bg="grey", fg="white")
        self.space.config(bg="white")
        self.space1.config(bg="white")
        self.space2.config(bg="white")
        self.space3.config(bg="white")
        self.space4.config(bg="white")
        self.button.config(bg="grey", fg="white")
        self.button1.config(bg="grey", fg="white")
        self.button2.config(bg="grey", fg="white")
        self.button3.config(bg="grey", fg="white")
        self.return_button.config(bg="grey", fg="white")

    # Functions assigned to buttons to open windows
    def open_loadcreatesave(self):
        self.controller.display_frame("LoadCreateSave")

    def open_setting(self):
        pass

    def open_instructions(self):
        pass

    def open_gallary(self):
        pass

    # Function for changing the theme colours


    # Closing function
    def return_screen(self):
        self.controller.display_frame("Userhub_screen")

class LoadCreateSave(tk.Frame):
    def __init__(self, master, controller):
        self.controller = controller
        tk.Frame.__init__(self, master)
        # Background
        self.light_bg = tk.PhotoImage(file="Images/Light bg.png")
        self.bg = tk.Label(self, image=self.light_bg)
        # title
        self.title = tk.Label(self, text="Select an option",
                              height=titleH, width=titleW)
        self.space = tk.Label(self, text="")
        # button
        self.button = tk.Button(self, text="Load saves", command=self.loadsaves,
                                height=buttonH, width=buttonW)
        self.space1 = tk.Label(self, text="")
        self.button1 = tk.Button(self, text="Create save", command=self.createsaves,
                                 height=buttonH, width=buttonW)
        self.space2 = tk.Label(self, text="")
        self.return_button = tk.Button(self, text="Return to main menu", command=self.return_screen,
                                       height=buttonH, width=buttonW)
        #Applying the default colour theme
        self.colour_theme()
        # Giving widgets position via grid
        self.title.grid(row=0)
        self.space.grid(row=1)
        self.space1.grid(row=3)
        self.space2.grid(row=5)
        self.button.grid(row=2)
        self.button1.grid(row=4)
        self.return_button.grid(row=6)
        # Placing the label holding the image
        self.bg.place(x=0, y=0, relwidth=1, relheight=1)

    def colour_theme(self):
        self.title.config(bg="grey", fg="white")
        self.space.config(bg="white")
        self.space1.config(bg="white")
        self.space2.config(bg="white")
        self.button.config(bg="grey", fg="white")
        self.button1.config(bg="grey", fg="white")
        self.return_button.config(bg="grey", fg="white")


    # Functions assigned to buttons to either load or create save files.
    def loadsaves(self):
        os.system('V_Smain.py')
    def createsaves(self):
        pass
    
    # Closing function
    def return_screen(self):
        self.controller.display_frame("Main_screen")





