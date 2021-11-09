"""Initial/base screen and TopRoot"""
"""level1"""
# imports
import tkinter as tk
from tkinter import ttk

# connecting other files
from V_Saccount import Log_screen, Reg_screen, RegInstruction_screen
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

        # Attribute to hold the list of names of frames
        self.frames = {}
        # Creating classes and creating instances
        for F in (Userhub_screen, Log_screen, Reg_screen, RegInstruction_screen, Main_screen):
            frame_name = F.__name__
            frame = F(master=base_frame, controller=self)
            self.frames[frame_name] = frame
            # Positioning the frame so that the north, south, east and west corners match up together to
            # stack on each other
            frame.grid(row=0, column=0, sticky="nsew")

        # Displaying the user hub screen as the default initial screen
        self.display_frame("Userhub_screen")

    # Getting references to other frames' widgets
    def get_frame(self, frame_name):
        return self.frames[frame_name]

    # Raises the frame from the list to the front
    def display_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()


class Userhub_screen(tk.Frame):
    # Base window or TopRoot
    def __init__(self, master, controller):
        # Class attributes
        self.controller = controller
        tk.Frame.__init__(self, master)

        # Background
        self.light_bg = tk.PhotoImage(file="Image/Light bg.png")
        self.dark_bg = tk.PhotoImage(file="Image/Dark bg.png")
        self.bg = tk.Label(self, image=self.light_bg)
        # Title
        self.title = tk.Label(self, text="Vegetation Simulation User Portal",
                              height=titleH, width=titleW)
        # buttons
        self.space = tk.Label(self, text="")
        self.button = tk.Button(self, text="Login", command=self.openlog_screen,
                                height=buttonH, width=buttonW)
        self.space1 = tk.Label(self, text="")
        self.button1 = tk.Button(self, text="Register", command=self.openreg_screen,
                                 height=buttonH, width=buttonW)
        self.space2 = tk.Label(self, text="")
        self.button2 = tk.Button(self, text="Light theme", command=self.light_theme,
                                 height=buttonH, width=buttonW)
        self.button3 = tk.Button(self, text="Dark theme", command=self.dark_theme,
                                 height=buttonH, width=buttonW)
        self.space3 = tk.Label(self, text="")
        # quit button
        self.quit = tk.Button(self, text="Exit program", command=self.close_screen,
                              height=buttonH, width=buttonW)
        # Empty space
        self.space4 = tk.Label(self, text="", pady=80)
        # Giving the widgets position via grid
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
        # Placing the label holding the image
        self.bg.place(x=0, y=0, relwidth=1, relheight=1)
        # Applying colour attributes to widgets and the frame
        self.colour_theme()

    # Applying the default colours to the frame
    def colour_theme(self):
        # Widgets
        self.bg.config(image=self.light_bg)
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
        self.quit.config(bg="grey", fg="white")
    # theme change functions
    def light_theme(self):
        # Getting references to other classes
        self.log = self.controller.get_frame("Log_screen")
        self.reg = self.controller.get_frame("Reg_screen")
        self.reginstruction = self.controller.get_frame("RegInstruction_screen")
        self.main = self.controller.get_frame("Main_screen")
        # Userhub frame
        self.bg.config(image=self.light_bg)
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
        self.quit.config(bg="grey", fg="white")
        # Log screen
        self.log.bg.config(image=self.light_bg)
        self.log.title.config(fg="white")
        self.log.space.config(bg="white")
        self.log.space1.config(bg="white")
        self.log.space2.config(bg="white")
        self.log.space3.config(bg="white")
        self.log.label.config(fg="white")
        self.log.label1.config(fg="white")
        self.log.button.config(fg="white")
        self.log.quit.config(fg="white")
        # Registration screen
        self.reg.bg.config(image=self.light_bg)
        self.reg.title.config(fg="white")
        self.reg.space.config(bg="white")
        self.reg.space1.config(bg="white")
        self.reg.space2.config(bg="white")
        self.reg.space3.config(bg="white")
        self.reg.space4.config(bg="white")
        self.reg.label.config(fg="white")
        self.reg.label1.config(fg="white")
        self.reg.submit_button.config(fg="white")
        self.reg.assist_button.config(fg="white")
        self.reg.return_button.config(fg="white")
        # Registration instruction screen
        self.reginstruction.bg.config(image=self.light_bg)
        self.reginstruction.title.config(fg="white")
        self.reginstruction.space.config(bg="white")
        self.reginstruction.space1.config(bg="white")
        self.reginstruction.space2.config(bg="white")
        self.reginstruction.label.config(fg="white")
        self.reginstruction.label1.config(fg="white")
        self.reginstruction.paragraph.config(bg="white", fg="black")
        self.reginstruction.paragraph1.config(bg="white", fg="black")
        self.reginstruction.return_button.config(fg="white")
        # Main screen
        self.main.bg.config(image=self.light_bg)
        self.main.title.config(fg="white")
        self.main.space.config(bg="white")
        self.main.space1.config(bg="white")
        self.main.space2.config(bg="white")
        self.main.space3.config(bg="white")
        self.main.space4.config(bg="white")
        self.main.button.config(fg="white")
        self.main.button1.config(fg="white")
        self.main.button2.config(fg="white")
        self.main.button3.config(fg="white")
        self.main.return_button.config(fg="white")

    def dark_theme(self):
        # Getting references to other classes
        self.log = self.controller.get_frame("Log_screen")
        self.reg = self.controller.get_frame("Reg_screen")
        self.reginstruction = self.controller.get_frame("RegInstruction_screen")
        self.main = self.controller.get_frame("Main_screen")
        # Userhub frame
        self.bg.config(image=self.dark_bg)
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
        self.log.bg.config(image=self.dark_bg)
        self.log.title.config(fg="black")
        self.log.space.config(bg="black")
        self.log.space1.config(bg="black")
        self.log.space2.config(bg="black")
        self.log.space3.config(bg="black")
        self.log.label.config(fg="black")
        self.log.label1.config(fg="black")
        self.log.button.config(fg="black")
        self.log.quit.config(fg="black")
        # Registration screen
        self.reg.bg.config(image=self.dark_bg)
        self.reg.title.config(fg="black")
        self.reg.space.config(bg="black")
        self.reg.space1.config(bg="black")
        self.reg.space2.config(bg="black")
        self.reg.space3.config(bg="black")
        self.reg.space4.config(bg="black")
        self.reg.label.config(fg="black")
        self.reg.label1.config(fg="black")
        self.reg.submit_button.config(fg="black")
        self.reg.assist_button.config(fg="black")
        self.reg.return_button.config(fg="black")
        # Registration instruction screen
        self.reginstruction.bg.config(image=self.dark_bg)
        self.reginstruction.title.config(fg="black")
        self.reginstruction.space.config(bg="black")
        self.reginstruction.space1.config(bg="black")
        self.reginstruction.space2.config(bg="black")
        self.reginstruction.label.config(fg="black")
        self.reginstruction.label1.config(fg="black")
        self.reginstruction.paragraph.config(bg="black", fg="white")
        self.reginstruction.paragraph1.config(bg="black", fg="white")
        self.reginstruction.return_button.config(fg="black")
        # Main screen
        self.main.bg.config(image=self.dark_bg)
        self.main.title.config(fg="black")
        self.main.space.config(bg="black")
        self.main.space1.config(bg="black")
        self.main.space2.config(bg="black")
        self.main.space3.config(bg="black")
        self.main.space4.config(bg="black")
        self.main.button.config(fg="black")
        self.main.button1.config(fg="black")
        self.main.button2.config(fg="black")
        self.main.button3.config(fg="black")
        self.main.return_button.config(fg="black")

    # Functions assigned to buttons switch frames
    def openlog_screen(self):
        self.controller.display_frame("Log_screen")

    def openreg_screen(self):
        self.controller.display_frame("Reg_screen")
    # Exit button
    def close_screen(self):
        self.master.destroy()

# Main loop
def main():
    app = App()
    app.title("Vegetation simulation")
    app.geometry("500x400")
    app.mainloop()

if __name__ == '__main__':
    main()
