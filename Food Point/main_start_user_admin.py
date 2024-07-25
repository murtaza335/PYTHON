import tkinter as tk
import subprocess
import sqlite3 as sql

conn = sql.connect("users_data.db")
cursor = conn.cursor()


# creating table of users data
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
               user_id INTEGER PRIMARY KEY  ,
               username TEXT,
               password TEXT,
               first_name TEXT,
               last_name TEXT,
               father_name TEXT,
               cnic INTEGER,
               d_o_b TEXT
               )""")
# cursor.execute("""CREATE TABLE IF NOT EXISTS admins(
#                user_id INTEGER PRIMARY KEY  ,
#                username TEXT,
#                password TEXT,
#                first_name TEXT,
#                last_name TEXT,
#                father_name TEXT,
#                cnic INTEGER,
#                d_o_b TEXT
#                )""")


# creating table of admin data

# commonly used colors
creamBg = "#F7DDBF"
maroonBg = "#820202"
yellowDullBg = "#CFD000"
DarkSkinBg = "#C0794F"






def run_user_login():
    subprocess.run(['python', 'login_user.py'])


def run_admin_login():
    subprocess.run(['python', 'login_admin.py'])

root = tk.Tk()

root.configure(background = creamBg)
root.state("zoomed")
root.resizable(False,False)

label = tk.Label(root,text = "Login As : ",font = ("Arial",24,"bold"),bg = creamBg).place(relx = 0.5,rely = 0.2,anchor = tk.CENTER)

frame_button = tk.Frame(root,width = 600,height = 300,bg = creamBg,relief="solid",bd = 2)
frame_button.place(relx = 0.5,rely = 0.5,anchor = tk.CENTER)
label_note = tk.Label(frame_button,text = "*Only Admin can register a new user",fg = "red",bg = creamBg)
label_note.place(relx = 0.5,rely = 0.9,anchor = tk.CENTER)


button_user = tk.Button(frame_button,text = "USER",bg = maroonBg,fg = "white",padx = 50,pady = 50,font = ("Arial",24,"bold"),command = run_user_login)
button_user.place(relx= 0.3,rely = 0.5,anchor=tk.CENTER)


button_admin = tk.Button(frame_button,text = "ADMIN",bg = maroonBg,fg = "white",padx = 50,pady = 50,font = ("Arial",24,"bold"),command = run_admin_login)
button_admin.place(relx= 0.7,rely = 0.5,anchor=tk.CENTER)

root.mainloop()