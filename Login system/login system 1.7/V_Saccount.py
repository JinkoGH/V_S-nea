"""Login and registration screens for the user to interact with the database"""
"""level2"""
# imports
import tkinter as tk
from tkinter import ttk
import sqlite3
import re

# Getting preset integers
from V_Ssettings import *
# Conneting to the main screen
from V_Smain import Main_screen


class Log_screen(tk.Frame):
    def __init__(self, master, controller):
        self.controller = controller
        tk.Frame.__init__(self, master)
        # Defining string/text variables
        self.username1 = tk.StringVar()
        self.password1 = tk.StringVar()

        # Background
        self.light_bg = tk.PhotoImage(file="Image/Light bg.png")
        # self.dark_bg = tk.PhotoImage(file="Image/Dark bg.png")
        self.bg = tk.Label(self, image=self.light_bg)
        # title
        self.title = tk.Label(self, text="Enter account details to proceed",
                              height=titleH, width=titleW)
        self.space = tk.Label(self, text="")
        # buttons and inputs
        self.label = tk.Label(self, text="Username",
                              height=labelH, width=labelW, )
        self.username_entry = tk.Entry(self, textvariable=self.username1)
        self.space1 = tk.Label(self, text="")
        self.label1 = tk.Label(self, text="Password",
                               height=labelH, width=labelW)
        self.password_entry = tk.Entry(self, textvariable=self.password1)
        self.password_entry.grid(row=6)
        self.space2 = tk.Label(self, text="")

        # Button to submit details and login in
        self.button = tk.Button(self, text="Login in", command=self.login_user,
                                height=buttonH, width=buttonW)
        # Return back to hub
        self.space3 = tk.Label(self, text="")
        self.quit = tk.Button(self, text="Return", command=self.return_screen,
                              height=buttonH, width=buttonW)
        # Applying colour attributes to widgets and the frame
        self.colour_theme()
        # Giving the widgets position via grid
        self.title.grid(row=0)
        self.space.grid(row=1)
        self.label.grid(row=2)
        self.username_entry.grid(row=3)
        self.space1.grid(row=4)
        self.label1.grid(row=5)
        self.space2.grid(row=7)
        self.button.grid(row=8)
        self.space3.grid(row=10)
        self.quit.grid(row=11)
        # Placing the label holding the image
        self.bg.place(x=0, y=0, relwidth=1, relheight=1)

    # Applying the default colours to the frame
    def colour_theme(self):
        # Local window
        tk.Frame.config(self, bg="white")
        self.title.config(bg="grey", fg="white")
        self.space.config(bg="white")
        self.space1.config(bg="white")
        self.space2.config(bg="white")
        self.space3.config(bg="white")
        self.label.config(bg="grey", fg="white")
        self.label1.config(bg="grey", fg="white")
        self.button.config(bg="grey", fg="white")
        self.quit.config(bg="grey", fg="white")

    def login_user(self):
        # creating string.var
        username_loginfo = self.username1.get()
        password_loginfo = self.password1.get()

        con = sqlite3.connect('User database.db')

        #
        def data_exists():
            while True:
                # Reading the database
                cursorObj = con.cursor()
                find_user1 = ("SELECT * FROM Userdetails WHERE Username = ? AND Password = ?")
                cursorObj.execute(find_user1, [(username_loginfo), (password_loginfo)])
                results = cursorObj.fetchall()
                # Validation process and choosing the user should proceed or not
                if results:
                    success_message = tk.Label(self, text="Login success.\nLoading main menu...",
                                               bg="green", height=labelH2, width=labelW)
                    success_message.grid(row=9)
                    self.master.after(1500, self.openmain_screen)
                    break

                else:
                    fail_message = tk.Label(self, text="Details incorrect",
                                            bg="light blue", height=labelH2, width=labelW)
                    fail_message.grid(row=9)
                    break

        # Running the while loop when login_user function is called
        data_exists()

    # Function for opening the main screen
    def openmain_screen(self):
        self.controller.display_frame("Main_screen")

    # Closing function
    def return_screen(self):
        self.controller.display_frame("Userhub_screen")


# Registration screen
class Reg_screen(tk.Frame):

    def __init__(self, master, controller):
        # Class attributes
        self.controller = controller
        tk.Frame.__init__(self, master)
        # Defining string/text variables
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        # Background
        self.light_bg = tk.PhotoImage(file="Image/Light bg.png")
        # self.dark_bg = tk.PhotoImage(file="Image/Dark bg.png")
        self.bg = tk.Label(self, image=self.light_bg)
        # title
        self.title = tk.Label(self, text="Enter details accordingly",
                              height=titleH, width=titleW)
        self.space = tk.Label(self, text="")
        # buttons and inputs
        self.label = tk.Label(self, text="Username",
                              height=labelH, width=labelW)
        self.username_entry = tk.Entry(self, textvariable=self.username)
        self.space1 = tk.Label(self, text="")
        self.label1 = tk.Label(self, text="Password",
                               height=labelH, width=labelW)
        self.password_entry = tk.Entry(self, textvariable=self.password)
        self.space2 = tk.Label(self, text="")
        # submit details button
        self.submit_button = tk.Button(self, text="Register", command=self.register_user,
                                       height=buttonH, width=buttonW)
        # assistance button
        self.space3 = tk.Label(self, text="")
        self.assist_button = tk.Button(self, text="Instructions", command=self.openinstruction,
                                       height=buttonH, width=buttonW)
        # Return back to hub
        self.space4 = tk.Label(self, text="")
        self.return_button = tk.Button(self, text="Return", command=self.return_screen,
                                       height=buttonH, width=buttonW)
        # Applying colour attributes to widgets and the frame
        self.colour_theme()
        # Giving the widgets position via grid
        self.title.grid(row=0)
        self.space.grid(row=1)
        self.space1.grid(row=4)
        self.space2.grid(row=7)
        self.space3.grid(row=9)
        self.space4.grid(row=12)
        self.label.grid(row=2)
        self.label1.grid(row=5)
        self.username_entry.grid(row=3)
        self.password_entry.grid(row=6)
        self.submit_button.grid(row=8)
        self.assist_button.grid(row=10)
        self.return_button.grid(row=13)
        # Placing the label holding the image
        self.bg.place(x=0, y=0, relwidth=1, relheight=1)

    # Functions for validating input and submitting to the database
    def register_user(self):
        # creating string.var
        username_reginfo = self.username.get()
        password_reginfo = self.password.get()
        # Presence check
        if len(self.username_entry.get()) == 0:
            self.error = tk.Label(self, text="Username field cannot be left empty",
                                  bg="light blue", height=labelH2, width=labelW2)
            self.error.grid(row=11)
            return

        if len(self.password_entry.get()) == 0:
            self.error1 = tk.Label(self, text="Password field cannot be left empty",
                                   bg="light blue", height=labelH2, width=labelW2)
            self.error1.grid(row=11)
            return
        # connecting to the database
        con = sqlite3.connect('User database.db')
        # Username duplication check
        cursorObj = con.cursor()
        find_user2 = ("SELECT * FROM Userdetails WHERE Username = ?")
        cursorObj.execute(find_user2, [(username_reginfo)])
        results = cursorObj.fetchall()
        # channeling/stopping the user though the account
        if results:
            self.error2 = tk.Label(self, text="Username taken",
                                   bg="light blue", height=labelH2, width=labelW2)
            self.error2.grid(row=11)
            return
        # Length check
        if (len(self.username_entry.get()) < 4 or len(self.username_entry.get()) > 16):
            self.error3 = tk.Label(self, text="Username length must be 4-16 ",
                                   bg="light blue", height=labelH2, width=labelW2)
            self.error3.grid(row=11)
            return
        if (len(self.password_entry.get()) < 4 or len(self.password_entry.get()) > 16):
            self.error4 = tk.Label(self, text="Password length must be 4-16",
                                   bg="light blue", height=labelH2, width=labelW2)
            self.error4.grid(row=11)
            return
        # Capital letter check
        elif not re.search("[A-Z]", self.password_entry.get()):
            self.error5 = tk.Label(self, text="Password does not include\n capital letter",
                                   bg="light blue", height=labelH2, width=labelW2)
            self.error5.grid(row=11)
            return
        # Lower case check
        elif not re.search("[a-z]", self.password_entry.get()):
            self.error6 = tk.Label(self, text="Password does not include\n lowercase letter",
                                   bg="light blue", height=labelH2, width=labelW2)
            self.error6.grid(row=11)
            return
        # Number check
        elif not re.search("[0-9]", self.password_entry.get()):
            self.error7 = tk.Label(self, text="Password does not include numbers",
                                   bg="light blue", height=labelH2, width=labelW2)
            self.error7.grid(row=11)
            return
        # Space check
        elif re.search("[\s]", self.username_entry.get()):
            self.error8 = tk.Label(self, text="Username should not include space",
                                   bg="light blue", height=labelH2, width=labelW2)
            self.error8.grid(row=11)
            return
        elif re.search("[\s]", self.password_entry.get()):
            self.error9 = tk.Label(self, text="Password should not include space",
                                   bg="light blue", height=labelH2, width=labelW2)
            self.error9.grid(row=11)
            return
        else:
            # Inserting data into the database

            con = sqlite3.connect('User database.db')
            entities = username_reginfo, password_reginfo

            def data_insert(con, entities):
                cursorObj = con.cursor()
                cursorObj.execute('INSERT INTO Userdetails(Username, Password) VALUES(?, ?)', entities)
                con.commit()

            data_insert(con, entities)
            # success message
            self.sucess_label = tk.Label(self, text="Success",
                                         bg="green", height=labelH2, width=labelW2)

        # Giving the message labels position via grid
        self.error.grid(row=11)
        self.error1.grid(row=11)
        self.error2.grid(row=11)
        self.error3.grid(row=11)
        self.error4.grid(row=11)
        self.error5.grid(row=11)
        self.error6.grid(row=11)
        self.error7.grid(row=11)
        self.error8.grid(row=11)
        self.error9.grid(row=11)

    # Applying the default colours to the frame
    def colour_theme(self):
        # Widgets
        self.title.config(bg="grey", fg="white")
        self.space.config(bg="white")
        self.space1.config(bg="white")
        self.space2.config(bg="white")
        self.space3.config(bg="white")
        self.space4.config(bg="white")
        self.label.config(bg="grey", fg="white")
        self.label1.config(bg="grey", fg="white")
        self.submit_button.config(bg="grey", fg="white")
        self.assist_button.config(bg="grey", fg="white")
        self.return_button.config(bg="grey", fg="white")



    # Function for opening instruction page
    def openinstruction(self):
        self.controller.display_frame("RegInstruction_screen")

    # Closing function
    def return_screen(self):
        self.controller.display_frame("Userhub_screen")


class RegInstruction_screen(tk.Frame):
    def __init__(self, master, controller):
        # Class attributes
        self.controller = controller
        tk.Frame.__init__(self, master)

        # Background
        self.light_bg = tk.PhotoImage(file="Image/Light bg.png")
        # self.dark_bg = tk.PhotoImage(file="Image/Dark bg.png")
        self.bg = tk.Label(self, image=self.light_bg)
        # Main title
        self.title = tk.Label(self, text="Follow the requirements",
                              height=titleH, width=titleW)
        self.space = tk.Label(self, text="")
        # Username
        self.label = tk.Label(self, text="Username requirements",
                              height=labelH, width=labelW2)
        self.paragraph = tk.Label(self, justify=tk.LEFT,
                                  text="-Username length must be 4-16\n-Username should not include space")
        self.space1 = tk.Label(self, text="")
        # Password
        self.label1 = tk.Label(self, text="Password requirements",
                               height=labelH, width=labelW2)
        self.paragraph1 = tk.Label(self, justify=tk.LEFT,
                                   text="-Password length must be 4-16\n-Password must include both capital\n and "
                                        "lowercase letters\n-Password must include numbers\n-Password should not have "
                                        "any spaces")
        self.space2 = tk.Label(self, text="")
        self.return_button = tk.Button(self, text="Return", command=self.return_screen,
                                       height=buttonH, width=buttonW)

        # Applying colour attributes to widgets and the frame
        self.colour_theme()
        # Giving the widgets position via grid
        self.title.grid(row=0)
        self.space.grid(row=1)
        self.space1.grid(row=4)
        self.space2.grid(row=7)
        self.label.grid(row=2)
        self.label1.grid(row=5)
        self.paragraph.grid(row=3)
        self.paragraph1.grid(row=6)
        self.return_button.grid(row=8)
        # Placing the label holding the image
        self.bg.place(x=0, y=0, relwidth=1, relheight=1)

    def colour_theme(self):
        tk.Frame.config(self, bg="white")
        self.title.config(bg="grey", fg="white")
        self.space.config(bg="white")
        self.space1.config(bg="white")
        self.space2.config(bg="white")
        self.label.config(bg="grey", fg="white")
        self.label1.config(bg="grey", fg="white")
        self.paragraph.config(bg="white", fg="black")
        self.paragraph1.config(bg="white", fg="black")
        self.return_button.config(bg="grey", fg="white")

    # Exit button
    def return_screen(self):
        self.controller.display_frame("Reg_screen")

