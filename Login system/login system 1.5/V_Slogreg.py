# imports
import tkinter as tk
from tkinter import ttk

# connecting other files
from V_Sreg import Reg_screen
from V_Slog import Log_screen
from V_Ssettings import *

class LogReg_screen():

    # Base window or TopRoot
    def __init__(self, master):
        self.master = master
        self.master.geometry(screen_size)
        self.frame = tk.Frame(master)
        self.frame.grid()
        # title
        self.master.title("Vegetation simulation")
        self.title = tk.Label(text="Vegetation Simulation User Portal",
                              background="grey", foreground="white", height=titleH, width=titleW).grid(row=0, column=0)

        # buttons
        self.space = tk.Label(text="").grid(row=1)
        self.button = tk.Button(text="Login", command=self.openlog_screen,
                                background="grey", foreground="white", height=buttonH, width=buttonW).grid(row=2)
        self.space = tk.Label(text="").grid(row=3)
        self.button = tk.Button(text="Register", command=self.openreg_screen,
                                background="grey", foreground="white", height=buttonH, width=buttonW).grid(row=4)
        self.space = tk.Label(text="").grid(row=5)
        self.button = tk.Button(text="Exit program", command=self.close_screen,
                                background="grey", foreground="white", height=buttonH, width=buttonW).grid(row=6)
        self.frame.grid()

    # functions for buttons to open windows
    def openreg_screen(self):
        self.openreg_screen = tk.Toplevel(self.master)
        self.app = Reg_screen(self.openreg_screen)

    def openlog_screen(self):
        self.openlog_screen = tk.Toplevel(self.master)
        self.app = Log_screen(self.openlog_screen)

    # Exit button
    def close_screen(self):
        self.master.destroy()

# Main loop
def main():
    root = tk.Tk()
    app = LogReg_screen(root)
    root.mainloop()

if __name__ == '__main__':
    main()
