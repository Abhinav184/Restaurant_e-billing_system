from tkinter import *
import random
import time
import datetime

root = Tk()
root.geometry("1600x8000")
root.title("Restaurant E-billing System")

Tops = Frame(root, width=1600, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

# =================================================================================
#                  TIME
# ================================================================================
localtime = time.asctime(time.localtime(time.time()))

lblInfo = Label(Tops, font=('arial', 50, 'bold'), text="Tasty Bites Restaurant Billing info.", fg="Sky Blue", bd=10,
                anchor='w')
lblInfo.grid(row=0, column=0)

lblInfo = Label(Tops, font=('arial', 20, 'bold'), text=localtime, fg="sky blue", bd=10, anchor='w')
lblInfo.grid(row=1, column=0)


def Ref():
    x = random.randint(10908, 500876)
    randomRef = str(x)
    rand.set(randomRef)

    if (Burger.get() == ""):
        CoBurger = 0
    else:
        CoBurger = float(Burger.get())

    if (Pizza.get() == ""):
        CoPizza = 0
    else:
        CoPizza = float(Pizza.get())

    if (FrenchFries.get() == ""):
        CoFrenchFries = 0
    else:
        CoFrenchFries = float(FrenchFries.get())

    if (Coffee.get() == ""):
        CoCoffee = 0
    else:
        CoCoffee = float(Coffee.get())

    if (Mojito.get() == ""):
        CoMojito = 0
    else:
        CoMojito = float(Mojito.get())

    if (Drinks.get() == ""):
        CoD = 0
    else:
        CoD = float(Drinks.get())

    CostofBurger = CoBurger * 50
    CostofDrinks = CoD * 30
    CostofPizza = CoPizza * 150
    CostofFrenchFries = CoFrenchFries * 60
    CostCoffee = CoCoffee * 30
    CoMojito = CoMojito * 30

    CostofMeal = "Rs", str(
        '%.2f' % (CostofBurger + CostofDrinks + CostofPizza + CostofFrenchFries + CostCoffee + CoMojito))

    PayTax = ((CostofBurger + CostofDrinks + CostofPizza + CostofFrenchFries + CostCoffee + CoMojito) * 0.2)

    TotalCost = (CostofBurger + CostofDrinks + CostofPizza + CostofFrenchFries + CostCoffee + CoMojito)

    Ser_Charge = ((CostofBurger + CostofDrinks + CostofPizza + CostofFrenchFries + CostCoffee + CoMojito) / 99)

    Service = "Rs", str('%.2f' % Ser_Charge)

    OverAllCost = "Rs", str('%.2f' % (PayTax + TotalCost + Ser_Charge))

    PaidTax = "Rs", str('%.2f' % PayTax)

    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)


def qExit():
    root.destroy()


def Reset():
    rand.set("")
    Burger.set("")
    Pizza.set("")
    FrenchFries.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Coffee.set("")
    Mojito.set("")


# ====================================Restaraunt Info 1===========================================================
rand = StringVar()
Burger = StringVar()
Pizza = StringVar()
FrenchFries = StringVar()
SubTotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
Cost = StringVar()
Coffee = StringVar()
Mojito = StringVar()

lblReference = Label(f1, font=('arial', 16, 'bold'), text="Reference", bd=16, anchor="w")
lblReference.grid(row=0, column=0)
txtReference = Entry(f1, font=('arial', 16, 'bold'), textvariable=rand, bd=10, insertwidth=4, bg="white",
                     justify='right')
txtReference.grid(row=0, column=1)

lblBurger = Label(f1, font=('arial', 16, 'bold'), text="BURGER", bd=16, anchor="w")
lblBurger.grid(row=1, column=0)
txtBurger = Entry(f1, font=('arial', 16, 'bold'), textvariable=Burger, bd=10, insertwidth=4, bg="white",
                  justify='right')
txtBurger.grid(row=1, column=1)

lblPizza = Label(f1, font=('arial', 16, 'bold'), text="PIZZA", bd=16, anchor="w")
lblPizza.grid(row=2, column=0)
txtPizza = Entry(f1, font=('arial', 16, 'bold'), textvariable=Pizza, bd=10, insertwidth=4, bg="white", justify='right')
txtPizza.grid(row=2, column=1)

lblFrenchFries = Label(f1, font=('arial', 16, 'bold'), text="FRENCH FRIES", bd=16, anchor="w")
lblFrenchFries.grid(row=3, column=0)
txtFrenchfries = Entry(f1, font=('arial', 16, 'bold'), textvariable=FrenchFries, bd=10, insertwidth=4, bg="white",
                       justify='right')
txtFrenchfries.grid(row=3, column=1)

lblCoffee = Label(f1, font=('arial', 16, 'bold'), text="COFFEE", bd=16, anchor="w")
lblCoffee.grid(row=4, column=0)
txtCoffee = Entry(f1, font=('arial', 16, 'bold'), textvariable=Coffee, bd=10, insertwidth=4, bg="white",
                  justify='right')
txtCoffee.grid(row=4, column=1)

lblMojito = Label(f1, font=('arial', 16, 'bold'), text="MOJITO/SHAKES", bd=16, anchor="w")
lblMojito.grid(row=5, column=0)
txtMojito = Entry(f1, font=('arial', 16, 'bold'), textvariable=Mojito, bd=10, insertwidth=4, bg="white",
                  justify='right')
txtMojito.grid(row=5, column=1)

# ============================================================================================================
#                                RESTAURANT INFO 2
# ========================================================================================

lblDrinks = Label(f1, font=('arial', 16, 'bold'), text="DRINKS", anchor="w")
lblDrinks.grid(row=0, column=2)
txtDrinks = Entry(f1, font=('arial', 16, 'bold'), textvariable=Drinks, bd=10, insertwidth=4, bg="white",
                  justify='right')
txtDrinks.grid(row=0, column=3)

lblCost = Label(f1, font=('arial', 16, 'bold'), text="Cost of Meal", bd=16, anchor="w")
lblCost.grid(row=1, column=2)
txtCost = Entry(f1, font=('arial', 16, 'bold'), textvariable=Cost, bd=10, insertwidth=4, bg="white", justify='right')
txtCost.grid(row=1, column=3)

lblService = Label(f1, font=('arial', 16, 'bold'), text="Service Charge", bd=16, anchor="w")
lblService.grid(row=2, column=2)
txtService = Entry(f1, font=('arial', 16, 'bold'), textvariable=Service_Charge, bd=10, insertwidth=4, bg="white",
                   justify='right')
txtService.grid(row=2, column=3)

lblStateTax = Label(f1, font=('arial', 16, 'bold'), text="State Tax", bd=16, anchor="w")
lblStateTax.grid(row=3, column=2)
txtStateTax = Entry(f1, font=('arial', 16, 'bold'), textvariable=Tax, bd=10, insertwidth=4, bg="white", justify='right')
txtStateTax.grid(row=3, column=3)

lblSubTotal = Label(f1, font=('arial', 16, 'bold'), text="Sub Total", bd=16, anchor="w")
lblSubTotal.grid(row=4, column=2)
txtSubTotal = Entry(f1, font=('arial', 16, 'bold'), textvariable=SubTotal, bd=10, insertwidth=4, bg="white",
                    justify='right')
txtSubTotal.grid(row=4, column=3)

lblTotalCost = Label(f1, font=('arial', 16, 'bold'), text="Total Cost", bd=16, anchor="w")
lblTotalCost.grid(row=5, column=2)
txtTotalCost = Entry(f1, font=('arial', 16, 'bold'), textvariable=Total, bd=10, insertwidth=4, bg="white",
                     justify='right')
txtTotalCost.grid(row=5, column=3)

# ==========================================Buttons==========================================================================================
btnTotal = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Total",
                  bg="sky blue", command=Ref).grid(row=7, column=1)

btnReset = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Reset",
                  bg="sky blue", command=Reset).grid(row=7, column=2)

btnExit = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Exit",
                 bg="sky blue", command=qExit).grid(row=7, column=3)

root.mainloop()


