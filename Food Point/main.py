import sqlite3 as sql
import tkinter as tk
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import random
from deals import *

import ttkbootstrap as tb
tb.Style().theme_use("cyborg")


# global objects-----------
row = 1 # this variable is used for displaying new item on the next line in bill management system area
AllItemsInOneBill = [] # contains all items that is included in a single order
# all variables related to a single order (to print the reciept)
productIdList = []
productCategoryList = []
productNameList = []
productRateList = []
productQtyList = []
productGstList = []
productTotalPriceList = []
productSizeList = []
# this variable counts number of items that are currently present in the current order
noOfItemsInOrder = 0 # this variable counts number of items that are present in the current order
gst = 0
totalBillItem = 0 # total bill of the single item
TotalBill = 0
Totalgst = 0
orderNo = 0

# ------------------------------------------------------------------------------------------------------------------------------------------------------------





# databse connection-----
conn_items = sql.connect("items.db")
cursor_itmes = conn_items.cursor()
conn_current_order = sql.connect("current_order.db")
cursor_current_order = conn_current_order.cursor()

# fetching data from all table in item.db

sauces_table = cursor_itmes.execute("SELECT * FROM sauces").fetchall()
sauces = []
for i in range(len(sauces_table)):
    sauces.append(f"{sauces_table[i][1]}--{sauces_table[i][2]}")

pizza_table = cursor_itmes.execute("SELECT * FROM pizza").fetchall()
pizza_top_table = cursor_itmes.execute("SELECT * FROM pizza_top").fetchall()
pizza_flavors = []
pizza_sizes = ['Small','Medium','Large','X_Large']
pizza_topping = []
for i in range(len(pizza_table)):
    pizza_flavors.append(pizza_table[i][1])
    pizza_topping.append(pizza_top_table[i][1])

burger_table = cursor_itmes.execute("SELECT * FROM burger").fetchall()
burger_flavors = []
for i in range(len(burger_table)):
    burger_flavors.append(burger_table[i][1])

shawarma_table = cursor_itmes.execute("SELECT * FROM shawarma").fetchall()
shawarma_flavors = []
sha_fri_sizes = ['Small','Medium','Large']

for i in range(len(shawarma_table)):
    shawarma_flavors.append(shawarma_table[i][1])

fries_table = cursor_itmes.execute("SELECT * FROM fries").fetchall()
fries_flavors = []
for i in range(len(fries_table)):
    fries_flavors.append(fries_table[i][1])

drinks_table = cursor_itmes.execute("SELECT * FROM drinks").fetchall()
drinks_sizes = ['Half_L','One_L','One_Half_L']
drinks = []
for i in range(len(drinks_table)):
    drinks.append(drinks_table[i][1])

def updating_order_table_after_confirming_order():
    cursor_current_order.execute("""CREATE TABLE IF NOT EXISTS current_order(
                                item_id INTEGER ,
                                 category TEXT,
                                item_name TEXT,
                                 size TEXT,
                                quantity INTEGER,
                                Rate FLOAT,
                                gst FLOAT,
                                totalPrice FLOAT                   
                                 )""")
    for i in range(len(productNameList)):
        cursor_current_order.execute("INSERT INTO current_order(item_id, category, item_name, size, quantity, Rate, gst,totalPrice) VALUES(?,?,?,?,?,?,?,?)",(productIdList[i],productCategoryList[i], productNameList[i],productSizeList[i], productQtyList[i], productRateList[i], productGstList[i], productTotalPriceList[i]))
        conn_current_order.commit()

def gst_total_calc(ItemPrice,quantity):
    
    totalBill = ItemPrice*quantity
    gst = (totalBill*17.5)/100
    totalBill += gst
    return gst,totalBill

def small_med_large_length_reducer(size):
    if size == "Small":
        size = "S"
    elif size == "Medium":
        size = "M"
    elif size == "Large":
        size = "L"
    elif size == "X_Large":
        size = "XL"
    elif size == "Half_L":
        size = "0.5L"
    elif size == "One_L":
        size = "1L"
    elif size == "One_Half_L":
        size = "1.5L"
    else:
        size = ""
    return size


def funcDealContents(i):
    dealHead = f"{family_deals[i-1][0]}: "
    dealContents = ""
    for j in range(len(family_deals[i-1][1])):
        dealLine = f"{family_deals[i-1][1][j][0]} x {family_deals[i-1][1][j][1]}\n"
        dealContents += dealLine
    return dealHead,dealContents
# if any field is empty
def show_error_empty_field():
    messagebox.showerror("Error","Select Both Flavor and size")
# this function clears order whenever CLEARBUTTON is pressed
def funcclearOrder():
    global productIdList,productNameList,productRateList,productQtyList,productGstList,productTotalPriceList,AllItemsInOneBill,TotalBill,Totalgst,noOfItemsInOrder,productCategoryList,productSizeList
    productSizeList.clear()
    productIdList.clear()
    productCategoryList.clear()
    productNameList.clear()
    productRateList.clear()
    productQtyList.clear()
    productGstList.clear()
    productTotalPriceList.clear()
    for item in AllItemsInOneBill:
        for label in item:
            label.destroy()
    AllItemsInOneBill.clear()
    TotalBill = 0
    Totalgst = 0
    noOfItemsInOrder = 0
    
# recieptPrinter() function creates a .txt file with name of the order no. and saves the bill in a formatted way and we can print it later if needed
def recieptPrinter():
    pass
    
        # f = open(f"reciepts/Order_{orderNo}.txt","w")
        # f.write(f"order no: {orderNo}\n\n")
        # for i in range(len(productNameList)):
        #     f.write(f"{productNameList[i]} x {productQtyList[i]} : Rs.{productTotalPriceList[i]}\n")
        # f.close()


def confirming_order():
    if noOfItemsInOrder >0:
        updating_order_table_after_confirming_order()
        recieptPrinter()
    else:
        messagebox.showerror("Error","Please select an item to order")
    
    funcclearOrder()
# this function updates total gst and total price whenever an item is deleted    
def updatePriceDeletedItem(gst,totalBillItem):
    
    global TotalBill,Totalgst
    TotalBill -= totalBillItem
    Totalgst -= gst
# this function updates total gst and total price in real time 
def updateTotalPrice():
    global TotalBill,Totalgst
    # updates the price whenever item is added.
    TotalBill += totalBillItem
    Totalgst += gst
    totalGstStringVar.set(value = f"{Totalgst:.1f}")
    totalPriceStringVar.set(value = f"{TotalBill:.1f}")
    # to update the total price after each 200 millisecond
    mainWindow.after(200, updateTotalPrice) 
# -------------------------
def updateProductListsforReciept_ADD(name,rate,qty,gst,price,item_id,category,size):
    global productIdList,productNameList,productRateList,productQtyList,productGstList,productTotalPriceList,productCategoryList,productSizeList
    # print(name,rate,qty,gst,price,item_id,category,size)
    productIdList.append(item_id)
    productCategoryList.append(category)
    productNameList.append(name)
    productSizeList.append(size)
    productQtyList.append(qty)
    productRateList.append(rate)
    productGstList.append(gst)
    productTotalPriceList.append(price)
def updateProductListsforReciept_DEL(name,rate,qty,gst,price,item_id,category,size):
    # deleting items from the list on the basis of the item_id so that if the list contain multiple same items. no error occurs
    productCategoryList.pop(productCategoryList.index(category))
    productIdList.pop(productIdList.index(item_id))
    productQtyList.pop(productQtyList.index(qty))
    productGstList.pop(productGstList.index(gst))
    productNameList.pop(productNameList.index(name))
    productRateList.pop(productRateList.index(rate))
    productTotalPriceList.pop(productTotalPriceList.index(price))
# -------------------------


# following function is triggered whenever the item is double clicked and deletes that label and its corresponding
def funcDeleteItemFromBill(event,allLabelsItemBill,gst,totalBillItem,ProductName,Rate,quantity,item_id,category,size):
    global noOfItemsInOrder
    # deleting item from the all the lists of ordered items
    updateProductListsforReciept_DEL(ProductName,Rate,quantity,gst,totalBillItem,item_id,category,size)
    noOfItemsInOrder -= 1
    # following fucntion is called so that the total price and total gst is updated after the item is deleted
    updatePriceDeletedItem(gst,totalBillItem)
    for lbl in allLabelsItemBill:
        lbl.destroy()
# this function adds new items to the bill management section when ever a new item is confirmed
def updateBillManagement(quantity,gst,totalBillItem,ProductName,Rate,item_id,category,size):
    global row,TotalBill,Totalgst,noOfItemsInOrder 
    TotalBill += totalBillItem # adds the price current item in the total bill
    Totalgst += gst # adds the gst applied on the current item to the total gst variable
    # following labels to display data in bill management frame
    
    labelProductName = tk.Label(frameBodyBillManagement,text = f"{ProductName}",wraplength=110,bg = "white")
    labelProductName.grid(column = 0,row=row,padx = 2)
    labelRate = tk.Label(frameBodyBillManagement,text = f"{Rate}",bg = "white")
    labelRate.grid(column=1,row = row)
    labelQty = tk.Label(frameBodyBillManagement,text = f"{quantity}",bg = "white",wraplength=30)
    labelQty.grid(column = 2,row=row,padx = 2)
    labelGst = tk.Label(frameBodyBillManagement,text = f"{gst:.1f}",bg = "white",wraplength=30)
    labelGst.grid(column = 3,row=row,padx = 2)
    labelPrice = tk.Label(frameBodyBillManagement,text = f"{totalBillItem}",bg = "white",wraplength=30)
    labelPrice.grid(column = 4,row=row,padx = 2)
    # creating feature to delete the item by double clicking it
    # following list contains all the labels in bill management frame related to a single item
    OneItem = [labelProductName,labelRate,labelQty,labelGst,labelPrice]
    AllItemsInOneBill.append(OneItem)
    updateProductListsforReciept_ADD(ProductName,Rate,quantity,gst,totalBillItem,item_id,category,size)
    # following for loop binds double click event to all the labels that were previously added to the list (OneItem) and whenever the label is double-clicked.
    
    for item in OneItem:
        item.bind("<Double-Button-1>",lambda event:funcDeleteItemFromBill(event,OneItem,gst,totalBillItem,ProductName,Rate,quantity,item_id,category,size))
    row += 1  
    noOfItemsInOrder +=1
    # calling following fucntion to update the total price 
    updateTotalPrice()
# following fucntion is used to get data from the pizza selection dropdowns and spinbox, it also calculates the price according the quantity
def funcPizzaSelection():
    Name = "Piz"
    category = "pizza"
    # recieving value from dropdowns and spinbox
    selectedFlavor = pizzaFlavorsDropDown.get()
    selectedSize = pizzaSizesDropDown.get()
    quantity = int(quantitySpinboxPizza.get())
    # empty field error handling
    if selectedFlavor == "" or selectedSize == "":
        show_error_empty_field()
    else:
        PizzaPrice = cursor_itmes.execute(f"SELECT {selectedSize} FROM pizza WHERE pizza_names = (?) ", (selectedFlavor,)).fetchone()
        PizzaPrice = int(PizzaPrice[0])
        gst,totalBillPizza = gst_total_calc(PizzaPrice,quantity)
        
        size = small_med_large_length_reducer(selectedSize)
        item_id = cursor_itmes.execute("SELECT pizza_id FROM pizza WHERE pizza_names=(?)",(selectedFlavor,)).fetchone()
        item_id = int(item_id[0])
        # setting spinbox to 1 
        spinboxVarPizza.set("1")
        # a comprehensive product name is made to display in the bill management section
        ProductName = f"{Name}: {selectedFlavor}-{size}"
        # updateBillManagement function is called to update the bill with the current pizza item
        updateBillManagement(quantity,gst,totalBillPizza,ProductName,PizzaPrice,item_id,category,selectedSize)
# following function is used to get data from burger selection dropdowns and spinbox, it also calculates the price according the quantity
def funcBurgerSelection():
    Name = "Bur"
    category = "Burger"
    # recieving data from the dropdowns and list boxes
    selectedFlavor = burgerFlavorsDropDown.get()
    quantity = int(quantitySpinboxBurger.get())
    selectedSize = None
    # empty field error handling
    if selectedFlavor == "" :
        show_error_empty_field()
    else:
        # calculating the total of the burger item and gst applied
        burgerPrice = cursor_itmes.execute(f"SELECT burger_price FROM burger WHERE burger_names = (?)",(selectedFlavor,)).fetchone()
        burgerPrice = int(burgerPrice[0])
        gst,totalBillBurger = gst_total_calc(burgerPrice,quantity)
        
        item_id = cursor_itmes.execute("SELECT burger_id FROM burger WHERE burger_names=(?)",(selectedFlavor,)).fetchone()
        item_id = int(item_id[0])
        # setting spinbox to 1 
        spinboxVarBurger.set("1")
        
        # making a comprehensive product name to display it in the bill management
        ProductName = f"{Name}: {selectedFlavor}"
        # updating the bill managing table
        updateBillManagement(quantity,gst,totalBillBurger,ProductName,burgerPrice,item_id,category,selectedSize)
# following function is used to get data from shawarma selection dropdowns and spinbox, it also calculates the price according the quantity 
def funcShawarmaSelection():
    Name = "Sha"
    category = "Shawarma"
    # recieving value from dropdowns and spinbox
    selectedFlavor = ShawarmaFlavorsDropDown.get()
    selectedSize = ShawarmaSizesDropDown.get()
    quantity = int(quantitySpinboxShawarma.get())
    # empty field error handling
    if selectedFlavor == "" or selectedSize == "":
        show_error_empty_field()
    else:
        # calculating total shawarma prices and gst applied on the item
        shawarmaPrice = cursor_itmes.execute(f"SELECT {selectedSize} FROM shawarma WHERE shawarma_names = (?)",(selectedFlavor,)).fetchone()
        shawarmaPrice = int(shawarmaPrice[0])
        gst,totalBillShawarma = gst_total_calc(shawarmaPrice,quantity)
        
        item_id = cursor_itmes.execute("SELECT shawarma_id FROM shawarma WHERE shawarma_names=(?)",(selectedFlavor,)).fetchone()
        item_id = int(item_id[0])
        # setting spinbox to 1 
        spinboxvarShawarma.set("1")
        selectedSize = small_med_large_length_reducer(selectedSize)
        # comprehensive product name 
        ProductName = f"{Name}: {selectedFlavor}-{selectedSize}"
        # updating bill manager
        updateBillManagement(quantity,gst,totalBillShawarma,ProductName,shawarmaPrice,item_id,category,selectedSize)
# following function is used to get data from fries selection dropdowns and spinbox, it also calculates the price according the quantity 
def funcFriesSelection():
    Name = "Fri"
    category = "Fries"
    # recieving value from dropdowns and spinbox
    selectedFlavor = FriesFlavorsDropDown.get()
    selectedSize = FriesSizesDropDown.get()
    quantity = int(quantitySpinboxFries.get())
    # empty field error handling
    if selectedFlavor == "" or selectedSize == "":
        show_error_empty_field()
    else:
        # calculating total fries prices and total gst applied
        friesPrice = cursor_itmes.execute(f"SELECT {selectedSize} FROM fries WHERE fries_names = (?)",(selectedFlavor,)).fetchone()
        friesPrice = friesPrice[0]
        gst,totalBillFries = gst_total_calc(friesPrice,quantity)
        
        item_id = cursor_itmes.execute("SELECT fries_id FROM fries WHERE fries_names=(?)",(selectedFlavor,)).fetchone()
        item_id = int(item_id[0])
        selectedSize = small_med_large_length_reducer(selectedSize)
        
        # setting spinbox to 1 
        spinboxvarFries.set("1")
        # comprehensive product name
        ProductName = f"{Name}: {selectedFlavor}-{selectedSize}"
        # updating bill manager
        updateBillManagement(quantity,gst,totalBillFries,ProductName,friesPrice,item_id,category,selectedSize)
# following function is used to get data from DRINKS selection dropdowns and spinbox, it also calculates the price according the quantity 
def funcDrinksSelection():
    Name = "Drink"
    category = "Drink"
    # recieving value from dropdowns and spinbox
    selectedDrink = DrinksDropDown.get()
    selectedSize = DrinksSizesDropdown.get()
    print(selectedSize)
    quantity = int(quantitySpinboxDrinks.get())
    # empty field error handling
    if selectedDrink == "" or selectedSize == "":
        show_error_empty_field()
    else:
        # calculating total fries prices
        
        drinkPrice = cursor_itmes.execute(f"SELECT {selectedSize} FROM drinks WHERE drinks_names = (?)",(selectedDrink,)).fetchone()
        drinkPrice = drinkPrice[0]
        gst,totalBillDrinks = gst_total_calc(drinkPrice,quantity)
        
        item_id = cursor_itmes.execute("SELECT drinks_id FROM drinks WHERE drinks_names=(?)",(selectedDrink,)).fetchone()
        item_id = int(item_id[0])
        selectedSize = small_med_large_length_reducer(selectedSize)
        # setting spinbox to 1 
        spinboxVarDrinks.set("1")
        # Comprehensive product name
        ProductName = f"{Name}: {selectedDrink}-{selectedSize}"
        # updating bill manager
        updateBillManagement(quantity,gst,totalBillDrinks,ProductName,drinkPrice,item_id,category,selectedSize)




# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------creating GUI -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


mainWindow = tk.Tk()
mainWindow.state("zoomed")
mainWindow.title("Murtaza Food Point")
mainWindow.resizable(False,False)

# commonly used colors
creamBg = "#F7DDBF"
maroonBg = "#820202"
yellowDullBg = "#CFD000"
DarkSkinBg = "#C0794F"

# -------------frame top bar ----------
frameTopBar = tk.Frame(mainWindow,bg = "red",relief="solid",bd = 2)
frameTopBar.place(relwidth= 1,relheight=0.03,relx = 0.0,rely = 0.0,anchor = tk.NW)

orderNo = random.randint(1000,9999)
OrderNotextVar = tk.StringVar()
tk.Label(frameTopBar,textvariable=OrderNotextVar,bg = "red",fg = "white",font = ("Arial",8,"bold")).place(relx = 0.0,rely = 0.0,anchor = tk.NW)
OrderNotextVar.set(value = f"order no : {orderNo}")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------main frame of full screen under top bar -----------------
frameMainUnderTopBar = tk.Frame(mainWindow,bg= creamBg)
frameMainUnderTopBar.place(relwidth= 1,relheight=1,relx = 0.0,rely = 0.0301,anchor = tk.NW)

# ----------left frame (bill management) inside main frame under top bar---------------------
frameLeftBillManagement = tk.Frame(frameMainUnderTopBar,bg= "white",bd =2,relief="solid")
frameLeftBillManagement.place(relwidth= 0.25,relheight=1,relx = 0.0,rely = 0.0,anchor = tk.NW)

# top bar of left frame of bill management
topBarOfFrameLeftBillManagement = tk.Frame(frameLeftBillManagement,relief="solid",bd = 1)
topBarOfFrameLeftBillManagement.place(relx = 0.0,rely = 0.0,relwidth=1,relheight=0.05,anchor = tk.NW)

labelHeadBillManagement = tk.Label(topBarOfFrameLeftBillManagement,text = "RECIEPT" , fg = "white",bg = maroonBg,font = ("Arial",20,"bold"))
labelHeadBillManagement.place(relwidth=1,relheight=1)

# canvas of body content bill managemnt
canvasBill = tk.Canvas(frameLeftBillManagement)
canvasBill.place(relwidth= 1,relheight= 0.5 ,relx = 0.0,rely = 0.05,anchor = tk.NW)


# body content bill managemnt main frame
frameBodyBillManagement = tk.Frame(canvasBill,bg = "white",relief="solid",bd= 1)
frameBodyBillManagement.place(relwidth= 1,relheight= 1 ,relx = 0.0,rely = 0.0,anchor = tk.NW)
# frame for confirm button etc
frameBodyBillConfirm = tk.Frame(frameLeftBillManagement,bg = "white",relief="solid",bd= 1)
frameBodyBillConfirm.place(relwidth= 1,relheight= 0.1 ,relx = 0.0,rely = 0.55,anchor = tk.NW)
# clear order
buttonClearOrder = tk.Button(frameBodyBillConfirm,text= "CLEAR ORDER",bg= "grey",fg = "white",font = ("Arial",16,"bold"),command = funcclearOrder)
buttonClearOrder.place(relwidth=0.48,relheight = 0.9,relx = 0.25,rely = 0.5,anchor = tk.CENTER)
# print reciept
buttonPrintReciept = tk.Button(frameBodyBillConfirm,text= "PRINT RECIEPT",bg= maroonBg,fg = "white",font = ("Arial",16,"bold"),command =confirming_order)
buttonPrintReciept.place(relwidth=0.48,relheight = 0.9,relx = 0.75,rely = 0.5,anchor = tk.CENTER)
# Create a vertical scrollbar for the canvas
scrollbar = ttk.Scrollbar(frameBodyBillManagement, orient=tk.VERTICAL, command=canvasBill.yview)
scrollbar.place(relheight=1,relx = 1,rely = 0.0,anchor = tk.NE)

# Configure the canvas and scrollbar
canvasBill.configure(yscrollcommand=scrollbar.set)

frameBodyBillManagement.update_idletasks()
canvasBill.configure(scrollregion=canvasBill.bbox("all"))
# --------------


headContentBillManagement = tk.Label(frameBodyBillManagement,text = "Product Name")
headContentBillManagement.grid(row = 0,column = 0,padx = 20,pady = 5)

headContentBillManagement = tk.Label(frameBodyBillManagement,text = "Rate")
headContentBillManagement.grid(row = 0,column = 1,padx = 10,pady = 5)

headContentBillManagement = tk.Label(frameBodyBillManagement,text = "Qty")
headContentBillManagement.grid(row = 0,column = 2,padx = 2,pady = 5)

headContentBillManagement = tk.Label(frameBodyBillManagement,text = "GST 17.5%")
headContentBillManagement.grid(row = 0,column = 3,padx = 10,pady = 5)

headContentBillManagement = tk.Label(frameBodyBillManagement,text = "Price")
headContentBillManagement.grid(row = 0,column = 4,padx = 10,pady = 5)

    



# main frame of three partitions in left frame (bill managemnt) (bottom)
frameMainOfPartitionsLeftBottom = tk.Frame(frameLeftBillManagement,bg = creamBg)
frameMainOfPartitionsLeftBottom.place(relheight= 0.35,relwidth=1,relx = 0.0,rely=1.0,anchor = tk.SW)
# four partitions left bottom
# 1
subFrameOfLeftBottom1 = tk.Frame(frameMainOfPartitionsLeftBottom,bg = yellowDullBg,relief="solid",bd = 1)
subFrameOfLeftBottom1.place(relwidth= 0.5,relheight=0.5,relx = 0.0,rely=0.0,anchor = tk.NW)
LabelTax1 = tk.Label(subFrameOfLeftBottom1,text = "Tax Applied: 17.5% Gst",bg = yellowDullBg,font = ("Arial",16,"bold"),wraplength=190)
LabelTax1.place(relx = 0.0,rely = 0.0,anchor = tk.NW)

# displays total gst with green bg
totalGstStringVar = tk.StringVar()
LabelTotalGst = tk.Label(subFrameOfLeftBottom1,text = Totalgst,bg = "green",font = ("Arial",20,"bold"),wraplength=190,fg = "white",textvariable= totalGstStringVar)
LabelTotalGst.place(relwidth = 1,relheight = 0.5,relx = 0.5,rely = 0.75,anchor = tk.CENTER)


# 2
subFrameOfLeftBottom2 = tk.Frame(frameMainOfPartitionsLeftBottom,relief="solid",bd = 1,bg = yellowDullBg)
subFrameOfLeftBottom2.place(relwidth= 0.5,relheight=0.5,relx = 1.0,rely=0.0,anchor = tk.NE)

LabelTotalPrice2 = tk.Label(subFrameOfLeftBottom2,text = "Total Payable: ",bg = yellowDullBg,font = ("Arial",16,"bold"),wraplength= 190)
LabelTotalPrice2.place(relx = 0.0,rely = 0.0,anchor = tk.NW)

# displays total price with red bg
totalPriceStringVar = tk.StringVar()
LabelTotalPrice = tk.Label(subFrameOfLeftBottom2,text = TotalBill,bg = maroonBg,font = ("Arial",20,"bold"),wraplength=190,fg = "white",textvariable=totalPriceStringVar)
LabelTotalPrice.place(relwidth = 1,relheight = 0.5,relx = 0.5,rely = 0.75,anchor = tk.CENTER)

# 3
subFrameOfLeftBottom3 = tk.Frame(frameMainOfPartitionsLeftBottom,relief="solid",bg = DarkSkinBg,bd = 2)
subFrameOfLeftBottom3.place(relwidth=1,relheight=0.5,relx = 0.0,rely = 1,anchor= tk.SW)
# LabelCashierInfoHead = tk.Label(subFrameOfLeftBottom3,text = f"Cashier Info: \n\nName: {cashier_data[index][2]}\nCashier-Id: {cashier_data[index][3]}\nShift: {cashier_data[index][4]}",bg = DarkSkinBg,wraplength= 190,fg = "white",font = ("",12,""))
# LabelCashierInfoHead.place(relx = 0.0,rely = 0.0,anchor = tk.NW)



# main center frame of menu between top left and right frame---------


centerMainFrameBwLeftRightTop = tk.Frame(mainWindow,bg = creamBg,relief="solid",bd = 1)
centerMainFrameBwLeftRightTop.place(relheight=0.97,relwidth=0.580,relx = 0.25,rely = 0.03,anchor = tk.NW)
# frame of menu pizza shawarma burger fries drink
frameMainMenu = tk.Frame(centerMainFrameBwLeftRightTop,bg = creamBg,relief="solid",bd = 2)
frameMainMenu.place(relwidth=1,relheight=0.675,relx = 0.0,rely=0.0,anchor=tk.NW)

# frame of pizza--------------
framePizza = tk.Frame(frameMainMenu,bg = creamBg ,relief="solid",bd = 1)
framePizza.place(relheight=1,relwidth=0.2,relx = 0.0,rely = 0.0,anchor=tk.NW)
frameHeadPizza = tk.Frame(framePizza,bg = creamBg,bd = 1,relief="solid")
frameHeadPizza.place(relwidth=1,relheight=0.1,relx = 0.0,rely = 0.0,anchor = tk.NW)
labelHeadPizza = tk.Label(frameHeadPizza,text = "PIZZA",bg = creamBg,font = ("Arial", 18,"bold"))
labelHeadPizza.place(relwidth=1,relheight=1,relx=0.0,rely=0.0,anchor = tk.NW)
frameBodyPizza = tk.Frame(framePizza,bg= creamBg)
frameBodyPizza.place(relheight=0.9,relwidth=1,relx = 0.0,rely = 0.1,anchor = tk.NW)

pizzaImage = ImageTk.PhotoImage(Image.open("images/pizza.png"))
labelPizzaImage = tk.Label(frameBodyPizza,image = pizzaImage)
labelPizzaImage.place(relwidth=1,relheight=0.3,relx = 0.5,rely = 0.15,anchor = tk.CENTER)

# all drop downs of pizza menu 

labelPizzaFlavorsDropDown = tk.Label(frameBodyPizza,text = "Select Flavor : ",bg = creamBg)
labelPizzaFlavorsDropDown.place(relx = 0.1,rely = 0.32,anchor=tk.NW)

pizzaFlavorsDropDown = ttk.Combobox(frameBodyPizza,values=pizza_flavors)
pizzaFlavorsDropDown.place(relx = 0.5,rely = 0.4,anchor=tk.CENTER)

labelPizzaSizesDropDown = tk.Label(frameBodyPizza,text = "Select size : ",bg = creamBg)
labelPizzaSizesDropDown.place(relx = 0.1,rely = 0.45,anchor=tk.NW)

pizzaSizesDropDown = ttk.Combobox(frameBodyPizza,values = pizza_sizes)
pizzaSizesDropDown.place(relx = 0.5,rely = 0.53,anchor=tk.CENTER)

labelPizzaTopingsDropDown = tk.Label(frameBodyPizza,text = "Select Extra Toppings : ",bg = creamBg)
labelPizzaTopingsDropDown.place(relx = 0.1,rely = 0.6,anchor=tk.NW)

pizzaToppingsDropDown = ttk.Combobox(frameBodyPizza,values = pizza_topping)
pizzaToppingsDropDown.place(relx = 0.5,rely = 0.68,anchor=tk.CENTER)

# spin box
spinboxVarPizza = tk.StringVar(value = "1")

label = tk.Label(frameBodyPizza, text="Select Quantity:",bg = creamBg)
label.place(relx = 0.35,rely = 0.75,anchor=tk.CENTER)

quantitySpinboxPizza = tk.Spinbox(frameBodyPizza, from_=1, to=100, width=5,textvariable=spinboxVarPizza)
quantitySpinboxPizza.place(relx = 0.8,rely = 0.75,anchor=tk.CENTER)

# confirm button of pizza menu

buttonConfirmMenu = tk.Button(frameBodyPizza,text = "CONFIRM",bg = "#A71E20",fg = "white",command = funcPizzaSelection)
buttonConfirmMenu.place(relwidth=0.5,relheight=0.1,relx = 0.5,rely = 0.9,anchor = tk.CENTER)


# frame of burger---------------


frameBurger = tk.Frame(frameMainMenu,bg = creamBg ,relief="solid",bd = 1)
frameBurger.place(relheight=1,relwidth=0.2,relx = 0.2,rely = 0.0,anchor=tk.NW)
frameHeadBurger = tk.Frame(frameBurger,bg = creamBg,bd = 1,relief="solid")
frameHeadBurger.place(relwidth=1,relheight=0.1,relx = 0.0,rely = 0.0,anchor = tk.NW)
labelHeadBurger = tk.Label(frameHeadBurger,text = "BURGER",bg = creamBg,font = ("Arial", 18,"bold"))
labelHeadBurger.place(relwidth=1,relheight=1,relx=0.0,rely=0.0,anchor = tk.NW)
frameBodyBurger = tk.Frame(frameBurger,bg= creamBg)
frameBodyBurger.place(relheight=0.9,relwidth=1,relx = 0.0,rely = 0.1,anchor = tk.NW)

burgerImage = Image.open("images/burger.png")
burgerPhotoImage = ImageTk.PhotoImage(burgerImage)
labelBurgerImage = tk.Label(frameBodyBurger,image = burgerPhotoImage)
labelBurgerImage.place(relwidth=1,relheight=0.3,relx = 0.5,rely = 0.15,anchor = tk.CENTER)

labelBurgerFlavorsDropDown = tk.Label(frameBodyBurger,text = "Select Burger : ",bg = creamBg)
labelBurgerFlavorsDropDown.place(relx = 0.1,rely = 0.32,anchor=tk.NW)

burgerFlavorsDropDown = ttk.Combobox(frameBodyBurger,values=burger_flavors)
burgerFlavorsDropDown.place(relx = 0.5,rely = 0.4,anchor=tk.CENTER)
# ------------------
labelBurgerSaucesDropDown = tk.Label(frameBodyBurger,text = "Select Extra Sauces : ",bg = creamBg)
labelBurgerSaucesDropDown.place(relx = 0.1,rely = 0.6,anchor=tk.NW)

BurgerSaucesDropDown = ttk.Combobox(frameBodyBurger,values = sauces)
BurgerSaucesDropDown.place(relx = 0.5,rely = 0.68,anchor=tk.CENTER)

# spin box
spinboxVarBurger = tk.StringVar(value = "1")

label = tk.Label(frameBodyBurger, text="Select Quantity:",bg = creamBg)
label.place(relx = 0.35,rely = 0.75,anchor=tk.CENTER)

quantitySpinboxBurger = tk.Spinbox(frameBodyBurger, from_=1, to=100, width=5,textvariable=spinboxVarBurger)
quantitySpinboxBurger.place(relx = 0.8,rely = 0.75,anchor=tk.CENTER)

# confirm button of burger menu

buttonConfirmMenu = tk.Button(frameBodyBurger,text = "CONFIRM",bg = "#A71E20",fg = "white",command = funcBurgerSelection)
buttonConfirmMenu.place(relwidth=0.5,relheight=0.1,relx = 0.5,rely = 0.9,anchor = tk.CENTER)



# frame of shawarma------------



frameShawarma = tk.Frame(frameMainMenu,bg = creamBg ,relief="solid",bd = 1)
frameShawarma.place(relheight=1,relwidth=0.2,relx = 0.4,rely = 0.0,anchor=tk.NW)
frameHeadShawarma = tk.Frame(frameShawarma,bg = creamBg,bd = 1,relief="solid")
frameHeadShawarma.place(relwidth=1,relheight=0.1,relx = 0.0,rely = 0.0,anchor = tk.NW)
labelHeadShawarma = tk.Label(frameHeadShawarma,text = "SHAWARMA",bg = creamBg,font = ("Arial", 18,"bold"))
labelHeadShawarma.place(relwidth=1,relheight=1,relx=0.0,rely=0.0,anchor = tk.NW)
frameBodyShawarma = tk.Frame(frameShawarma,bg= creamBg)
frameBodyShawarma.place(relheight=0.9,relwidth=1,relx = 0.0,rely = 0.1,anchor = tk.NW)
# shawarma image
shawarmaImage = Image.open("images/shawarma.png")
shawarmaPhotoImage = ImageTk.PhotoImage(shawarmaImage)
labelBurgerImage = tk.Label(frameBodyShawarma,image = shawarmaPhotoImage)
labelBurgerImage.place(relwidth=1,relheight=0.3,relx = 0.5,rely = 0.15,anchor = tk.CENTER)

# all dropdowns of shawarma menu
labelShawarmaFlavorsDropDown = tk.Label(frameBodyShawarma,text = "Select Flavor : ",bg = creamBg)
labelShawarmaFlavorsDropDown.place(relx = 0.1,rely = 0.32,anchor=tk.NW)

ShawarmaFlavorsDropDown = ttk.Combobox(frameBodyShawarma,values=shawarma_flavors)
ShawarmaFlavorsDropDown.place(relx = 0.5,rely = 0.4,anchor=tk.CENTER)

labelShawarmaSizesDropDown = tk.Label(frameBodyShawarma,text = "Select size : ",bg = creamBg)
labelShawarmaSizesDropDown.place(relx = 0.1,rely = 0.45,anchor=tk.NW)

ShawarmaSizesDropDown = ttk.Combobox(frameBodyShawarma,values = sha_fri_sizes)
ShawarmaSizesDropDown.place(relx = 0.5,rely = 0.53,anchor=tk.CENTER)

labelShawarmaSaucesDropDown = tk.Label(frameBodyShawarma,text = "Select Extra sauces : ",bg = creamBg)
labelShawarmaSaucesDropDown.place(relx = 0.1,rely = 0.6,anchor=tk.NW)

ShawarmaSaucesDropDown = ttk.Combobox(frameBodyShawarma,values = sauces)
ShawarmaSaucesDropDown.place(relx = 0.5,rely = 0.68,anchor=tk.CENTER)

# spin box
spinboxvarShawarma = tk.StringVar(value = "1")

label = tk.Label(frameBodyShawarma, text="Select Quantity:",bg = creamBg)
label.place(relx = 0.35,rely = 0.75,anchor=tk.CENTER)

quantitySpinboxShawarma = tk.Spinbox(frameBodyShawarma, from_=1, to=100, width=5,textvariable=spinboxvarShawarma)
quantitySpinboxShawarma.place(relx = 0.8,rely = 0.75,anchor=tk.CENTER)

# confirm button of shawarma menu

buttonConfirmMenu = tk.Button(frameBodyShawarma,text = "CONFIRM",bg = "#A71E20",fg = "white",command = funcShawarmaSelection)
buttonConfirmMenu.place(relwidth=0.5,relheight=0.1,relx = 0.5,rely = 0.9,anchor = tk.CENTER)


# frame of fries---------------------
frameFries = tk.Frame(frameMainMenu,bg = creamBg ,relief="solid",bd = 1)
frameFries.place(relheight=1,relwidth=0.2,relx = 0.6,rely = 0.0,anchor=tk.NW)
frameHeadFries = tk.Frame(frameFries,bg = creamBg,bd = 1,relief="solid")
frameHeadFries.place(relwidth=1,relheight=0.1,relx = 0.0,rely = 0.0,anchor = tk.NW)
labelHeadFries = tk.Label(frameHeadFries,text = "FRIES",bg = creamBg,font = ("Arial", 18,"bold"))
labelHeadFries.place(relwidth=1,relheight=1,relx=0.0,rely=0.0,anchor = tk.NW)
frameBodyFries = tk.Frame(frameFries,bg= creamBg)
frameBodyFries.place(relheight=0.9,relwidth=1,relx = 0.0,rely = 0.1,anchor = tk.NW)

friesImage = Image.open("images/fries.png")
friesPhotoImage = ImageTk.PhotoImage(friesImage)
labelFriesImage = tk.Label(frameBodyFries,image = friesPhotoImage)
labelFriesImage.place(relwidth=1,relheight=0.3,relx = 0.5,rely = 0.15,anchor = tk.CENTER)

# all dropdowns of fries menu
labelFriesFlavorsDropDown = tk.Label(frameBodyFries,text = "Select Flavor : ",bg = creamBg)
labelFriesFlavorsDropDown.place(relx = 0.1,rely = 0.32,anchor=tk.NW)

FriesFlavorsDropDown = ttk.Combobox(frameBodyFries,values=fries_flavors)
FriesFlavorsDropDown.place(relx = 0.5,rely = 0.4,anchor=tk.CENTER)

labelFriesSizesDropDown = tk.Label(frameBodyFries,text = "Select size : ",bg = creamBg)
labelFriesSizesDropDown.place(relx = 0.1,rely = 0.45,anchor=tk.NW)

FriesSizesDropDown = ttk.Combobox(frameBodyFries,values = sha_fri_sizes)
FriesSizesDropDown.place(relx = 0.5,rely = 0.53,anchor=tk.CENTER)

labelFriesSaucesDropDown = tk.Label(frameBodyFries,text = "Select Extra sauces : ",bg = creamBg)
labelFriesSaucesDropDown.place(relx = 0.1,rely = 0.6,anchor=tk.NW)

FriesSaucesDropDown = ttk.Combobox(frameBodyFries,values = sauces)
FriesSaucesDropDown.place(relx = 0.5,rely = 0.68,anchor=tk.CENTER)

# spin box
spinboxvarFries = tk.StringVar(value = "1")

label = tk.Label(frameBodyFries, text="Select Quantity:",bg = creamBg)
label.place(relx = 0.35,rely = 0.75,anchor=tk.CENTER)

quantitySpinboxFries = tk.Spinbox(frameBodyFries, from_=1, to=100, width=5,textvariable=spinboxvarFries)
quantitySpinboxFries.place(relx = 0.8,rely = 0.75,anchor=tk.CENTER)

# confirm button of fries menu

buttonConfirmMenu = tk.Button(frameBodyFries,text = "CONFIRM",bg = "#A71E20",fg = "white",command = funcFriesSelection)
buttonConfirmMenu.place(relwidth=0.5,relheight=0.1,relx = 0.5,rely = 0.9,anchor = tk.CENTER)


# frame of drinks-----------------------
frameDrinks = tk.Frame(frameMainMenu,bg = creamBg ,relief="solid",bd = 1)
frameDrinks.place(relheight=1,relwidth=0.2,relx = 0.8,rely = 0.0,anchor=tk.NW)
frameHeadDrinks = tk.Frame(frameDrinks,bg = creamBg,bd = 1,relief="solid")
frameHeadDrinks.place(relwidth=1,relheight=0.1,relx = 0.0,rely = 0.0,anchor = tk.NW)
labelHeadDrinks = tk.Label(frameHeadDrinks,text = "DRINKS",bg = creamBg,font = ("Arial", 18,"bold"))
labelHeadDrinks.place(relwidth=1,relheight=1,relx=0.0,rely=0.0,anchor = tk.NW)

frameBodyDrinks = tk.Frame(frameDrinks,bg= creamBg)
frameBodyDrinks.place(relheight=0.9,relwidth=1,relx = 0.0,rely = 0.1,anchor = tk.NW)

DrinksImage = Image.open("images/drinks.png")
DrinksPhotoImage = ImageTk.PhotoImage(DrinksImage)
labelDrinksImage = tk.Label(frameBodyDrinks,image = DrinksPhotoImage)
labelDrinksImage.place(relwidth=1,relheight=0.3,relx = 0.5,rely = 0.15,anchor = tk.CENTER)

# spin box
spinboxVarDrinks = tk.StringVar(value = "1")

label = tk.Label(frameBodyDrinks, text="Select Quantity:",bg = creamBg)
label.place(relx = 0.35,rely = 0.75,anchor=tk.CENTER)

quantitySpinboxDrinks = tk.Spinbox(frameBodyDrinks, from_=1, to=100, width=5,textvariable= spinboxVarDrinks)
quantitySpinboxDrinks.place(relx = 0.8,rely = 0.75,anchor=tk.CENTER)

# all dropdowns of drink menu
labelDrinksDropDown = tk.Label(frameBodyDrinks,text = "Select Drink : ",bg = creamBg)
labelDrinksDropDown.place(relx = 0.1,rely = 0.32,anchor=tk.NW)

DrinksDropDown = ttk.Combobox(frameBodyDrinks,values=drinks)
DrinksDropDown.place(relx = 0.5,rely = 0.4,anchor=tk.CENTER)

labelDrinksSizesDropDown = tk.Label(frameBodyDrinks,text = "Select size : ",bg = creamBg)
labelDrinksSizesDropDown.place(relx = 0.1,rely = 0.45,anchor=tk.NW)

DrinksSizesDropdown = ttk.Combobox(frameBodyDrinks,values=drinks_sizes)
DrinksSizesDropdown.place(relx = 0.5,rely = 0.53,anchor=tk.CENTER)

# confirm button of drink menu

buttonConfirmMenu = tk.Button(frameBodyDrinks,text = "CONFIRM",bg = "#A71E20",fg = "white",command = funcDrinksSelection)
buttonConfirmMenu.place(relwidth=0.5,relheight=0.1,relx = 0.5,rely = 0.9,anchor = tk.CENTER)


# main right frame (family deals)
frameRightFamilyDeals = tk.Frame(frameMainUnderTopBar,bg = creamBg,relief="solid",bd = 2)
frameRightFamilyDeals.place(relwidth=0.17,relheight=1,relx = 1,rely = 0.0,anchor = tk.NE)
#  top bar of right frame (family deals)
topBarOfFrameRightFamilyDeals = tk.Frame(frameRightFamilyDeals,bg = maroonBg,relief="solid",bd = 1)
topBarOfFrameRightFamilyDeals.place(relwidth=1,relheight=0.05,relx = 1,rely = 0.0,anchor = tk.NE)

labelHeadFamilyDeals = tk.Label(topBarOfFrameRightFamilyDeals,text = "FAMILY DEALS" , fg = "white",bg = maroonBg,font = ("Arial",20,"bold"))
labelHeadFamilyDeals.place(relwidth=1,relheight=1)


# frames of all deals 
frameAllDeals = tk.Frame(frameRightFamilyDeals,bg = yellowDullBg,relief = "solid",bd = 2)
frameAllDeals.place(relwidth=1,relheight=0.88,relx = 0.0,rely = 0.05)
# subframes of all deals

deal1 = tk.Frame(frameAllDeals,bg = yellowDullBg,relief="solid",bd = 1)
deal1.place(relwidth=0.5,relheight=0.2,relx = 0.0,rely = 0.0,anchor = tk.NW)
dealHead,dealContents  = funcDealContents(1)
deal1Content = tk.Button(deal1,text = f"{dealHead}\n{dealContents}",bg = yellowDullBg,font = ("Arial",10),wraplength=120)
deal1Content.place(relx=0.0,rely=0.0,anchor =tk.NW,relwidth = 1,relheight=1)

deal2 = tk.Frame(frameAllDeals,bg = yellowDullBg,relief="solid",bd = 1)
deal2.place(relwidth=0.5,relheight=0.2,relx = 0.0,rely = 0.2,anchor = tk.NW)
dealHead,dealContents  = funcDealContents(2)
deal2Content = tk.Button(deal2,text = f"{dealHead}\n{dealContents}",bg = yellowDullBg,font = ("Arial",10),wraplength=120)
deal2Content.place(relx=0.0,rely=0.0,anchor =tk.NW,relwidth = 1,relheight=1)

deal3 = tk.Frame(frameAllDeals,bg = yellowDullBg,relief="solid",bd = 1)
deal3.place(relwidth=0.5,relheight=0.2,relx = 0.0,rely = 0.4,anchor = tk.NW)
dealHead,dealContents  = funcDealContents(3)
deal3Content = tk.Button(deal3,text = f"{dealHead}\n{dealContents}",bg = yellowDullBg,font = ("Arial",10),wraplength=120)
deal3Content.place(relx=0.0,rely=0.0,anchor =tk.NW,relwidth = 1,relheight=1)

deal4 = tk.Frame(frameAllDeals,bg = yellowDullBg,relief="solid",bd = 1)
deal4.place(relwidth=0.5,relheight=0.2,relx = 0.0,rely = 0.6,anchor = tk.NW)
dealHead,dealContents  = funcDealContents(4)
deal4Content = tk.Button(deal4,text = f"{dealHead}\n{dealContents}",bg = yellowDullBg,font = ("Arial",10),wraplength=120)
deal4Content.place(relx=0.0,rely=0.0,anchor =tk.NW,relwidth = 1,relheight=1)

deal5 = tk.Frame(frameAllDeals,bg = yellowDullBg,relief="solid",bd = 1)
deal5.place(relwidth=0.5,relheight=0.2,relx = 0.0,rely = 0.8,anchor = tk.NW)
dealHead,dealContents  = funcDealContents(5)
deal5Content = tk.Button(deal5,text = f"{dealHead}\n{dealContents}",bg = yellowDullBg,font = ("Arial",10),wraplength=120)
deal5Content.place(relx=0.0,rely=0.0,anchor =tk.NW,relwidth = 1,relheight=1)

deal6 = tk.Frame(frameAllDeals,bg = yellowDullBg,relief="solid",bd = 1)
deal6.place(relwidth=0.5,relheight=0.2,relx = 0.5,rely = 0.0,anchor = tk.NW)
dealHead,dealContents  = funcDealContents(6)
deal6Content = tk.Button(deal6,text = f"{dealHead}\n{dealContents}",bg = yellowDullBg,font = ("Arial",10),wraplength=120)
deal6Content.place(relx=0.0,rely=0.0,anchor =tk.NW,relwidth = 1,relheight=1)

deal7 = tk.Frame(frameAllDeals,bg = yellowDullBg,relief="solid",bd = 1)
deal7.place(relwidth=0.5,relheight=0.2,relx = 0.5,rely = 0.2,anchor = tk.NW)
dealHead,dealContents  = funcDealContents(7)
deal7Content = tk.Button(deal7,text = f"{dealHead}\n{dealContents}",bg = yellowDullBg,font = ("Arial",10),wraplength=120)
deal7Content.place(relx=0.0,rely=0.0,anchor =tk.NW,relwidth = 1,relheight=1)

deal8 = tk.Frame(frameAllDeals,bg = yellowDullBg,relief="solid",bd = 1)
deal8.place(relwidth=0.5,relheight=0.2,relx = 0.5,rely = 0.4,anchor = tk.NW)
dealHead,dealContents  = funcDealContents(8)
deal8Content = tk.Button(deal8,text = f"{dealHead}\n{dealContents}",bg = yellowDullBg,font = ("Arial",10),wraplength=120)
deal8Content.place(relx=0.0,rely=0.0,anchor =tk.NW,relwidth = 1,relheight=1)

deal9 = tk.Frame(frameAllDeals,bg = yellowDullBg,relief="solid",bd = 1)
deal9.place(relwidth=0.5,relheight=0.2,relx = 0.5,rely = 0.6,anchor = tk.NW)
dealHead,dealContents  = funcDealContents(9)
deal9Content = tk.Button(deal9,text = f"{dealHead}\n{dealContents}",bg = yellowDullBg,font = ("Arial",10),wraplength=120)
deal9Content.place(relx=0.0,rely=0.0,anchor =tk.NW,relwidth = 1,relheight=1)

deal10 = tk.Frame(frameAllDeals,bg = yellowDullBg,relief="solid",bd = 1)
deal10.place(relwidth=0.5,relheight=0.2,relx = 0.5,rely = 0.8,anchor = tk.NW)
dealHead,dealContents  = funcDealContents(10)
deal10Content = tk.Button(deal10,text = f"{dealHead}\n{dealContents}",bg = yellowDullBg,font = ("Arial",10),wraplength=120)
deal10Content.place(relx=0.0,rely=0.0,anchor =tk.NW,relwidth = 1,relheight=1)



# dealContents = ""
# dealContentsFinal = ""
# for i in range(10):
#     dealHead = f"\n{family_deals[i][0]}\n"
#     for j in range(len(family_deals[i][1])):
#         dealContents = f"{family_deals[i][1][j][0]} x {family_deals[i][1][j][1]}"
        

    

# buttons framea
frameButtonsFamilyDeals = tk.Frame(frameRightFamilyDeals,bg = "orange",relief="solid",bd = 2)
frameButtonsFamilyDeals.place(relwidth=1,relheight=0.07,relx = 1,rely = 0.972,anchor = tk.SE)


buttonAddDeal = tk.Button(frameButtonsFamilyDeals,text= "ADD DEAL",bg = maroonBg,font=("Arial",12,"bold"),fg = "white").place(relheight=0.9,relwidth=0.47,relx = 0.25,rely=0.5,anchor = tk.CENTER)
buttonRemoveDeal = tk.Button(frameButtonsFamilyDeals,text= "DEL DEAL",bg = maroonBg,font=("Arial",12,"bold"),fg = "white").place(relheight=0.9,relwidth=0.47,relx = 0.73,rely=0.5,anchor = tk.CENTER)


mainWindow.mainloop()
