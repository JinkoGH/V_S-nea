#imports
import tkinter as tk
#from login_system_settings import Custom
from tkinter import ttk
import sqlite3
import os

screen_size = ("500x500")

class LogReg_screen:

    # Base window or toproot
    def __init__(self, master):
        self.master = master
        self.master.geometry(screen_size)
        self.frame = tk.Frame(master)
        # title
        self.master.title("Vegetation simulation")
        self.title = tk.Label(text = "Vegetation simulation\nuser portal", background="grey", foreground="white",
                              height="2", width="35").pack()

        # buttons
        self.space = tk.Label(text="").pack()
        self.button = tk.Button(text="Login", command = self.openlog_screen(), background="grey", foreground="white",
                                height="1", width="15").pack()
        self.space = tk.Label(text="").pack()
        self.button = tk.Button(text="Register", command=self.openreg_screen, background="grey", foreground="white",
                                height="1", width="15").pack()
        self.space = tk.Label(text="").pack()
        self.button = tk.Button(text="Exit program", command = self.close_screen, background="grey", foreground="white",
                                height="1", width="15").pack()
        self.frame.pack()

    # functions for buttons to open windows
    def openreg_screen(self):
        pass
    def openlog_screen(self):
        pass

    # Exit button
    def close_screen(self):
        self.master.destroy()

class reg_screen:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.master.destroy()

# The main loop where classes are looped.
def main():
    root = tk.Tk()
    LogReg_screen(root)
    root.mainloop()

# Allowing classes to function
if __name__ == '__main__':
    main()




        




