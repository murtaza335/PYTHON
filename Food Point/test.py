import tkinter as tk

def toggle_entry():
    if var.get():
        global entry  # Use a global variable to reference the entry widget
        entry = tk.Entry(root)
        entry.pack()
    else:
        entry.destroy()

root = tk.Tk()
var = tk.BooleanVar()
checkbox = tk.Checkbutton(root, text="Check me!", variable=var, command=toggle_entry)
checkbox.pack()

root.mainloop()
