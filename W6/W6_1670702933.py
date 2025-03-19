from tkinter import *
from tkinter import ttk
# from tkmacos import Button

def createwindow():
    master = Tk()
    master.geometry('800x700+300+100')
    master.option_add("*font", "tahoma 14")
    master.title("Week6 : Sweet Home Cafe' Application by Bongkodphetr Yotkathok")
    master.configure(bg='light pink')
    master.grid_rowconfigure((0,2),weight=1)
    master.grid_rowconfigure(1,weight=5) #ตรงกลาง
    master.grid_columnconfigure(0,weight=1)
    master.grid_columnconfigure(1,weight=3)
    return (master)

def layout(mater) :
    #top
    top.grid_columnconfigure((0,1,2),weight=1)
    top.grid_rowconfigure((0) ,weight=1)
    top.grid(row=0, columnspan=2 ,sticky='news')
    #bottom
    bottom.grid_rowconfigure(0, weight=1)
    bottom.grid_columnconfigure((0,1),weight=1)
    bottom.grid(row=2, columnspan=2 , sticky='news')


def topframe(top) : 
    Button(top,text='Cake Menu', image=icon1,compound='top',command=cakeclick).grid(row=0, column=0, sticky='news')
    Button(top,text='Drink Menu',image=icon2,compound='top',command=drinkclick).grid(row=0, column=1, sticky='news')
    Button(top,text='Checkout',image=icon3,compound='top',command=checkoutclick).grid(row=0, column=2, sticky='news')

def bottomframe(bottom) :
    Button(bottom,text='Reset Submit', image=icon4,compound='left',command=cancelclick).grid(row=0,column=0,sticky='news')
    Button(bottom,text='Exit Program', image=icon5,compound='left',command=exit).grid(row=0,column=1,sticky='news')

def cakeclick() :
    # dleft.grid_forget()
    # dright.grid_forget()
    # checkoutframe.grid_forget()
    dleft.grid_forget()
    dright.grid_forget()
    checkoutframe.grid_forget()
    cleft.grid_columnconfigure(0, weight=1)
    cleft.grid_rowconfigure((0,1,2),weight=1)
    cleft.grid(row=1,column=0,sticky='news')
    cright.grid_columnconfigure((0,1),weight=1)
    cright.grid_rowconfigure((0,1,2),weight=1)
    cright.grid(row=1,column=1,sticky='news')
    cakeimage = [cake1,cake2,cake3]
    for i,cake in enumerate(cakemenu) :
        Label(cleft,bg='#D4F6FF',text=cake, image=cakeimage[i],compound='bottom').grid(row=i)
        Label(cright,bg='#C6E7FF',text=f'(Price :{price1[i]}) Amount : ').grid(row=i, column=0)
        Entry(cright,font=('tahoma',16,'bold'),width=10,justify='center',textvariable=cakespy[i]).grid(row=i, column=1)

def drinkclick() :
    cleft.grid_forget()
    cright.grid_forget()
    checkoutframe.grid_forget()
    dleft.grid_columnconfigure(0,weight=1)
    dleft.grid_rowconfigure((0,1),weight=1)
    dleft.grid(row=1,column=0,sticky='news')
    dright.grid_rowconfigure((0,1),weight=1)
    dright.grid_columnconfigure((0,1),weight=1)
    dright.grid(row=1,column=1,sticky='news')
    drinkimage = [drink1,drink2]
    for i,drink in enumerate(drinkmenu) :
        Label(dleft,bg='#FFECC8', text=drink, image=drinkimage[i],compound='bottom').grid(row=i)
        Label(dright,bg='#FFD09B' , text=f'(Price : {price2[i]}) Amount :').grid(row=i, column=0)
        Entry(dright,font=('tahoma',16,'bold'),width=10,justify='center',textvariable=drinkspy[i]).grid(row=i, column=1)

def checkoutclick() :
    global sumcake,sumdrink
    sumcake,sumdrink = 0,0
    cleft.grid_forget()
    dleft.grid_forget()
    cright.grid_forget()
    dright.grid_forget()
    checkoutframe.grid_columnconfigure(0,weight=1)
    checkoutframe.grid_rowconfigure((0,3), weight=2)
    checkoutframe.grid_rowconfigure((1,2),weight=1)
    checkoutframe.grid(row=1,columnspan=2,sticky='news')
    for i,cake in enumerate(price1) :
        sumcake += cakespy[i].get() * price1[i]
        sumdrink += drinkspy[i].get() * price2[i]
    #calculate total price
    total = sumcake + sumdrink
    Label(checkoutframe,text='~ Summary of Cake/Drink Menu ~',font=('comic sans ms',20,'bold'),fg='blue',bg='#EBC7E6').grid(row=0)
    Label(checkoutframe,text=f'Total cake price = {sumcake:,.2f} ',bg='#FFB38E').grid(row=1,sticky='news')
    Label(checkoutframe,text=f'Total drink price = {sumdrink:,.2f} ',bg='#C6E7FF').grid(row=2,sticky='news')
    Label(checkoutframe,text=f'Tota price of your order = {total:,.2f} Baht',font=('comic sans ms',20,'bold'),fg='blue',bg='#EBC7E6').grid(row=3)

def cancelclick() :
    for i,price in enumerate(price1) : 
        cakespy[i].set(0)
        drinkspy[i].set(0)

#main program
master = createwindow()
drink1 = PhotoImage(file="image/drink1.png")
drink2 = PhotoImage(file="image/drink2.png")
drink3 = PhotoImage(file='image/drink3.png')
cake1 = PhotoImage(file="image/cake1.png")
cake2 = PhotoImage(file="image/cake2.png")
cake3 = PhotoImage(file="image/cake3.png")
#create image list for cake and drink menu
icon1 = PhotoImage(file='image/cake-button.png')
icon2 = PhotoImage(file='image/drink-button.png')
icon3 = PhotoImage(file="image/checkout.png")
icon4 = PhotoImage(file="image/cancel.png")
icon5 = PhotoImage(file="image/exit.png")
cakemenu = [' Strawberry Cake \n'," Cheese   Cake  \n","Newyork Cheese Cake\n"]
drinkmenu = ['| Orange   Mixed |\n',' Lemonade Mixed \n']
drinkmenu1 = ['| Orange   Mixed |\n',' Lemonade Mixed \n',"| Mojito  Miexd  Berry |\n"]
price1 = [145,120,130]
price2 = [120,100,90]
#spy for cake/drink amount
cakespy = [IntVar() for x in price1]
drinkspy = [IntVar() for x in price2]
#create frame as global
top = Frame(master,bg='#FBFBFB')
cleft = Frame(master,bg='#D4F6FF')
dleft = Frame(master,bg='#FFECC8')
cright = Frame(master,bg='#C6E7FF')
dright = Frame(master,bg='#FFD09B')
bottom = Frame(master,bg='#FFDDAE')
checkoutframe = Frame(master,bg='#EBC7E6')
layout(master)
topframe(top)
bottomframe(bottom)
master.mainloop()
