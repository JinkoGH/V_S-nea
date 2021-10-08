#imports
import tkinter as tk
#from login_system_settings import Custom
from tkinter import ttk
import sqlite3
import os

screen_size = ("400x300")

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
        self.openreg_screen = tk.Toplevel(self.master)
        self.app = reg_screen(self.openreg_screen)
        
    def openlog_screen(self):
        pass

    # Exit button
    def close_screen(self):
        self.master.destroy()

global username

class reg_screen:
   
    def __init__(self, master):
        self.master = master
        self.master.geometry(screen_size)
        self.frame = tk.Frame(self.master)

        # Defining string/text variables
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        
      
        # title
        self.master.title("Registration page")
        self.title = tk.Label(self.frame, text="Enter details accordingly", background ="grey", foreground ="white",
                              height = "3", width = "35").pack()
        self.space = tk.Label(self.frame, text="").pack()

        #buttons and inputs
        self.label = tk.Label(self.frame, text="Username", height="1", width="17",
                              background ="grey", foreground ="white").pack()
        self.username_entry = tk.Entry(self.frame, textvariable = self.username)
        self.username_entry.pack()
        self.label = tk.Label(self.frame, text="Password", height="1", width="17",
                              background ="grey", foreground ="white").pack()
        self.password_entry = tk.Entry(self.frame, textvariable = self.password)
        self.password_entry.pack()
        self.space = tk.Label(self.frame, text="").pack()
        
        #submit details button
        self.button = tk.Button(self.frame, text = "Register", height="1", width="17",
                                background ="grey", foreground ="white").pack()

        #assistance button
        self.label = tk.Label(self.frame, text="").pack()
        self.assistbutton = tk.Button(self.frame, text = "Instructions", height="1", width="9",
                                      background ="blue", foreground ="white").pack()

        self.frame.pack()
        
    # Functions for validating input and submiting to the database
    def register_user():
        #creating string.var
        username_reginfo = self.username.get()
        password_reginfo = self.password.get()
        #Presence check
        if len(username_entry.get()) == 0:
                self.label = Label(self.frame, text="Username field cannot be left empty",height="1", width="27", background="light blue").pack()
                return

        if len(password_entry.get()) == 0:
                self.lable = Label(self.frame, text="Password field cannot be left empty",height="1", width="27", background="light blue").place(x=27,y=200)
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
                self.label = Label(self.frame, text="Username taken", height="1", width="27", background="light blue").place(x=27, y=200)
                return
        #Length check
        if (len(username_entry.get())<4 or len(username_entry.get())>16):
                self.label = Label(self.frame, text="Username length must be 4-16 ", height="1", width="27", background="light blue").pack()
                return
        if (len(password_entry.get())<4 or len(password_entry.get())>16):
                self.label = Label(self.frame, text="Password length must be 4-16", height="1", width="27", background="light blue").pack()
                return
        #Captial letter check
        elif not re.search("[A-Z]", password_entry.get()):
                self.label = Label(self.frame, text="Password does not include capital letter", height="1", width="32", background="light blue").place(x=27, y=200)
                return
        #Lower case check
        elif not re.search("[a-z]", password_entry.get()):
                self.label = Label(self.frame, text="Password does not include lowercase letter", height="1", width="32", background="light blue").place(x=23, y=200)
                return
        #Number check
        elif not re.search("[0-9]", password_entry.get()):
                self.label = Label(self.frame, text="Password does not include numbers", height="1", width="27",background="light blue").place(x=27, y=200)
                return
        #Space check
        elif re.search("[\s]", username_entry.get()):
                self.label = Label(self.frame, text="Username should not include space", height="1", width="27", background="light blue").place(x=27, y=200)
                return
        elif re.search("[\s]", password_entry.get()):
                self.label = Label(self.frame, text="Password should not include space", height="1", width="27", background="light blue").place(x=27, y=200)
                return
        else:
                #Iserting data into the database

                con = sqlite3.connect('User database.db')
                entities = username_reginfo, password_reginfo

                def data_insert(con, entities):
                        cursorObj = con.cursor()
                        cursorObj.execute('INSERT INTO Userdetails(Username, Password) VALUES(?, ?)', entities)
                        con.commit()

                data_insert(con, entities)
                #successmessage
                self.sucesslabel = Label(self.frame, text="Success", height="1", width="27", background="green").pack()
                self.frame.after(4000, self.frame.destroy)

    # Exit button
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




        




