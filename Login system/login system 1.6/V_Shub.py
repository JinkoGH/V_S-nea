"""Initial/base screen and TopRoot"""
"""level1"""
# imports
import tkinter as tk
from tkinter import ttk

# connecting other files
from V_Saccount import Log_screen, Reg_screen
from V_Smain import Main_screen, LoadCreateSave
from V_Ssetting import Setting

# Getting preset integers
from V_Ssettings import *

class Userhub_screen:

    # Base window or TopRoot
    def __init__(self, root):
        # Class attributes
        self.root = root
        self.root.geometry(screen_size)
        self.frame = tk.Frame(root)
        self.frame.grid()

        # title
        self.root.title("Vegetation simulation")
        self.title = tk.Label(root, text="Vegetation Simulation User Portal",
                              bg="grey", fg="white", height=titleH, width=titleW)
        self.title.grid(row=0)

        # buttons
        self.space = tk.Label(root, text="")
        self.space.grid(row=1)
        self.button = tk.Button(root, text="Login", command=self.openlog_screen,
                                bg="grey", fg="white", height=buttonH, width=buttonW)
        self.button.grid(row=2)
        self.space1 = tk.Label(root, text="")
        self.space1.grid(row=3)
        self.button1 = tk.Button(root, text="Register", command=self.openreg_screen,
                                 bg="grey", fg="white", height=buttonH, width=buttonW)
        self.button1.grid(row=4)
        self.space2 = tk.Label(root, text="")
        self.space2.grid(row=5)

        # create menu and options
        self.my_menu = tk.Menu(root)
        root.config(menu=self.my_menu)
        self.theme_menu = tk.Menu(self.my_menu, tearoff=False)
        # self.theme_menu.grid(row=6)
        self.my_menu.add_cascade(label="Interface theme", menu=self.theme_menu)
        self.theme_menu.add_command(label="Light theme", command=self.lighttheme)
        self.theme_menu.add_command(label="Dark theme", command=self.darktheme)
        self.space3 = tk.Label(root, text="")
        self.space3.grid(row=7)

        # quit button
        self.quit = tk.Button(root, text="Exit program", command=self.close_screen,
                              bg="grey", fg="white", height=buttonH, width=buttonW)
        self.quit.grid(row=6)

        #self.test = tk.Button(master, text="test", command=self.darktheme,
        #                      bg="grey", fg="white", height=buttonH, width=buttonW)
        #self.test.grid(row=7)


    # Functions for menu
    def lighttheme(self):
        # Local window
        self.root.config(bg="white")
        self.title.config(fg="white")
        self.space.config(bg="white")
        self.space1.config(bg="white")
        self.space2.config(bg="white")
        self.space3.config(bg="white")
        self.button.config(fg="white")
        self.button1.config(fg="white")
        self.quit.config(fg="white")
        # Linking other classes to access their attributes
        # External windows
        #self.log_screen.master.config(bg="white")

    def darktheme(self):
        # Local window
        self.root.config(bg="black")
        self.title.config(bg="grey", fg="black")
        self.space.config(bg="black")
        self.space1.config(bg="black")
        self.space2.config(bg="black")
        self.space3.config(bg="black")
        self.button.config(fg="black")
        self.button1.config(fg="black")
        self.quit.config(bg="grey", fg="black")
        # Linking other classes to access their attributes

        # External windows
        # self.log_screen.master.config(bg="black")
        # self.log_screen.space.config(bg="black")
        # self.log_screen.label.config(bg="grey", fg="black")


    # Functions assigned to buttons to open windows
    def openreg_screen(self):
        self.openreg_screen = tk.Toplevel(self.root)
        self.app = Reg_screen(self.openreg_screen)

    def openlog_screen(self):
        self.openlog_screen = tk.Toplevel(self.root)
        self.app = Log_screen(self.openlog_screen)

    # Exit button
    def close_screen(self):
        self.root.destroy()

# Main loop
def main():
    root = tk.Tk()
    app = Userhub_screen(root)
    root.mainloop()

if __name__ == '__main__':
    main()
