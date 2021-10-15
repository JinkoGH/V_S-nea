"""Instruction sheet with all the requirements for registering an account"""
"""level2"""
#imports
import tkinter as tk
from tkinter import ttk
import re

# Getting preset integers
from V_Ssettings import *

class RegInstruction_screen:

    def __init__(self, master):
        self.master = master
        self.master.geometry(screen_size)
        self.frame = tk.Frame(self.master)
        self.frame.grid()
        # Main title
        self.title = tk.Label(self.frame, text="Follow the requirements",
                              background="grey", foreground="white", height=titleH, width=titleW).grid(row=0)
        self.space = tk.Label(self.frame, text="").grid(row=1)
        # Username
        self.label = tk.Label(self.frame,text="Username requirements",
                              background="grey",foreground="white", height=labelH, width=labelW2).grid(row=2)
        self.label = tk.Label(self.frame, justify=tk.LEFT, text="-Username length must be 4-16\n-Username should not include space").grid(row=3)
        self.space = tk.Label(self.frame, text="").grid(row=4)
        # Password
        self.label = tk.Label(self.frame, text="Password requirements",
                              background="grey",foreground="white", height=labelH, width=labelW2).grid(row=5)
        self.label = tk.Label(self.frame, justify=tk.LEFT, text="-Password length must be 4-16\n-Password must include both capital\n and lowercase letters\n-Password must include numbers\n-Password should not have any spaces").grid(row=6)
        self.space = tk.Label(self.frame, text="").grid(row=7)
        self.button = tk.Button(self.frame, text="Return", command=self.close_screen,
                                background="grey", foreground="white", height=buttonH, width=buttonW2).grid(row=8)

    # Exit button
    def close_screen(self):
        self.master.destroy()








                               
