from tkinter import *
import os

logreg_root = Tk()

#database define
import sqlite3


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

        #saving details button
        Label(reg_root, text="").pack()
        Button(reg_root, text = "Register", command= register_user, height="1", width="17", background ="grey", foreground ="white").pack()
        

#Registeration function
def register_user():
        #creating string.var
        username_info = username.get()
        password_info = password.get()
        #error messages when input fields are empty
        if len(username_entry.get()) == 0:
                Label(reg_root, text="Username field cannot be left empty",height="1", width="27", background="light blue").place(x=27,y=200)
                return

        if len(password_entry.get()) == 0:
                Label(reg_root, text="Password field cannot be left empty",height="1", width="27", background="light blue").place(x=27,y=200)
                return
        else:
                #create textfile
                file=open(username_info, "w")
                file.write(username_info+"\n")
                file.write(password_info)
                file.close()
                #clearing temp user inputs
                username_entry.delete(0, END)
                password_entry.delete(0, END)
                Label(reg_root, text="Success",height="1", width="27", background="green").place(x=27,y=200)
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
        global username_verify
        global password_verify
        global username_entry1
        global password_entry1
        username_verify = StringVar()
        password_verify = StringVar()

        Label(log_root, text="Username", height="1", width="17", background="grey", foreground="white").pack()
        username_entry1 =  Entry(log_root, textvariable = username_verify)
        username_entry1.pack()
        Label(log_root, text="Password", height="1", width="17", background="grey", foreground="white").pack()
        password_entry1 = Entry(log_root, textvariable=password_verify)
        password_entry1.pack()

        #confirming and entering inputs
        # saving details button
        Label(log_root, text="").pack()
        Button(log_root, text="Login in", command= login_verify, height="1", width="17", background="grey", foreground="white").pack()

#Login function
def login_verify():
        username1 = username_verify.get()
        password1 = password_verify.get()
        username_entry1.delete(0, END)
        password_entry1.delete(0, END)

        list_of_files = os.listdir()
        if username1 in list_of_files:
                file1 = open(username1, "r")
                verify = file1.read().splitlines()
                if password1 in verify:
                        Label(log_root, text="Login success", command = main_screen() , height="1", width="19", background="green").place(x=56,y=200)
                        log_root.after(3000,log_root.destroy)
                        
                else:
                        Label(log_root, text="Wrong password", height="1", width="19", background="light blue").place(x=56,y=200)
        else:
               Label(log_root, text="username not recognised", height="1", width="19", background="light blue").place(x=56,y=200)

#main menu
def main_screen():
        main_root = Toplevel(logreg_root)
        main_root.title("Main menu")
        main_root.geometry("500x600")
        Label(main_root, text="Vegetation simulation", background="grey", foreground="white", height="1", width="35").pack()
        Label(main_root, text="Main Menu", background="grey", foreground="white", height="1", width="35").pack()


#Registation and login in screen
def logreg_screen():
        global logreg_root
        logreg_root.geometry("500x600")
        logreg_root.title("Vegetation simulation")
        Label(text = "Vegetation simulation", background ="grey", foreground ="white" ,height = "1", width = "35").pack()
        Label(text = "User portal", background ="grey", foreground ="white" ,height = "1", width = "35").pack()
        #buttons
        Label(text="").pack()
        Button(text = "Login", command = login_screen, height = "1", width = "15",background ="grey", foreground ="white").pack()

        Label(text= "").pack()
        Button(text = "Register", command = register_screen, height = "1", width = "15", background ="grey", foreground ="white").pack()

        Label(text="").pack()
        Button(text="Exit program", command= logreg_root.destroy, height="1", width="15", background ="grey", foreground ="white").pack()
        logreg_root.mainloop()

logreg_screen()


