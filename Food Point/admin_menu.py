import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
import sqlite3 as sql
from PIL import Image,ImageTk


# import ttkbootstrap as tb
# tb.Style().theme_use("cyborg")


# padding variables
padx_of_control_panel_grid = 40
pady_of_control_panel_grid =5

# font variables
font_grid_controlpanel_sub = ("Helvetica",12)
font_grid_controlpanel_head = ("Helvetica",12,"bold")
row_counter = 0 #for printing all tables at once
table_names_in_items = []
next_id = 0
check_confirm_btn_clicked = False
all_functions = ["Add Item","Delete Item","Edit Item","Show All Items","Delete Category","Show All Categories"]


conn = sql.connect("items.db")
cursor = conn.cursor()

def fetch_table_names_from_items():
    global table_names_in_items
    table_names = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    for i in range(len(table_names)):
        table_names_in_items.append(table_names[i][0])
fetch_table_names_from_items()

def calculate_next_item_id():
    next_id = 0
    try :
        selected_category = select_category_string_var.get()
        column = f"{selected_category}_id"
        id_list = cursor.execute(f"SELECT {column} FROM {selected_category}").fetchall()
        last_id = id_list[-1][0]
        next_id = last_id+1
    except:
        pass
    return next_id
def fetch_table_info(table_name):
    list = cursor.execute(f"PRAGMA table_info({table_name})").fetchall()
    return list

def fetch_col_names_from_table_info(table_info):
    column_names = []
    for i in range(len(table_info)):
        column_names.append(table_info[i][1])
    return column_names

def fetch_sizes_from_table_info(table_name):
    table_info = fetch_table_info(table_name)
    column_names = fetch_col_names_from_table_info(table_info)
    recommended_sizes= []
    for size in column_names:
        if size in ["Small","Medium","Large","X_Large"]:
            recommended_sizes.append(size)
        elif size in ["Half_L","One_L","One_Half_L"]:
            recommended_sizes.append(size)
    return recommended_sizes

def confirm_draft_add_item(entry_item_name):
    if (selected_category == "pizza" or selected_category == "shawarma"  or selected_category == "fries" or selected_category == "drinks"):
        if entry_item_name == "" or (checkbox1_selected and entry_price_size_small.get() == "") or (checkbox2_selected and entry_price_size_medium.get() == "") or (checkbox3_selected and entry_price_size_large.get() == "") or (checkbox4_selected and entry_price_size_x_large.get() == ""):
            messagebox.showerror("Error","Incomplete Data Provided")
    elif (selected_category == "burger" or "sauces" or "pizza_top"):
        pass

    

def show_entry_price_small():
    global entry_price_size_small,checkbox1,checkbox1_selected
    if checkbox1.get():
        checkbox1_selected = True
        entry_price_size_small = ctk.CTkEntry(temp_frame_in_frame_add_item,placeholder_text="Price")
        entry_price_size_small.grid(column = 1,row=5)
    else:
        try:
            checkbox1_selected = False
            entry_price_size_small.destroy()
        except:
            pass

def show_entry_price_medium():
    global entry_price_size_medium,checkbox2,checkbox2_selected
    if checkbox2.get():
        checkbox2_selected = True
        entry_price_size_medium = ctk.CTkEntry(temp_frame_in_frame_add_item,placeholder_text="Price")
        entry_price_size_medium.grid(column = 1,row=6)
    else:
        try:
            checkbox2_selected = False
            entry_price_size_medium.destroy()
        except:
            pass
def show_entry_price_large():
    global entry_price_size_large,checkbox3,checkbox3_selected
    if checkbox3.get():
        checkbox3_selected = True
        entry_price_size_large = ctk.CTkEntry(temp_frame_in_frame_add_item,placeholder_text="Price")
        entry_price_size_large.grid(column = 1,row=7)
    else:
        try:
            checkbox3_selected = False
            entry_price_size_large.destroy()
        except:
            pass
def show_entry_price_x_large():
    global entry_price_size_x_large,checkbox4,checkbox4_selected
    if checkbox4.get():
        checkbox4_selected = True
        entry_price_size_x_large = ctk.CTkEntry(temp_frame_in_frame_add_item,placeholder_text="Price")
        entry_price_size_x_large.grid(column = 1,row=8)
    else:
        try:
            checkbox4_selected = False
            entry_price_size_x_large.destroy()
        except:
            pass
def display_sizes_checkboxes(table_name):
    global checkbox1,checkbox2,checkbox3,checkbox4,entry_price_size_small,entry_price_size_medium,entry_price_size_large,entry_price_size_x_large
    
    recommended_sizes = fetch_sizes_from_table_info(table_name)

    label_select_checkboxes = tk.Label(temp_frame_in_frame_add_item,text = f"Select Sizes",bg= search_bar_frame_bg,font = font_grid_controlpanel_sub)
    label_select_checkboxes.grid(column=0,row=4)

    label_recommend_sizes = tk.Label(temp_frame_in_frame_add_item,text = f"Recommended: {recommended_sizes}",bg= search_bar_frame_bg,fg = "red")
    label_recommend_sizes.grid(row=4,column=1)

    checkbox1 = ctk.CTkCheckBox(temp_frame_in_frame_add_item,text= "Small",font= font_grid_controlpanel_sub,fg_color="red",text_color="black",command = show_entry_price_small)
    checkbox1.grid(column = 0,row = 5,pady = pady_of_control_panel_grid,padx = padx_of_control_panel_grid)
            

    checkbox2 = ctk.CTkCheckBox(temp_frame_in_frame_add_item,text= "Medium",font= font_grid_controlpanel_sub,fg_color="red",text_color="black",command = show_entry_price_medium)
    checkbox2.grid(column = 0,row = 6,pady = pady_of_control_panel_grid,padx = padx_of_control_panel_grid)
            

    checkbox3 = ctk.CTkCheckBox(temp_frame_in_frame_add_item,text= "Large",font= font_grid_controlpanel_sub,fg_color="red",text_color="black",command = show_entry_price_large)
    checkbox3.grid(column = 0,row = 7,pady = pady_of_control_panel_grid,padx = padx_of_control_panel_grid)


    checkbox4 = ctk.CTkCheckBox(temp_frame_in_frame_add_item,text= "X_Large",font= font_grid_controlpanel_sub,fg_color="red",text_color="black",command = show_entry_price_x_large)
    checkbox4.grid(column = 0,row = 8,pady = pady_of_control_panel_grid,padx = padx_of_control_panel_grid)

def display_button_confirm_draft():
    confirm_button_add_item = ctk.CTkButton(temp_frame_in_frame_add_item,text = "Confirm Draft",fg_color="red",width = 400,command = lambda : confirm_draft_add_item(entry_item_name.get()))
    confirm_button_add_item.grid(column = 0,row = 9,columnspan = 2,pady = 5,padx = 5)

def perform_action_on_basis_of_category(selected_category,selected_func):
    global temp_frame_in_frame_add_item,entry_item_name
    print_table(selected_category,0)
    if selected_func == "Add Item" :
        temp_frame_in_frame_add_item = tk.Frame(frame_of_add_item,bg =search_bar_frame_bg)
        temp_frame_in_frame_add_item.place(relx = 1,rely = 1,anchor = tk.SE ,relwidth=1,relheight=0.8)
        next_id = calculate_next_item_id()
        
        label_item_id = tk.Label(temp_frame_in_frame_add_item,text = "Item Code : ",bg = search_bar_frame_bg,font = font_grid_controlpanel_sub)
        label_item_id.grid(row = 2,column=0,pady = pady_of_control_panel_grid,padx = padx_of_control_panel_grid)

        item_id = tk.Label(temp_frame_in_frame_add_item,text = f"{next_id}",font = ("Helvetica",12),bg = search_bar_frame_bg)
        item_id.grid(row = 2,column = 1,pady = 5,padx = 5)
        label_enter_item_name = tk.Label(temp_frame_in_frame_add_item,text = "Enter Item Name : ",bg = search_bar_frame_bg,font = font_grid_controlpanel_sub)
        label_enter_item_name.grid(row = 3,column=0,pady = pady_of_control_panel_grid,padx = padx_of_control_panel_grid)

        entry_item_name = ctk.CTkEntry(temp_frame_in_frame_add_item,width = 200)
        entry_item_name.grid(column = 1,row = 3)

        if (selected_category == "pizza" or selected_category == "shawarma"  or selected_category == "fries" or selected_category == "drinks"):
            display_sizes_checkboxes(selected_category)
            display_button_confirm_draft()
        elif (selected_category == "burger" or "sauces" or "pizza_top"):
            display_button_confirm_draft()
            
        




def show_category_dropdown(selected_func):
    global select_category_string_var,selected_category
    label_select_category = tk.Label(frame_of_add_item,text = "Select Category: ",bg = search_bar_frame_bg,font = font_grid_controlpanel_sub)
    label_select_category.grid(row = 1,column=0,pady = pady_of_control_panel_grid,padx = padx_of_control_panel_grid)
    select_category_string_var = tk.StringVar()
    select_fucntion_dropdown = ctk.CTkComboBox(frame_of_add_item,values = table_names_in_items,width = 200,variable=select_category_string_var,command = lambda event: perform_action_on_basis_of_category(event,selected_func))
    
    select_fucntion_dropdown.grid(row = 1,column = 1,pady = pady_of_control_panel_grid,padx = padx_of_control_panel_grid)
    select_category_string_var.set(value = "Category")


    


def sales_analysis():
    pass
def user_report():
    pass
def available_stock():
    pass
def committing_changes_to_items():
    conn.commit()

# def update_total_after_gst():
#     calculate_next_item_id()
#     try:
#         entered_price = int(entry_item_price.get())
#         total_after_gst.set(value = "0.0")
#         price_after_gst = str(entered_price+(entered_price*0.175))
#         total_after_gst.set(value = f"{price_after_gst}")
#         mainWindow.after(200, update_total_after_gst) 
#     except:
#         total_after_gst.set(value = "0.0")



def print_table(table_name,row_count):
    global row_counter 
    row_counter = row_count
    none_label.destroy()
    table = cursor.execute(f"SELECT * FROM {table_name}").fetchall()
    info = cursor.execute(f"PRAGMA table_info({table_name})").fetchall()

    table_frame = tk.Frame(frame_under_table_selection_frame,bg = "white")
    table_frame.place(relx = 0,rely = 0,relwidth=1,relheight = 1,anchor = tk.NW)

    # label = tk.Label(frame_under_table_selection_frame,text = f"{info[0][1]}")
    # label.grid(row = row_counter,column = 0,columnspan  = 6)
    row_counter +=1
    for i in range(len(info)):
        label = tk.Label(frame_under_table_selection_frame,text = f"{info[i][1]}",bg = "white",font = ("Helvetica",10,"bold"))
        label.grid(column = i,row = row_counter,padx = 20)
    row_counter += 1
    for i in range(len(table)):
        for j in range(len(table[i])):
            label = tk.Label(frame_under_table_selection_frame,text = f"{table[i][j]}",bg = "white")
            label.grid(column = j,row = row_counter,padx = 50)
        row_counter +=1
    
def table_selection_command(table_name):
    print_table(table_name,0)




def displayallitems():
    pizza_table = cursor.execute("SELECT * FROM pizza").fetchall()
    shawarma_table = cursor.execute("SELECT * FROM shawarma").fetchall()
    burger_table = cursor.execute("SELECT * FROM burger").fetchall()
    fries_table = cursor.execute("SELECT * FROM fries").fetchall()
    drinks_table = cursor.execute("SELECT * FROM drinks").fetchall()

    pizza_info = cursor.execute("PRAGMA table_info(pizza)").fetchall()
    shawarma_info = cursor.execute("PRAGMA table_info(shawarma)").fetchall()
    burger_info = cursor.execute("PRAGMA table_info(burger)").fetchall()
    fries_info = cursor.execute("PRAGMA table_info(fries)").fetchall()
    drinks_info = cursor.execute("PRAGMA table_info(drinks)").fetchall()




# commonly used colors
creamBg = "#F7DDBF"
maroonBg = "#820202"
yellowDullBg = "#CFD000"
DarkSkinBg = "#C0794F"
purplebg = "#C660E2"
greybg = "#908B92"
darkgreybg = "#433F44"
hoverbuttongreybg = "#7B757C"
search_bar_frame_bg = "#D1DAD4"
entrywidget_bg = "#B1B6B3"
navyblue_bg = "#B8E0DC"


mainWindow = tk.Tk()
mainWindow.state("zoomed")
mainWindow.resizable(False,False)



select_category_string_var  =tk.StringVar()
temp_frame_in_frame_add_item = 0
checkbox1_selected = False
checkbox2_selected = False
checkbox3_selected = False
checkbox4_selected = False

entry_item_name = None
selected_category = None
checkbox1 = None
checkbox2 = None
checkbox3 = None
checkbox4 = None
entry_price_size_small = None
entry_price_size_medium = None
entry_price_size_large = None
entry_price_size_x_large = None


# -----------gui------------
main_frame_of_fullscreen = tk.Frame(mainWindow)
main_frame_of_fullscreen.place(relwidth=1,relheight=1)

# mainframe of navbar
main_frame_of_navbar = tk.Frame(main_frame_of_fullscreen,bg = "#89998B")
main_frame_of_navbar.place(relwidth=1,relheight = 0.05,relx = 0.0,rely = 0.0,anchor = tk.NW)

# mainframe of displaying all items
main_frame_of_display_allitems = tk.Frame(main_frame_of_fullscreen)
main_frame_of_display_allitems.place(relx = 1,rely =1,anchor = tk.SE,relwidth=0.6,relheight = 0.95)


# headers frame of display all items

scrollabel_frame_item = ctk.CTkScrollableFrame(main_frame_of_display_allitems,label_fg_color=darkgreybg,label_text_color="black",label_font = ("Helvetica",18),fg_color="white")
scrollabel_frame_item.place(relx = 1,rely= 1,anchor = tk.SE,relwidth = 1,relheight = 1)


frame_under_table_selection_frame = tk.Frame(scrollabel_frame_item,bg= "white",width = 900,height = 740)
frame_under_table_selection_frame.grid(column = 0,row =0)

none_label_var = tk.StringVar()
none_label = tk.Label(frame_under_table_selection_frame,text = "Nothing to Display",font = ("Helvetica",12),fg = "grey",textvariable=none_label_var,bg = "white")
none_label.place(relx = 0.5,rely = 0.5,anchor = tk.CENTER)
none_label_var.set("None of the Table Selected to Display")


# mainframe of control panel besides frame of display all items

main_frame_of_control_panel = tk.Frame(main_frame_of_fullscreen)
main_frame_of_control_panel.place(relx = 0,rely =1,anchor = tk.SW,relwidth=0.4,relheight = 0.95)


# frame of three buttons: sales analysis,available stock,user data

# frame_of_three_buttons = tk.Frame(main_frame_of_control_panel)
# frame_of_three_buttons.place(relx = 0,rely =1,anchor = tk.SW,relwidth=1,relheight = 0.15)

# button_avaialable_stock = ctk.CTkButton(frame_of_three_buttons,text = "Available Stock",width = 270,height = 45,font = ("Helvetica",14),fg_color=greybg,text_color="black",hover_color=hoverbuttongreybg,corner_radius=100)
# button_avaialable_stock.grid(column = 0 ,row = 0,padx = 10,pady = 10)

# button_user_report = ctk.CTkButton(frame_of_three_buttons,text = "User Report",width = 270,height = 45,font = ("Helvetica",14),fg_color=greybg,text_color="black",hover_color=hoverbuttongreybg,corner_radius=100)
# button_user_report.grid(column = 1,row = 0,padx = 10,pady = 10)

# button_sales_analysis = ctk.CTkButton(frame_of_three_buttons,text = "Sales Analysis",width = 580,height = 45,font = ("Helvetica",14),fg_color=greybg,text_color="black",hover_color=hoverbuttongreybg,corner_radius=100)
# button_sales_analysis.grid(column = 0,row = 1,columnspan=2,padx = 20)

# search item frame
frame_of_search_widget = tk.Frame(main_frame_of_control_panel,bg = search_bar_frame_bg)
frame_of_search_widget.place(relx = 0,rely =0,anchor = tk.NW,relwidth=1,relheight = 0.06)
# search icon
search_icon = ImageTk.PhotoImage(Image.open("images/search_icon.png"))
label_search = tk.Button(frame_of_search_widget,image=search_icon,bd=1,relief="raised")
label_search.place(relx = 0.97,rely=0.5,anchor = tk.E,width=30,height=30)
# search entry
search_entry = ctk.CTkEntry(frame_of_search_widget,placeholder_text="Search Item",width = 500,corner_radius=100,border_width=1,fg_color=entrywidget_bg,placeholder_text_color="black",border_color="black")
search_entry.pack(pady = 10)


# control panel all fucntion frame 
frame_of_add_item = tk.Frame(main_frame_of_control_panel,bg = search_bar_frame_bg)
frame_of_add_item.place(relx = 0,rely =0.06,anchor = tk.NW,relwidth=1,relheight = 0.5)


label_select_function = tk.Label(frame_of_add_item,text = "Select Function : ",bg = search_bar_frame_bg,font = font_grid_controlpanel_head)
label_select_function.grid(row = 0,column = 0,pady = pady_of_control_panel_grid,padx = padx_of_control_panel_grid)

select_func_string_var = tk.StringVar()
select_fucntion_dropdown = ctk.CTkComboBox(frame_of_add_item,values = all_functions,width = 200,variable=select_func_string_var,command = show_category_dropdown)
select_fucntion_dropdown.grid(row = 0,column = 1,pady = pady_of_control_panel_grid,padx = padx_of_control_panel_grid)
select_func_string_var.set(value = "Function")



















# show draft----------------------








mainWindow.mainloop()