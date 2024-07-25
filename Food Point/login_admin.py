import tkinter as tk
from tkinter import messagebox
import subprocess
import sqlite3 as sql

conn = sql.connect("users_data.db")
cursor = conn.cursor()

username_from_db = cursor.execute("SELECT username FROM admins ").fetchall()[0][0]
password_from_db = cursor.execute("SELECT password FROM admins ").fetchall()[0][0]


# commonly used colors
creamBg = "#F7DDBF"
maroonBg = "#820202"
yellowDullBg = "#CFD000"
DarkSkinBg = "#C0794F"

def login():
    entered_username = entry_username.get()
    entered_password = entry_password.get()
    if entered_username == "" or entered_password == "":
        messagebox.showerror("Error","Enter Both username and password")
    else:
        if entered_username == username_from_db and entered_password == password_from_db:
            root.destroy()
            subprocess.run(["Python","admin_menu.py"])
        else:
            messagebox.showerror("Error","Incorrect username or password")
        

root = tk.Tk()

root.title("Login: ADMIN")
root.geometry("250x280")
root.configure(background=yellowDullBg)
frame = tk.Frame(root, padx=20, pady=30,bg = yellowDullBg)
frame.pack(pady=10)
label_username = tk.Label(frame, text="Username:",bg= yellowDullBg,font = ("Arial",10,"bold"))
label_username.grid(row=0, column=0,pady = 20)
usernameVar = tk.StringVar()
entry_username = tk.Entry(frame,textvariable=usernameVar,relief = "raised",bd = 2 )
entry_username.grid(row=0, column=1, pady=(0, 5))
label_password = tk.Label(frame, text="Password:",bg= yellowDullBg,font = ("Arial",10,"bold"))
label_password.grid(row=1, column=0, pady=(0, 5))
passwordVar = tk.StringVar()
entry_password = tk.Entry(frame, show="*",textvariable=passwordVar,relief = "raised",bd = 2 )
entry_password.grid(row=1, column=1, pady=(0, 5))
login_button = tk.Button(frame, text="Login",width = 20,bg = maroonBg,fg = "white",command = login)
login_button.grid(row=2, columnspan=2,pady = 20)
root.mainloop()

