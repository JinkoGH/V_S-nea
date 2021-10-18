"""Main hub for navigation of gui. (After user logs in)"""
"""level3"""
#imports
import tkinter as tk
from tkinter import ttk

# Importing classes
from V_Ssetting import Setting#, InterfaceSet
# Getting preset integers
from V_Ssettings import *

class Main_screen():
    def __init__(self, master):
        self.master = master
        self.master.geometry(screen_size)
        self.frame = tk.Frame(self.master)
        self.frame.grid()
        # Title
        self.master.title("Main menu")
        self.title = tk.Label(master, text="Vegetation simulation\nmain menu",
                              bg="grey", fg="white", height=titleH, width=titleW)
        self.title.grid(row=0)
        # buttons
        self.space = tk.Label(master, text="")
        self.space.grid(row=1)
        self.button = tk.Button(master, text="Load/create save", command=self.open_loadcreatesave,
                                bg="grey", fg="white", height=buttonH, width=buttonW)
        self.button.grid(row=2)
        self.space1 = tk.Label(master, text="")
        self.space1.grid(row=3)
        self.button1 = tk.Button(master, text="Settings", command=self.open_setting,
                                 bg="grey", fg="white", height=buttonH, width=buttonW)
        self.button1.grid(row=4)
        self.space2 = tk.Label(master, text="")
        self.space2.grid(row=5)
        self.button2 = tk.Button(master, text="Instruction",
                                 bg="grey", fg="white", height=buttonH, width=buttonW)
        self.button2.grid(row=6)
        self.space3 = tk.Label(master, text="")
        self.space3.grid(row=7)
        self.button3 = tk.Button(master, text="Gallery",
                                 bg="grey", fg="white", height=buttonH, width=buttonW)
        self.button3.grid(row=8)
        self.space4 = tk.Label(master, text="")
        self.space4.grid(row=9)
        self.quit = tk.Button(master, text="Exit", command=self.close_screen,
                              bg="grey", fg="white", height=buttonH, width=buttonW)
        self.quit.grid(row=10)

    # Functions assigned to buttons to open windows
    def open_loadcreatesave(self):
        self.open_loadcreatesave = tk.Toplevel(self.master)
        self.app = LoadCreateSave(self.open_loadcreatesave)

    def open_setting(self):
        self.open_setting = tk.Toplevel(self.master)
        self.app = Setting(self.open_setting)

    def open_instructions(self):
        pass

    def open_gallary(self):
        pass

    # Function for changing the theme colours


    # Closing function
    def close_screen(self):
        self.master.destroy()

class LoadCreateSave():
    def __init__(self, master):
        self.master = master
        self.master.geometry(screen_size)
        self.frame = tk.Frame(self.master)
        self.frame.grid()
        # title
        self.title = tk.Label(self.frame, text="Select an option",
                              bg="grey", fg="white", height=titleH, width=titleW)
        self.title.grid(row=0)
        self.space = tk.Label(self.frame, text="").grid(row=1)
        self.space.grid(row=1)
        # button
        self.button = tk.Button(self.frame, text="Load saves", command=self.loadsaves,
                                bg="grey", fg="white", height=buttonH, width=buttonW)
        self.space1 = tk.Label(self.frame, text="").grid(row=3)
        self.space1.grid(row=3)
        self.button1 = tk.Button(self.frame, text="Create save", command=self.createsaves,
                                 bg="grey", fg="white", height=buttonH, width=buttonW)
        self.button1.grid(row=4)
        self.space2 = tk.Label(self.frame, text="").grid(row=5)
        self.space2.grid(row=5)
        self.button2 = tk.Button(self.frame, text="Return to main menu", command=self.close_screen,
                                 bg="grey", fg="white", height=buttonH, width=buttonW)
        self.button2.grid(row=6)

    # Functions assigned to buttons to either load or create save files.
    def loadsaves(self):
        pass
    def createsaves(self):
        pass
    
    # Closing function
    def close_screen(self):
        self.master.destroy()




