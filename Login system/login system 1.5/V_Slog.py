#imports
import tkinter as tk
from tkinter import ttk
import sqlite3
import re
import os

# Getting preset integers
from V_Ssettings import *


class Log_screen:
    def __init__(self, master):
        self.master = master
        self.master.geometry(screen_size)
        self.frame = tk.Frame(self.master)

        # Defining string/text variables
        self.username1 = tk.StringVar()
        self.password1 = tk.StringVar()

        # title
        self.master.title("Login page")
        self.title = tk.Label(self.frame, text="Enter account details to proceed",
                              background="grey", foreground="white", height=titleH, width=titleW).grid(row=0, column=0)
        self.space = tk.Label(self.frame, text="").grid(row=1)

        # buttons and inputs
        self.label = tk.Label(self.frame, text="Username", height=labelH, width=labelW,
                              background="grey", foreground="white").grid(row=2)
        self.username_entry = tk.Entry(self.frame, textvariable=self.username1)
        self.username_entry.grid(row=3)
        self.space = tk.Label(self.frame, text="").grid(row=4)
        self.label = tk.Label(self.frame, text="Password", height=labelH, width=labelW,
                              background="grey", foreground="white").grid(row=5)
        self.password_entry = tk.Entry(self.frame, textvariable=self.password1)
        self.password_entry.grid(row=6)
        self.space = tk.Label(self.frame, text="").grid(row=7)

        # Button to submit details and login in
        self.button = tk.Button(self.frame, text="Login in", command=self.login_user, height=buttonH, width=buttonW,
               background="grey", foreground="white").grid(row=8)

        # allowing grid to be used
        self.frame.grid()

    def login_user(self):
        # creating string.var
        username_loginfo = self.username1.get()
        password_loginfo = self.password1.get()
        # username_entry1.delete(0, END)
        # password_entry1.delete(0, END)

        con = sqlite3.connect('User database.db')

        def data_exists():
            while True:
                # reading the database
                cursorObj = con.cursor()
                find_user1 = ("SELECT * FROM Userdetails WHERE Username = ? AND Password = ?")
                cursorObj.execute(find_user1, [(username_loginfo), (password_loginfo)])
                results = cursorObj.fetchall()
                # channeling/stopping the user though the account
                if results:

                    self.label = tk.Label(self.frame, text="Login success.\nLoading main menu...",
                                          height=labelH2, width=labelW, background="green").grid(row=9)
                    #self.frame.after(1500)
                    self.frame.after(10000, self.frame.destroy)
                    break

                else:
                    self.label = tk.Label(self.frame, text="Details incorrect",
                                          height=labelH, width=labelW, background="light blue").grid(row=9)
                    break
        data_exists()