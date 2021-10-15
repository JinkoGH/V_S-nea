"""Main hub for navigation of gui. (After user logs in)"""
"""level3"""
#imports
import tkinter as tk
from tkinter import ttk

# Getting preset integers
from V_Ssettings import *

class Main_screen:
    def __init__(self, master):
        self.master = master
        self.master.geometry(screen_size)
        self.frame = tk.Frame(self.master)
        self.frame.grid()
        # Title
        self.label = tk.Label(self.frame, text="Vegetation simulation\nmain menu",
                              background="grey", foreground="white", height=titleH, width=titleW).grid(row=0)
        # buttons
        self.space = tk.Label(self.frame, text="").grid(row=1)
        self.button = tk.Button(self.frame, text="Load/create save",
                                background="grey", foreground="white", height=buttonH, width=buttonW).grid(row=2)
        self.label = tk.Label(self.frame, text="").grid(row=3)
        self.button = tk.Button(self.frame, text="Settings",
                                background="grey", foreground="white", height=buttonH, width=buttonW).grid(row=4)
        self.label = tk.Label(self.frame, text="").grid(row=5)
        self.button = tk.Button(self.frame, text="Instruction",
                                background="grey", foreground="white", height=buttonH, width=buttonW).grid(row=6)
        self.label = tk.Label(self.frame, text="").grid(row=7)
        self.button = tk.Button(self.frame, text="Gallery",
                                background="grey", foreground="white", height=buttonH, width=buttonW).grid(row=8)
        self.label = tk.Label(self.frame, text="").grid(row=9)
        self.button = tk.Button(self.frame, text="Exit", command=self.close_screen,
                                background="grey", foreground="white", height=buttonH, width=buttonW).grid(row=10)

    # Functions assigned to buttons to open windows
    def open_loadcreatesave(self):
        self.open_loadcreatesave = tk.Toplevel(self.master)
        self.app = LoadCreateSave(self.open_loadcreatesave)

    def open_settings(self):
        pass

    def open_instructions(self):
        pass

    def open_gallary(self):
        pass

    # Closing function
    def close_screen(self):
        self.master.destroy()

class LoadCreateSave:
    def __init__(self, master):
        self.master = master
        self.master.geometry(screen_size)
        self.frame = tk.Frame(self.master)
        self.frame.grid()
        # title
        self.title = tk.Label(self.frame, text="Select an option",
                              background="grey", foreground="white", height=titleH, width=titleW).grid(row=0)
        self.space = tk.Label(self.frame, text="").grid(row=1)
        # button
        self.button = tk.Button(self.frame, text="Load saves", command=self.loadsaves,
               height="1", width="17", background="grey", foreground="white").grid(row=2)
        self.space = tk.Label(self.frame, text="").grid(row=3)
        self.button = tk.Button(self.frame, text="Create save", command=self.createsaves,
               height="1", width="17", background="grey", foreground="white").grid(row=4)
        self.space = tk.Label(self.frame, text="").grid(row=5)
        self.button = tk.Button(self.frame, text="Return to main menu", command= self.close_screen,
               height="1", width="17", background="grey", foreground="white").grid(row=6)

    # Functions assigned to buttons to open windows
    def loadsaves(self):
        pass
    def createsaves(self):
        pass
    
    # Closing function
    def close_screen(self):
        self.master.destroy()


