"""Initial/base screen and TopRoot"""
"""level1"""
# imports
import tkinter as tk
from tkinter import ttk

# connecting other files
from V_Saccount import Log_screen, Reg_screen
from V_Ssettings import *

class Userhub_screen():

    # Base window or TopRoot
    def __init__(self, master):
        self.master = master
        self.master.geometry(screen_size)
        self.frame = tk.Frame(master)
        self.frame.grid()

        # title
        self.master.title("Vegetation simulation")
        self.title = tk.Label(master, text="Vegetation Simulation User Portal",
                              bg="grey", fg="white", height=titleH, width=titleW)
        self.title.grid(row=0)

        # buttons
        self.space = tk.Label(master, text="")
        self.space.grid(row=1)
        self.button = tk.Button(master, text="Login", command=self.openlog_screen,
                                bg="grey", fg="white", height=buttonH, width=buttonW)
        self.button.grid(row=2)
        self.space1 = tk.Label(master, text="")
        self.space1.grid(row=3)
        self.button1 = tk.Button(master, text="Register", command=self.openreg_screen,
                                 bg="grey", fg="white", height=buttonH, width=buttonW)
        self.button1.grid(row=4)
        self.space2 = tk.Label(master, text="")
        self.space2.grid(row=5)
        self.quit = tk.Button(master, text="Exit program", command=self.close_screen,
                              bg="grey", fg="white", height=buttonH, width=buttonW)
        self.quit.grid(row=6)

        #self.test = tk.Button(master, text="test", command=self.darktheme,
        #                      bg="grey", fg="white", height=buttonH, width=buttonW)
        #self.test.grid(row=7)

    # Functions assigned to buttons to open windows
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
    app = Userhub_screen(root)
    root.mainloop()

if __name__ == '__main__':
    main()
