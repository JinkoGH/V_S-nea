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


class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Container used to stack frames on top of each other
        base_frame = tk.Frame(self)
        base_frame.grid()

        # Attribute to hold the list of names of pages
        self.frames = {}
        # Creating classes and creating instances
        for F in (Userhub_screen, Log_screen):
            frame_name = F.__name__
            frame = F(master=base_frame, controller=self)
            self.frames[frame_name] = frame
            # Positioning the frame so that the north, south, east and west corners match up together to
            # stack on each other
            frame.grid(row=0, column=0, sticky="nsew")

        # Displaying the user hub screen as the default initial screen
        self.display_frame("Userhub_screen")

    def get_frame(self, frame_name):
        frame = self.frames[frame_name]
        return frame

    def display_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()

        # menu_theme = frame.my_menu(self)
        # self.configure(menu=menu_theme)


class Userhub_screen(tk.Frame):
    # Base window or TopRoot
    def __init__(self, master, controller):
        # Class attributes
        tk.Frame.__init__(self, master)
        tk.Frame.config(self, bg="white")
        self.controller = controller
        self.title = tk.Label(self, text="Vegetation Simulation User Portal",
                              bg="grey", fg="white", height=titleH, width=titleW)
        # buttons
        self.space = tk.Label(self, text="", bg="white")
        self.button = tk.Button(self, text="Login", command=self.openlog_screen,
                                bg="grey", fg="white", height=buttonH, width=buttonW)
        self.space1 = tk.Label(self, text="", bg="white")
        self.button1 = tk.Button(self, text="Register", command=self.openreg_screen,
                                 bg="grey", fg="white", height=buttonH, width=buttonW)
        self.space2 = tk.Label(self, text="", bg="white")
        self.space2.grid(row=5)
        self.button2 = tk.Button(self, text="Light theme", command=self.light_theme,
                                 bg="grey", fg="white", height=buttonH, width=buttonW)
        self.button3 = tk.Button(self, text="Dark theme", command=self.dark_theme,
                                 bg="grey", fg="white", height=buttonH, width=buttonW)
        self.space3 = tk.Label(self, text="", bg="white")
        # quit button
        self.quit = tk.Button(self, text="Exit program", command=self.close_screen,
                              bg="grey", fg="white", height=buttonH, width=buttonW)
        # Empty space
        self.space4 = tk.Label(self, text="", bg="white", pady=80)

        # Grid the widgets
        self.title.grid(row=0)
        self.space.grid(row=1)
        self.space1.grid(row=3)
        self.space2.grid(row=5)
        self.space3.grid(row=8)
        self.space4.grid(row=10)
        self.button.grid(row=2)
        self.button1.grid(row=4)
        self.button2.grid(row=6)
        self.button3.grid(row=7)
        self.quit.grid(row=9)

        self.log_screen = self.controller.get_frame("Log_screen")
    # Interface drop down menu
    # def my_menu(self, root):
    #     my_menu = tk.Menu(root)
    #     theme_menu = tk.Menu(my_menu, tearoff=False)
    #     my_menu.add_cascade(label="Interface theme", menu=theme_menu)
    #     theme_menu.add_command(label="Light theme", command=self.light_theme)
    #     theme_menu.add_command(label="Dark theme", command=self.dark_theme)
    #     return my_menu

    # theme functions

    def light_theme(self):
        # Userhub frame
        tk.Frame.config(self, bg="white")
        self.title.config(fg="white")
        self.space.config(bg="white")
        self.space1.config(bg="white")
        self.space2.config(bg="white")
        self.space3.config(bg="white")
        self.space4.config(bg="white")
        self.button.config(fg="white")
        self.button1.config(fg="white")
        self.button2.config(fg="white")
        self.button3.config(fg="white")
        self.quit.config(fg="white")


    def dark_theme(self):
        # Userhub frame
        tk.Frame.config(self, bg="black")
        self.title.config(fg="black")
        self.space.config(bg="black")
        self.space1.config(bg="black")
        self.space2.config(bg="black")
        self.space3.config(bg="black")
        self.space4.config(bg="black")
        self.button.config(fg="black")
        self.button1.config(fg="black")
        self.button2.config(fg="black")
        self.button3.config(fg="black")
        self.quit.config(fg="black")
        # Log screen
        #self.log_screen.title.config(fg="black")

    # Functions assigned to buttons to open windows
    def openreg_screen(self):
        pass

    def openlog_screen(self):

        self.controller.display_frame("Log_screen")

    # Exit button
    def close_screen(self):
        self.master.destroy()


# Main loop
def main():
    app = App()
    app.title("Vegetation simulation")
    # app.geometry("500x500")
    app.mainloop()

if __name__ == '__main__':
    main()
