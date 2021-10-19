""" Settings screen to allow the user to change various things in the gui or inputs"""
"""level3"""
#imports
import tkinter as tk
from tkinter import ttk

# Getting preset integers
from V_Ssettings import *


class Setting():
    def __init__(self, master):
        self.master = master
        self.master.geometry(screen_size)
        self.frame = tk.Frame(self.master)
        self.frame.grid()
        # title
        self.master.title("Settings")
        self.title = tk.Label(self.frame, text="Settings",
                              background="grey", foreground="white", height=titleH, width=titleW).grid(row=0)
        self.space = tk.Label(self.frame, text="").grid(row=1)
        # button
        self.button = tk.Button(self.frame, text="Graphical settings",
                                background="grey", foreground="white", height=buttonH, width=buttonW).grid(row=2)
        self.space = tk.Label(self.frame, text="").grid(row=3)
        self.button = tk.Button(self.frame, text="Interface settings", command=self.open_interfaceset,
                                background="grey", foreground="white", height=buttonH, width=buttonW).grid(row=4)
        self.space = tk.Label(self.frame, text="").grid(row=5)
        self.button = tk.Button(self.frame, text="Audio settings", command=self.open_audioset,
                                background="grey", foreground="white", height=buttonH, width=buttonW).grid(row=6)
        self.space = tk.Label(self.frame, text="").grid(row=7)
        self.button = tk.Button(self.frame, text="Control settings", command=self.open_controlset,
                                background="grey", foreground="white", height=buttonH, width=buttonW).grid(row=8)
        self.space = tk.Label(self.frame, text="").grid(row=9)
        self.button = tk.Button(self.frame, text="Return to main menu", command=self.close_screen,
                                background="grey", foreground="white", height=buttonH, width=buttonW).grid(row=10)

    # Functions assigned to buttons to open other screens
    def open_graphicalset(self):
        pass
    def open_audioset(self):
        pass
    def open_controlset(self):
        pass

    # Closing function
    def close_screen(self):
        self.master.destroy()

class GraphicalStyle():
    pass

# class InterfaceSet():
#     def __init__(self, master):
#         self.master = master
#         self.master.geometry(screen_size)
#         self.frame = tk.Frame(self.master)
#         self.frame.grid()
#
#         # title
#         self.master.title("Interface settings")
#         self.title = tk.Label(master, text="Interface settings",
#                               bg="grey", fg="white", height=titleH, width=titleW)
#         self.title.grid(row=0)
#         self.space = tk.Label(master, text="")
#         self.space.grid(row=1)
#         # assigning each radio buttons to a variable
#         self.v = tk.IntVar()
#         # button
#         self.radio = tk.Radiobutton(master, text="Light theme", command=self.lighttheme,
#                                     indicatoron=0, variable=self.v, value=0, height=radioH, width=radioW)
#         self.radio.grid(row=2)
#         self.space1 = tk.Label(master, text="")
#         self.space1.grid(row=3)
#         self.radio1 = tk.Radiobutton(master, text="Dark theme", command=self.darktheme,
#                                      indicatoron=0, variable=self.v, value=1, height=radioH, width=radioW)
#         self.radio1.grid(row=4)
#         self.space2 = tk.Label(master, text="")
#         self.space2.grid(row=5)
#         self.quit = tk.Button(master, text="Return to main menu", command=self.close_screen,
#                               background="grey", foreground="white", height=buttonH, width=buttonW)
#         self.quit.grid(row=6)
#
#         # Empty labels for using in other areas of the gui
#         self.button = tk.Button()
#         self.button1 = tk.Button()
#
#         # Linking to the other files
#         self.hub = Userhub_screen(master)
#
#
#     # Functions for changing the interface of the gui
#
#     def lighttheme(self):
#
#         self.master.config(bg="white")
#         self.title.config(bg="grey", fg="white")
#         self.space.config(bg="white")
#         self.space1.config(bg="white")
#         self.space2.config(bg="white")
#         self.quit.config(bg="grey", fg="white")
#
#     def darktheme(self):
#         # Local screen change
#         self.master.config(bg="black")
#         self.title.config(bg="grey", fg="black")
#         self.space.config(bg="black")
#         self.space1.config(bg="black")
#         self.space2.config(bg="black")
#         self.quit.config(bg="grey", fg="black")
#         # External screen changes
#         self.hub.master.config(bg="black")
#         self.hub.title.config(bg="black")
#         self.hub.space.config(bg="black")
#         self.hub.space1.config(bg="black")
#         self.hub.space2.config(bg="black")
#         self.hub.button.config(bg="grey", fg="black")
#         self.hub.button1.config(bg="grey", fg="black")
#         self.hub.quit.config(bg="grey", fg="black")
#
#     # Closing function
#     def close_screen(self):
#         self.master.destroy()
