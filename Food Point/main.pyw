import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from items import *
from user_data import *
import random
row = 1
allLabelsItemsBill = []
srNo = random.randint(10000000,99999999)
gst = 0
totalBillItem = 0
TotalBill = 0
Totalgst = 0
orderNo = 0
# this function clears order whenever CLEARBUTTON is pressed
def funcclearOrder():
    pass

# recieptPrinter() function creates a .txt file with name of the order no. and saves the bill in a formatted way and we can print it later if needed
def recieptPrinter():
    f = open(f"Food Point/reciepts/{orderNo}.txt","w")

    f.close()
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
    # to update the total price after each 500 millisecond
    mainWindow.after(500, updateTotalPrice) 

# this function adds new items to the bill management section when ever a new item is confirmed
def updateBillManagement(quantity,gst,totalBillItem,ProductName):
    global row,TotalBill,Totalgst
    TotalBill += totalBillItem # adds the price current item in the total bill
    Totalgst += gst # adds the gst applied on the current item to the total gst variable
    # following labels to display data in bill management frame
    labelSrNo = tk.Label(frameBodyBillManagement,text = f"{srNo}",bg = "white")
    labelSrNo.grid(column=0,row = row)
    labelProductName = tk.Label(frameBodyBillManagement,text = f"{ProductName}",wraplength=110,bg = "white")
    labelProductName.grid(column = 1,row=row,padx = 2)
    labelQty = tk.Label(frameBodyBillManagement,text = f"{quantity}",bg = "white",wraplength=30)
    labelQty.grid(column = 2,row=row,padx = 2)
    labelGst = tk.Label(frameBodyBillManagement,text = f"{gst:.1f}",bg = "white",wraplength=30)
    labelGst.grid(column = 3,row=row,padx = 2)
    labelPrice = tk.Label(frameBodyBillManagement,text = f"{totalBillItem}",bg = "white",wraplength=30)
    labelPrice.grid(column = 4,row=row,padx = 2)
    # creating feature to delete the item by double clicking it
    # following list contains all the labels in bill management frame related to a single item
    allLabelsItemsBill = [labelSrNo,labelProductName,labelQty,labelGst,labelPrice]
    # following for loop binds double click event to all the labels that were previously added to the list (allLabelsItemsBill) and whenever the label is double-clicked.
    for item in allLabelsItemsBill:
        item.bind("<Double-Button-1>",lambda event,lbls = allLabelsItemsBill,gst1 = gst,totalBillItem1  = totalBillItem :funcDeleteItemFromBill(event,lbls,gst1,totalBillItem1))
    row += 1  
    # calling following fucntion to update the total price 
    updateTotalPrice()
# following function is triggered whenever the item is double clicked and deletes that label and its corresponding
def funcDeleteItemFromBill(event,allLabelsItemBill,gst,totalBillItem):
    # following fucntion is called so that the total price and total gst is updated after the item is deleted
    updatePriceDeletedItem(gst,totalBillItem)
    for lbl in allLabelsItemBill:
        lbl.destroy()
# following fucntion is used to get data from the pizza selection dropdowns and spinbox, it also calculates the price according the quantity
def funcPizzaSelection():
    Name = "Piz"
    # recieving value from dropdowns and spinbox
    selectedFlavor = pizzaFlavorsDropDown.get()
    selectedSize = pizzaSizesDropDown.get()
    quantity = int(quantitySpinboxPizza.get())
    # calculating total pizza prices
    indexSelectedSize = int(pizza_sizes[0].index(selectedSize))
    PizzaPrice = pizza_sizes[1][indexSelectedSize]
    totalBillPizza =  (PizzaPrice * quantity)
    totalBillPizza += float((totalBillPizza*17.5)/100)
    gst = (totalBillPizza*17.5)/100
    # setting spinbox to 1 
    spinboxVarPizza.set("1")
    # setting all dropdowns to ""
    pizzaFlavorsDropDown.set("")
    pizzaSizesDropDown.set("")
    pizzaToppingsDropDown.set("")
    # a comprehensive product name is made to display in the bill management section
    ProductName = f"{Name}: {selectedFlavor}-{pizza_sizes[2][indexSelectedSize]}"
    # updateBillManagement function is called to update the bill with the current pizza item
    updateBillManagement(quantity,gst,totalBillPizza,ProductName)
# following function is used to get data from burger selection dropdowns and spinbox, it also calculates the price according the quantity
def funcBurgerSelection():
    Name = "Bur"
    # recieving data from the dropdowns and list boxes
    selectedFlavor = burgerFlavorsDropDown.get()
    quantity = int(quantitySpinboxBurger.get())
    indexSelectedBurger = burger_flavors[0].index(selectedFlavor)
    # calculating the total of the burger item and gst applied
    totalBillBurger =  (burger_flavors[1][indexSelectedBurger] * quantity)
    totalBillBurger += float((totalBillBurger*17.5)/100)
    gst = (totalBillBurger*17.5)/100
    # setting spinbox to 1 
    spinboxVarBurger.set("1")
    # setting all dropdowns to ""
    burgerFlavorsDropDown.set("")
    BurgerSaucesDropDown.set("")
    # making a comprehensive product name to display it in the bill management
    ProductName = f"{Name}: {selectedFlavor}"
    # updating the bill managing table
    updateBillManagement(quantity,gst,totalBillBurger,ProductName)
# following function is used to get data from shawarma selection dropdowns and spinbox, it also calculates the price according the quantity 
def funcShawarmaSelection():
    Name = "Sha"
    # recieving value from dropdowns and spinbox
    selectedFlavor = ShawarmaFlavorsDropDown.get()
    selectedSize = ShawarmaSizesDropDown.get()
    quantity = int(quantitySpinboxShawarma.get())
    # calculating total shawarma prices and gst applied on the item
    indexSelectedSize = int(shawarma_sizes[0].index(selectedSize))
    ShawarmaPrice = shawarma_sizes[1][indexSelectedSize]
    totalBillShawarma =  (ShawarmaPrice * quantity)
    totalBillShawarma += float((totalBillShawarma*17.5)/100)
    gst = (totalBillShawarma*17.5)/100
    # setting spinbox to 1 
    spinboxvarShawarma.set("1")
    # setting all dropdowns to ""
    ShawarmaFlavorsDropDown.set("")
    ShawarmaSizesDropDown.set("")
    ShawarmaSaucesDropDown.set("")
    # comprehensive product name 
    ProductName = f"{Name}: {selectedFlavor}-{pizza_sizes[2][indexSelectedSize]}"
    # updating bill manager
    updateBillManagement(quantity,gst,totalBillShawarma,ProductName)
# following function is used to get data from fries selection dropdowns and spinbox, it also calculates the price according the quantity 
def funcFriesSelection():
    Name = "Fri"
    # recieving value from dropdowns and spinbox
    selectedFlavor = FriesFlavorsDropDown.get()
    selectedSize = FriesSizesDropDown.get()
    quantity = int(quantitySpinboxFries.get())
    # calculating total fries prices and total gst applied
    indexSelectedSize = int(fries_sizes[0].index(selectedSize))
    FriesPrice = fries_sizes[1][indexSelectedSize]
    totalBillFries =  (FriesPrice * quantity)
    totalBillFries += float((totalBillFries*17.5)/100)
    gst = (totalBillFries*17.5)/100
    # setting spinbox to 1 
    spinboxvarFries.set("1")
    # setting all dropdowns to ""
    FriesFlavorsDropDown.set("")
    FriesSizesDropDown.set("")
    FriesSaucesDropDown.set("")
    # comprehensive product name
    ProductName = f"{Name}: {selectedFlavor}-{pizza_sizes[2][indexSelectedSize]}"
    # updating bill manager
    updateBillManagement(quantity,gst,totalBillFries,ProductName)
# following function is used to get data from DRINKS selection dropdowns and spinbox, it also calculates the price according the quantity 
def funcDrinksSelection():
    Name = "Drink"
    # recieving value from dropdowns and spinbox
    selectedDrink = DrinksDropDown.get()
    selectedSize = DrinksSizesDropdown.get()
    quantity = int(quantitySpinboxDrinks.get())
    # calculating total fries prices
    indexSelectedSize = int(drinks_sizes[0].index(selectedSize))
    DrinksPrice = drinks_sizes[1][indexSelectedSize]
    totalBillDrinks =  (DrinksPrice * quantity)
    totalBillDrinks += float((totalBillDrinks*17.5)/100)
    gst = (totalBillDrinks*17.5)/100
    # setting spinbox to 1 
    spinboxVarDrinks.set("1")
    # setting all dropdowns to ""
    DrinksDropDown.set("")
    DrinksSizesDropdown.set("")
    # Comprehensive product name
    ProductName = f"{Name}: {selectedDrink}-{drinks_sizes[0][indexSelectedSize]}"
    # updating bill manager
    updateBillManagement(quantity,gst,totalBillDrinks,ProductName)




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
frameTopBar = tk.Frame(mainWindow,bg = "red",relief="solid",bd = 2).place(relwidth= 1,relheight=0.03,relx = 0.0,rely = 0.0,anchor = tk.NW)

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
buttonPrintReciept = tk.Button(frameBodyBillConfirm,text= "PRINT RECIEPT",bg= maroonBg,fg = "white",font = ("Arial",16,"bold"),command = recieptPrinter)
buttonPrintReciept.place(relwidth=0.48,relheight = 0.9,relx = 0.75,rely = 0.5,anchor = tk.CENTER)
# Create a vertical scrollbar for the canvas
scrollbar = ttk.Scrollbar(frameBodyBillManagement, orient=tk.VERTICAL, command=canvasBill.yview)
scrollbar.place(relheight=1,relx = 1,rely = 0.0,anchor = tk.NE)

# Configure the canvas and scrollbar
canvasBill.configure(yscrollcommand=scrollbar.set)

frameBodyBillManagement.update_idletasks()
canvasBill.configure(scrollregion=canvasBill.bbox("all"))
# --------------
headContentBillManagement = tk.Label(frameBodyBillManagement,text = "Sr.No")
headContentBillManagement.grid(row = 0,column = 0,padx = 20,pady = 5)

headContentBillManagement = tk.Label(frameBodyBillManagement,text = "Product Name")
headContentBillManagement.grid(row = 0,column = 1,padx = 20,pady = 5)

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
LabelCashierInfoHead = tk.Label(subFrameOfLeftBottom3,text = f"Cashier Info: \n\nName: {cashier_data[0][1]}\nCashier-Id: {cashier_data[0][3]}\nShift: {cashier_data[0][4]}",bg = DarkSkinBg,wraplength= 190,fg = "white",font = ("",12,""))
LabelCashierInfoHead.place(relx = 0.0,rely = 0.0,anchor = tk.NW)
































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

pizzaImage = Image.open("Food Point/images/pizza.png")
pizzaPhotoImage = ImageTk.PhotoImage(pizzaImage)
labelPizzaImage = tk.Label(frameBodyPizza,image = pizzaPhotoImage)
labelPizzaImage.place(relwidth=1,relheight=0.3,relx = 0.5,rely = 0.15,anchor = tk.CENTER)

# all drop downs of pizza menu 

labelPizzaFlavorsDropDown = tk.Label(frameBodyPizza,text = "Select Flavor : ",bg = creamBg)
labelPizzaFlavorsDropDown.place(relx = 0.1,rely = 0.32,anchor=tk.NW)

pizzaFlavorsDropDown = ttk.Combobox(frameBodyPizza,values=pizza_flavors)
pizzaFlavorsDropDown.place(relx = 0.5,rely = 0.4,anchor=tk.CENTER)

labelPizzaSizesDropDown = tk.Label(frameBodyPizza,text = "Select size : ",bg = creamBg)
labelPizzaSizesDropDown.place(relx = 0.1,rely = 0.45,anchor=tk.NW)

pizzaSizesDropDown = ttk.Combobox(frameBodyPizza,values = pizza_sizes[0])
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

burgerImage = Image.open("Food Point/images/burger.png")
burgerPhotoImage = ImageTk.PhotoImage(burgerImage)
labelBurgerImage = tk.Label(frameBodyBurger,image = burgerPhotoImage)
labelBurgerImage.place(relwidth=1,relheight=0.3,relx = 0.5,rely = 0.15,anchor = tk.CENTER)

# all drop downs of burger menu

labelBurgerFlavorsDropDown = tk.Label(frameBodyBurger,text = "Select Burger : ",bg = creamBg)
labelBurgerFlavorsDropDown.place(relx = 0.1,rely = 0.32,anchor=tk.NW)

burgerFlavorsDropDown = ttk.Combobox(frameBodyBurger,values=burger_flavors[0])
burgerFlavorsDropDown.place(relx = 0.5,rely = 0.4,anchor=tk.CENTER)
# ------------------
labelBurgerSaucesDropDown = tk.Label(frameBodyBurger,text = "Select Extra Sauces : ",bg = creamBg)
labelBurgerSaucesDropDown.place(relx = 0.1,rely = 0.6,anchor=tk.NW)

BurgerSaucesDropDown = ttk.Combobox(frameBodyBurger,values = burger_sauces)
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
shawarmaImage = Image.open("Food Point/images/shawarma.png")
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

ShawarmaSizesDropDown = ttk.Combobox(frameBodyShawarma,values = shawarma_sizes[0])
ShawarmaSizesDropDown.place(relx = 0.5,rely = 0.53,anchor=tk.CENTER)

labelShawarmaSaucesDropDown = tk.Label(frameBodyShawarma,text = "Select Extra sauces : ",bg = creamBg)
labelShawarmaSaucesDropDown.place(relx = 0.1,rely = 0.6,anchor=tk.NW)

ShawarmaSaucesDropDown = ttk.Combobox(frameBodyShawarma,values = burger_sauces)
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

friesImage = Image.open("Food Point/images/fries.png")
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

FriesSizesDropDown = ttk.Combobox(frameBodyFries,values = fries_sizes[0])
FriesSizesDropDown.place(relx = 0.5,rely = 0.53,anchor=tk.CENTER)

labelFriesSaucesDropDown = tk.Label(frameBodyFries,text = "Select Extra sauces : ",bg = creamBg)
labelFriesSaucesDropDown.place(relx = 0.1,rely = 0.6,anchor=tk.NW)

FriesSaucesDropDown = ttk.Combobox(frameBodyFries,values = burger_sauces)
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

DrinksImage = Image.open("Food Point/images/drinks.png")
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

DrinksSizesDropdown = ttk.Combobox(frameBodyDrinks,values=drinks_sizes[0])
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



mainWindow.mainloop()
