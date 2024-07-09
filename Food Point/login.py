import tkinter as tk
from tkinter import messagebox
from user_data import *
import subprocess
def login():
    global index
    username = entry_username.get()
    password = entry_password.get()
    allUsernames = []
    allPasswords = []
    for i in range(len(cashier_data)):
        allUsernames.append(cashier_data[i][0])
        allPasswords.append(cashier_data[i][1])
    if username == "" or password == "":
        messagebox.showerror("Error","None of the field can be empty")
    else:
        if username in allUsernames :
            index = allUsernames.index(username)
            if password == allPasswords[index]:
                root.destroy()
                subprocess.run(['python', 'main.py'])
            else:
                messagebox.showerror("Error","Incorrect Password")
                passwordVar.set("")
        else:
            messagebox.showerror("Error","Username Does Not exist")
            usernameVar.set("")
            passwordVar.set("")
        
root = tk.Tk()

root.title("Login Page")
root.geometry("+600+250") 
frame = tk.Frame(root, padx=20, pady=30)
frame.pack(pady=10)
label_username = tk.Label(frame, text="Username:")
label_username.grid(row=0, column=0,pady = 20)
usernameVar = tk.StringVar()
entry_username = tk.Entry(frame,textvariable=usernameVar)
entry_username.grid(row=0, column=1, pady=(0, 5))
label_password = tk.Label(frame, text="Password:")
label_password.grid(row=1, column=0, pady=(0, 5))
passwordVar = tk.StringVar()
entry_password = tk.Entry(frame, show="*",textvariable=passwordVar)
entry_password.grid(row=1, column=1, pady=(0, 5))
login_button = tk.Button(frame, text="Login", command=login,width = 20)
login_button.grid(row=2, columnspan=2,pady = 20)
root.mainloop()

