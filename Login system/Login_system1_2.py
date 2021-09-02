#imports
from tkinter import *
import tkinter as tk
logreg_root = Tk()
import sqlite3
import re
import os
from V_Smain import *


#Registration screen
def register_screen():
        global reg_root
        reg_root = Toplevel(logreg_root)
        reg_root.title("Register page")
        reg_root.geometry("250x300")
        #storing user inputs
        global username
        global password
        global username_entry
        global password_entry
        username = StringVar()
        password = StringVar()
        #title
        Label(reg_root, text="Enter details accordingly", background ="grey", foreground ="white" ,height = "3", width = "35").pack()
        Label(reg_root, text="").pack()
        #buttons and inputs
        Label(reg_root,text="Username", height="1", width="17", background ="grey", foreground ="white").pack()
        username_entry = Entry(reg_root,textvariable = username)
        username_entry.pack()
        Label(reg_root,text="Password", height="1", width="17", background ="grey", foreground ="white").pack()
        password_entry = Entry(reg_root,textvariable = password)
        password_entry.pack()
        #assistance button
        Label(reg_root, text="").pack()
        Button(reg_root,text = "Instructions", command=registration_instruction ,height="1", width="9", background ="blue", foreground ="white").place(x=86.5, y=265)
        #saving details button
        Button(reg_root, text = "Register", command= register_user, height="1", width="17", background ="grey", foreground ="white").pack()

#registation instuction screen
def registration_instruction():
        global reginstruct_root
        reginstruct_root = Toplevel(logreg_root)
        reginstruct_root.title("Registration Instructions")
        reginstruct_root.geometry("250x300")
        #Main title
        Label(reginstruct_root, text="Follow the requirements", background="grey", foreground="white", height="3",width="35").pack()
        Label(reginstruct_root, text="").pack()
        #Username
        Label(reginstruct_root,text="Username requirements", background="grey",foreground="white", height="1", width= "19").pack()
        Label(reginstruct_root, justify=tk.LEFT, text="-Username length must be 4-16\n-Username should not include space").pack()
        #Password
        Label(reginstruct_root, text="Password requirements", background="grey",foreground="white", height="1", width= "19").pack()
        Label(reginstruct_root, justify=tk.LEFT,text= "-Password length must be 4-16\n-Password must include both capital\n and lowercase letters\n-Password must include numbers\n-Password should not have any spaces").pack()




#Registeration function
def register_user():
        #creating string.var
        username_reginfo = username.get()
        password_reginfo = password.get()
        #Presence check
        if len(username_entry.get()) == 0:
                Label(reg_root, text="Username field cannot be left empty",height="1", width="27", background="light blue").place(x=27,y=200)
                return

        if len(password_entry.get()) == 0:
                Label(reg_root, text="Password field cannot be left empty",height="1", width="27", background="light blue").place(x=27,y=200)
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
                Label(reg_root, text="Username taken", height="1", width="27", background="light blue").place(x=27, y=200)
                return
        #Length check
        if (len(username_entry.get())<4 or len(username_entry.get())>16):
                Label(reg_root, text="Username length must be 4-16 ", height="1", width="27", background="light blue").place(x=27, y=200)
                return
        if (len(password_entry.get())<4 or len(password_entry.get())>16):
                Label(reg_root, text="Password length must be 4-16", height="1", width="27", background="light blue").place(x=27, y=200)
                return
        #Captial letter check
        elif not re.search("[A-Z]", password_entry.get()):
                Label(reg_root, text="Password does not include capital letter", height="1", width="32", background="light blue").place(x=27, y=200)
                return
        #Lower case check
        elif not re.search("[a-z]", password_entry.get()):
                Label(reg_root, text="Password does not include lowercase letter", height="1", width="32", background="light blue").place(x=23, y=200)
                return
        #Number check
        elif not re.search("[0-9]", password_entry.get()):
                Label(reg_root, text="Password does not include numbers", height="1", width="27",background="light blue").place(x=27, y=200)
                return
        #Space check
        elif re.search("[\s]", username_entry.get()):
                Label(reg_root, text="Username should not include space", height="1", width="27", background="light blue").place(x=27, y=200)
                return
        elif re.search("[\s]", password_entry.get()):
                Label(reg_root, text="Password should not include space", height="1", width="27", background="light blue").place(x=27, y=200)
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
                #success  message
                Label(reg_root, text="Success", height="1", width="27", background="green").place(x=27, y=200)
                reg_root.after(4000, reg_root.destroy)



#Loginscreen
def login_screen():
        global log_root
        log_root = Toplevel(logreg_root)
        log_root.title("Login page")
        log_root.geometry("250x300")
        #title
        Label(log_root, text="Enter account information", background="grey", foreground="white", height="3", width="35").pack()
        Label(log_root, text="").pack()
        #buttons and inputs
        global username1
        global password1
        global username_entry1
        global password_entry1
        username1 = StringVar()
        password1 = StringVar()

        Label(log_root, text="Username", height="1", width="17", background="grey", foreground="white").pack()
        username_entry1 = Entry(log_root, textvariable= username1 )
        username_entry1.pack()
        Label(log_root, text="Password", height="1", width="17", background="grey", foreground="white").pack()
        password_entry1 = Entry(log_root, textvariable= password1, show="*")
        password_entry1.pack()

        #Button to submit user details
        Label(log_root, text="").pack()
        Button(log_root, text="Login in", command = login_user, height="1", width="17", background="grey", foreground="white").pack()



#Login function
def login_user():
        #creating string.var
        username_loginfo = username1.get()
        password_loginfo = password1.get()
        username_entry1.delete(0, END)
        password_entry1.delete(0, END)

        con = sqlite3.connect('User database.db')


        def data_exists():
                while True:
                        #reading the database
                        cursorObj = con.cursor()
                        find_user1 = ("SELECT * FROM Userdetails WHERE Username = ? AND Password = ?")
                        cursorObj.execute(find_user1, [(username_loginfo),(password_loginfo)])
                        results = cursorObj.fetchall()
                        #channeling/stopping the user though the account
                        if results:
                                Label(log_root, text="Login success", command = main_screen() , height="1", width="19", background="green").place(x=56,y=200)
                                log_root.after(3000,log_root.destroy)
                                break
                        else:
                                Label(log_root, text="Details incorrect", height="1", width="19", background="light blue").place(x=56, y=200)
                                break
        data_exists()








#main menu
def main_screen():
        main_root = Toplevel(logreg_root)
        main_root.title("Main menu")
        main_root.geometry("500x600")
        #title
        Label(main_root, text="Vegetation simulation\nmain menu", background="grey", foreground="white", height="2", width="35").pack()
        #buttons
        Label(main_root, text="").pack()
        Button(main_root, text="Load/create save", command = loadsavescreen,height = "1", width = "15",background ="grey", foreground ="white").pack()
        Label(main_root, text="").pack()

        Button(main_root, text="Settings", height = "1", width = "15",background ="grey", foreground ="white").pack()
        Label(main_root, text="").pack()

        Button(main_root, text="Instruction", height = "1", width = "15",background ="grey", foreground ="white").pack()
        Label(main_root, text="").pack()

        Button(main_root, text="Gallery", height = "1", width = "15",background ="grey", foreground ="white").pack()
        Label(main_root, text="").pack()

        Button(main_root, text="Exit",command = main_root.destroy, height = "1", width = "15",background ="grey", foreground ="white").pack()
#Screen for load/create saves
def loadsavescreen():
        global loadsavescreen
        loadsave_root = Toplevel(logreg_root)
        loadsave_root.title("Load/create saves")
        loadsave_root.geometry("250x300")
        #title
        Label(loadsave_root, text="Select option", background="grey", foreground="white", height="3", width="35").pack()
        Label(loadsave_root, text="").pack()
        #button

        #Button(loadsave_root, text="Load saves", height="1", width="17", background="grey", foreground="white").pack()
        #Label(loadsave_root, text="").pack()

        Button(loadsave_root, text="Create save", command = opensim(), height="1", width="17", background="grey", foreground="white").pack()
        Label(loadsave_root, text="").pack()

        Button(loadsave_root, text="Return to main menu", command= loadsave_root.destroy, height="1", width="17", background="grey", foreground="white").pack()

#linking to the Main simulation file.
def opensim():
        os.system('V_Smain.py')



#Registation and login in screen
def logreg_screen():
        global logreg_root
        logreg_root.geometry("500x600")
        logreg_root.title("Vegetation simulation")
        Label(text = "Vegetation simulation\nuser portal", background ="grey", foreground ="white" ,height = "2", width = "35").pack()
        #buttons
        Label(text="").pack()
        Button(text = "Login", command = login_screen, height = "1", width = "15",background ="grey", foreground ="white").pack()

        Label(text= "").pack()
        Button(text = "Register", command = register_screen, height = "1", width = "15", background ="grey", foreground ="white").pack()

        Label(text="").pack()
        Button(text="Exit program", command= logreg_root.destroy, height="1", width="15", background ="grey", foreground ="white").pack()

        logreg_root.mainloop()

logreg_screen()


