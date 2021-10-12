"""Login screen for user to login """
"""level2"""
#imports
import tkinter as tk
from tkinter import ttk
import sqlite3


# Getting preset integers
from V_Ssettings import *
# Conneting to the main screen
from V_Smain import Main_screen



class Log_screen:
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
        self.title = tk.Label(self.frame, text="Enter account details to proceed",
                              background="grey", foreground="white", height=titleH, width=titleW).grid(row=0, column=0)
        self.space = tk.Label(self.frame, text="").grid(row=1)

        # buttons and inputs
        self.label = tk.Label(self.frame, text="Username",
                              background="grey", foreground="white", height=labelH, width=labelW,).grid(row=2)
        self.username_entry = tk.Entry(self.frame, textvariable=self.username1)
        self.username_entry.grid(row=3)
        self.space = tk.Label(self.frame, text="").grid(row=4)
        self.label = tk.Label(self.frame, text="Password",
                              background="grey", foreground="white", height=labelH, width=labelW).grid(row=5)
        self.password_entry = tk.Entry(self.frame, textvariable=self.password1)
        self.password_entry.grid(row=6)
        self.space = tk.Label(self.frame, text="").grid(row=7)

        # Button to submit details and login in
        self.button = tk.Button(self.frame, text="Login in", command=self.login_user,
                                background="grey", foreground="white", height=buttonH, width=buttonW,).grid(row=8)
        # Return back to hub
        self.label = tk.Label(self.frame, text="").grid(row=10)
        self.button = tk.Button(self.frame, text="Return", command=self.close_screen,
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
                    self.label = tk.Label(self.frame, text="Login success.\nLoading main menu...",
                                          background="green", height=labelH2, width=labelW).grid(row=9)
                    self.master.after(1500, self.openmain_screen)
                    break

                else:
                    self.label = tk.Label(self.frame, text="Details incorrect",
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