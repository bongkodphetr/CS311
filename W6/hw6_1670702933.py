from tkinter import *


def createwindow() :
    master = Tk()
    master.geometry("900x700+300+100")
    master.option_add("*font", "tahoma 14")
    master.title("Homework of Week 6 : Sweet Home Cafe' Application by Bongkodphetr Yotkathok")
    master.configure(bg="light pink")
    master.rowconfigure(0, weight=1)
    master.columnconfigure(0, weight=1)
    master.columnconfigure(1, weight=2)    
    return master

def layout(master) :
    leftmenu = Frame(master, bg='#FFFFFF')
    leftmenu.columnconfigure(0, weight=1)
    leftmenu.rowconfigure((0, 1, 2), weight=1)
    leftmenu.grid(rowspan=3, column=0, sticky='news')
    return leftmenu

def leftframe(leftmenu) :
    Button(leftmenu,text='Product Menu', image=product_icon, compound=BOTTOM, command=midframe).grid(row=0, column=0, sticky='news')
    Button(leftmenu,text='Checkout', image=checkout_icon, compound=BOTTOM, command=checkoutclick).grid(row=1, column=0, sticky='news')
    Button(leftmenu,text='Close Program', image=exit_icon, compound=BOTTOM, command=exit).grid(row=2, column=0, sticky='news')
    
def midframe() :
    checkoutframe.grid_forget()
    mid1.columnconfigure((0, 1), weight=1)
    mid1.rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
    mid1.grid(row=0, column=1, sticky='news')
    
    cakeimg = [cake1, cake2, cake3]
    drinkimg = [drink1, drink2, drink3]
    
    for i, cake in enumerate(cakemenu):
        Label(mid1, bg="#D4F6FF", text=cake, image=cakeimg[i], compound=RIGHT).grid(row=i*2, column=0, pady=10, sticky='news')
        Spinbox(mid1, from_=0, to=100, justify=CENTER, width=15, textvariable=cakespy[i]).grid(row=i*2+1, column=0, pady=5)
    
    for i, drink in enumerate(drinkmenu):
        Label(mid1, bg="#D4F6FF", text=drink, image=drinkimg[i], compound=RIGHT).grid(row=i*2, column=1, pady=10, sticky='news')
        Spinbox(mid1, from_=0, to=100, justify=CENTER, width=15, textvariable=drinkspy[i]).grid(row=i*2+1, column=1, pady=5)
    
    
def checkoutclick() :
    global sumcake,sumdrink
    sumcake,sumdrink = 0,0
    mid1.grid_forget()
    checkoutframe.columnconfigure(0, weight=1)
    checkoutframe.rowconfigure((0, 1, 2, 3), weight=1)
    checkoutframe.grid(row=0, column=1, sticky='news')
    for i,cake in enumerate(price1) :
        sumcake += cakespy[i].get() * price1[i]
        sumdrink += drinkspy[i].get() * price2[i]
    total = sumcake + sumdrink
    Label(checkoutframe,text='~ Summary of Cake/Drink Menu ~', font=('comic sans ms',20,'bold'), fg='blue', bg='#EBC7E6').grid(row=0)
    Label(checkoutframe,text=f'Total cake price = {sumcake:,.2f}', bg='#FFB38E').grid(row=1,sticky='news')
    Label(checkoutframe,text=f'Total drink price = {sumdrink:,.2f}', bg='#C6E7FF').grid(row=2,sticky='news')
    Label(checkoutframe,text=f'Tota price of your order = {total:,.2f} Baht', font=('comic sans ms',20,'bold'), fg='blue', bg='#EBC7E6').grid(row=3)

master = createwindow()

cake1 = PhotoImage(file="image/cake1.png")
cake2 = PhotoImage(file="image/cake2.png")
cake3 = PhotoImage(file="image/cake3.png")

drink1 = PhotoImage(file="image/drink1.png")
drink2 = PhotoImage(file="image/drink2.png")
drink3 = PhotoImage(file="image/drink3.png")

product_icon = PhotoImage(file="image/cake-button.png")
checkout_icon = PhotoImage(file="image/drink-button.png")
exit_icon = PhotoImage(file="image/exit.png")
cakemenu = ["Strawberry Cake\nPrice : 145", "Cheese Cake\nPrice : 120", "Newyork Cheese Cake\nPrice : 130"]
drinkmenu = ["Orange Mixed\nPrice : 120", "Lemonade Mixed\nPrice : 100", "Mojito Mixed Berry\nPrice : 90"]
price1 = [145, 120, 130]
price2 = [120, 100, 90]
cakespy = [IntVar() for x in price1]
drinkspy = [IntVar() for x in price2]
mid1 = Frame(master, bg='#D4F6FF')
checkoutframe = Frame(master, bg='#EBC7E6')
leftmenu = layout(master)
leftframe(leftmenu)
master.mainloop()