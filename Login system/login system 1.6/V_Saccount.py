"""Login and registration screens for the user to interact with the database"""
"""level2"""
#imports
import tkinter as tk
from tkinter import ttk
import sqlite3
import re


# Getting preset integers
from V_Ssettings import *
# Conneting to the main screen
from V_Sinstruction1 import RegInstruction_screen
from V_Smain import Main_screen




class Log_screen():
    def __init__(self, master):
        self.master = master
        self.master.geometry(screen_size)
        self.frame = tk.Frame(self.master)
        # allowing grid to be used
        self.frame.grid()

        # Defining string/text variables
        self.username1 = tk.StringVar()
        self.password1 = tk.StringVar()

        # title
        self.master.title("Login page")
        self.title = tk.Label(master, text="Enter account details to proceed",
                              background="grey", foreground="white", height=titleH, width=titleW).grid(row=0, column=0)
        self.space = tk.Label(master, text="").grid(row=1)

        # buttons and inputs
        self.label = tk.Label(master, text="Username",
                              background="grey", foreground="white", height=labelH, width=labelW,).grid(row=2)
        self.username_entry = tk.Entry(master, textvariable=self.username1)
        self.username_entry.grid(row=3)
        self.space = tk.Label(master, text="").grid(row=4)
        self.label = tk.Label(master, text="Password",
                              background="grey", foreground="white", height=labelH, width=labelW).grid(row=5)
        self.password_entry = tk.Entry(master, textvariable=self.password1)
        self.password_entry.grid(row=6)
        self.space = tk.Label(master, text="").grid(row=7)

        # Button to submit details and login in
        self.button = tk.Button(master, text="Login in", command=self.login_user,
                                background="grey", foreground="white", height=buttonH, width=buttonW,).grid(row=8)
        # Return back to hub
        self.label = tk.Label(master, text="").grid(row=10)
        self.button = tk.Button(master, text="Return", command=self.close_screen,
                                background="grey", foreground="white", height=buttonH, width=buttonW).grid(row=11)

    def login_user(self):
        # creating string.var
        username_loginfo = self.username1.get()
        password_loginfo = self.password1.get()

        con = sqlite3.connect('User database.db')

        def data_exists():
            while True:
                # reading the database
                cursorObj = con.cursor()
                find_user1 = ("SELECT * FROM Userdetails WHERE Username = ? AND Password = ?")
                cursorObj.execute(find_user1, [(username_loginfo), (password_loginfo)])
                results = cursorObj.fetchall()
                # Deciding whether the user should proceed or not
                if results:
                    self.label = tk.Label(self.master, text="Login success.\nLoading main menu...",
                                          background="green", height=labelH2, width=labelW).grid(row=9)
                    self.master.after(1500, self.openmain_screen)
                    break

                else:
                    self.label = tk.Label(self.master, text="Details incorrect",
                                          background="light blue", height=labelH2, width=labelW).grid(row=9)
                    break
        data_exists()

    # Function for opening the main screen
    def openmain_screen(self):
        self.openmain_screen = tk.Toplevel(self.master)
        self.app = Main_screen(self.openmain_screen)

    # Closing function
    def close_screen(self):
        self.master.destroy()

# Registration screen
class Reg_screen():

    def __init__(self, master):
        self.master = master
        self.master.geometry(screen_size)
        self.frame = tk.Frame(self.master)
        self.frame.grid()


        # Defining string/text variables
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        # title
        self.master.title("Registration page")
        self.title = tk.Label(self.frame, text="Enter details accordingly",
                              background="grey", foreground="white", height=titleH, width=titleW).grid(row=0, column=0)
        self.space = tk.Label(self.frame, text="").grid(row=1)

        # buttons and inputs
        self.label = tk.Label(self.frame, text="Username",
                              background="grey", foreground="white", height=labelH, width=labelW).grid(row=2)
        self.username_entry = tk.Entry(self.frame, textvariable=self.username)
        self.username_entry.grid(row=3)
        self.space = tk.Label(self.frame, text="").grid(row=4)
        self.label = tk.Label(self.frame, text="Password",
                              background="grey", foreground="white", height=labelH, width=labelW).grid(row=5)
        self.password_entry = tk.Entry(self.frame, textvariable=self.password)
        self.password_entry.grid(row=6)
        self.space = tk.Label(self.frame, text="").grid(row=7)
        # submit details button
        self.button = tk.Button(self.frame, text="Register", command=self.register_user,
                                background="grey", foreground="white", height=buttonH, width=buttonW,).grid(row=8)
        # assistance button
        self.label = tk.Label(self.frame, text="").grid(row=9)
        self.button = tk.Button(self.frame, text="Instructions", command=self.openinstruction,
                                      background="blue", foreground="white", height=buttonH, width=buttonW).grid(row=10)
        # Return back to hub
        self.label = tk.Label(self.frame, text="").grid(row=12)
        self.button = tk.Button(self.frame, text="Return", command=self.close_screen,
                                background="grey", foreground="white", height=buttonH, width=buttonW).grid(row=13)
        self.frame.grid()


    # Functions for validating input and submitting to the database
    def register_user(self):
        # creating string.var
        username_reginfo = self.username.get()
        password_reginfo = self.password.get()
        # Presence check
        if len(self.username_entry.get()) == 0:
            self.label = tk.Label(self.frame, text="Username field cannot be left empty",
                                  height=labelH2, width=labelW2, background="light blue").grid(row=11, rowspan=2)
            return

        if len(self.password_entry.get()) == 0:
            self.lable = tk.Label(self.frame, text="Password field cannot be left empty",
                                  height=labelH2, width=labelW2, background="light blue").grid(row=11, rowspan=2)
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
            self.label = tk.Label(self.frame, text="Username taken",
                                  height=labelH2, width=labelW2, background="light blue").grid(row=11, rowspan=2)
            return
        # Length check
        if (len(self.username_entry.get()) < 4 or len(self.username_entry.get()) > 16):
            self.label = tk.Label(self.frame, text="Username length must be 4-16 ",
                                  height=labelH2, width=labelW2, background="light blue").grid(row=11, rowspan=2)
            return
        if (len(self.password_entry.get()) < 4 or len(self.password_entry.get()) > 16):
            self.label = tk.Label(self.frame, text="Password length must be 4-16",
                                  height=labelH2, width=labelW2, background="light blue").grid(row=11, rowspan=2)
            return
        # Capital letter check
        elif not re.search("[A-Z]", self.password_entry.get()):
            self.label = tk.Label(self.frame, text="Password does not include\n capital letter",
                                  height=labelH2, width=labelW2, background="light blue").grid(row=11, rowspan=2)
            return
        # Lower case check
        elif not re.search("[a-z]", self.password_entry.get()):
            self.label = tk.Label(self.frame, text="Password does not include\n lowercase letter",
                                  height=labelH2, width=labelW2, background="light blue").grid(row=11, rowspan=2)
            return
        # Number check
        elif not re.search("[0-9]", self.password_entry.get()):
            self.label = tk.Label(self.frame, text="Password does not include numbers",
                                  height=labelH2, width=labelW2, background="light blue").grid(row=11, rowspan=2)
            return
        # Space check
        elif re.search("[\s]", self.username_entry.get()):
            self.label = tk.Label(self.frame, text="Username should not include space",
                                  height=labelH2, width=labelW2, background="light blue").grid(row=11, rowspan=2)
            return
        elif re.search("[\s]", self.password_entry.get()):
            self.label = tk.Label(self.frame, text="Password should not include space",
                                  height=labelH2, width=labelW2, background="light blue").grid(row=11, rowspan=2)
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
            self.sucesslabel = tk.Label(self.frame, text="Success",
                                        height=labelH2, width=labelW2, background="green").grid(row=11)
            self.frame.after(4000, self.close_screen)

    # Function for opening instruction page
    def openinstruction(self):
        self.openinstruction = tk.Toplevel(self.master)
        self.app = RegInstruction_screen(self.openinstruction)

    # Closing function
    def close_screen(self):
        self.master.destroy()
