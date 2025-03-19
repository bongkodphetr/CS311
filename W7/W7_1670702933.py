from tkinter import *
from tkinter import messagebox

def create_window():
    master = Tk()
    master.title("Week7 - Dream Cafe' Application by Bongkodphetr Yotkathok")
    master.geometry('800x700+300+100')
    master.option_add("*font", "tahoma 16")
    # master.rowconfigure(0, weight=1)
    # master.columnconfigure(0, weight=1)
    master.configure(bg='#EDDFE0')
    master.grid_rowconfigure((0,2),weight=1)
    master.grid_rowconfigure(1,weight=5)
    master.grid_columnconfigure(0,weight=1)
    return (master)

def layout(master) :
    top.grid(row=0,sticky='news')
    top.grid_rowconfigure((0,1), weight=1)
    top.grid_columnconfigure((0,2), weight=1)
    top.grid_columnconfigure(1,weight=3)
    center.grid(row=1, sticky='news')
    center.grid_rowconfigure((0,1,2),weight=1)
    center.grid_columnconfigure((0,1,2,3),weight=1)
    bottom.grid(row=2, sticky='news')
    bottom.rowconfigure(0, weight=1)
    bottom.columnconfigure((0,1), weight=1)


def topframe(top) :
    Label(top,bg='#AB886D', image=img1).grid(row=0, column=0,rowspan=2)
    Label(top,bg='#AB886D', image=img2).grid(row=0, column=2,rowspan=2)
    Label(top,bg='#AB886D', text="Dream Cafe' Shop",font=('tahoma',26,'bold')).grid(row=0,column=1,sticky=S)
    Label(top,bg='#AB886D',text="Customer Like our Family").grid(row=1,column=1,sticky=N)

def bottomframe(bottom) :
    Button(bottom,text='Reset All', width=10,command=resetclick).grid(row=0,column=0, sticky=E, padx=5)
    Button(bottom,text='Check Out', width=10,command=checkout).grid(row=0,column=1, sticky=W, padx=5)

def centerframe(center) :
    Button(center,text='Cake menu',image=img1,compound='bottom',command=cakeclick).grid(row=0, column=0,sticky='news')
    Button(center,text='Drink menu',image=img1,compound='bottom',command=drinkclick).grid(row=1, column=3,sticky='news')
    Button(center,text='Coffee menu',image=coffee1,compound='bottom',command=coffeeclick).grid(row=2, column=0,sticky='news')

def cakeclick() :
    cakeframe.grid(row=0,column=1, columnspan=3,sticky='news')
    cakeframe.rowconfigure(0,weight=1)
    cakeframe.columnconfigure((0,1,2),weight=1)
    Radiobutton(cakeframe,bg='#FFE3E3',text='Cake menu1\n(Price : 120 B)', image=cake1,compound='top',variable=cakespy, value=0).grid(row=0,column=0)
    Radiobutton(cakeframe,bg='#FFE3E3',text='Cake menu2\n(Price : 140 B)', image=cake2,compound='top',variable=cakespy, value=1).grid(row=0,column=1)
    Spinbox(cakeframe,from_=0, to=100, width=10,bg='black',fg='white',justify='center',textvariable=camt).grid(row=0, column=2)
 

def drinkclick() :

    drinkframe.grid(row=1,column=0, columnspan=3 ,sticky='news')
    drinkframe.columnconfigure((0,1,2),weight=1)
    drinkframe.rowconfigure(0,weight=1)
    Spinbox(drinkframe,from_=0,to=100,width=10,bg='black',fg='white',justify='center',textvariable=damt).grid(row=0,column=0)
    Radiobutton(drinkframe,bg='#FFF7D1',text='Drink menu\n(Price : 75 B)', image=drink1,compound='top',variable=drinkspy, value=0).grid(row=0,column=1)
    Radiobutton(drinkframe,bg='#FFF7D1',text='Drink menu\n(Price : 80 B)', image=drink2,compound='top',variable=drinkspy, value=1).grid(row=0,column=2)

def coffeeclick() :
    coffeeframe.grid(row=2, column=1,columnspan=3, sticky='news')
    coffeeframe.rowconfigure(0,weight=1) 
    coffeeframe.columnconfigure((0,1,2),weight=1)
    Radiobutton(coffeeframe, bg='#ECDFCC',text='Coffee menu1\n(Price : 50 B)', image=coffee2,compound='top',variable=coffeespy, value=0).grid(row=0,column=0)
    Radiobutton(coffeeframe, bg='#ECDFCC',text='Coffee menu2\n(Price : 60 B)', image=coffee3,compound='top',variable=coffeespy, value=1).grid(row=0,column=1)
    Spinbox(coffeeframe, from_=0, to=100, width=10,justify='center',bg='black',fg='white',textvariable=cofamt).grid(row=0,column=2)

def checkout() :

    bottom.grid_forget()
    center2.grid(row=1,rowspan=2,sticky='news')
    center2.rowconfigure((0,1,2,3,4,5),weight=1)
    center2.columnconfigure(0,weight=1)
    cprice = camt.get() * price1[cakespy.get()]
    dprice = damt.get() * price2[drinkspy.get()]
    cpirce = cofamt.get() * price3[coffeespy.get()]
    total = cprice + dprice + cpirce

    Label(center2,bg='#EDDFE0',text='Thank you for your order').grid(row=0)
    Label(center2,bg='#EDDFE0',text=f"Total Cake price : {cpirce:,.2f} baht").grid(row=1)
    Label(center2,bg='#EDDFE0',text=f"Total Drink price :{dprice:,.2f} baht").grid(row=2)
    Label(center2,bg='#EDDFE0',text=f"Total Coffee price : {cprice:,.2f} baht").grid(row=3)
    Label(center2,bg='#EDDFE0',text=f"Total Price : {total:,.2f} baht",fg='blue').grid(row=4,sticky='news')
    Button(center2,text='Back to menu',width=15,command=backtomenu).grid(row=5)

def resetclick() :
    cakeframe.grid_forget()
    drinkframe.grid_forget()
    coffeeframe.grid_forget()

    
def backtomenu() :
    center2.grid_forget()
    center.grid(row=1,sticky='news')
    bottom.grid(row=2,sticky='news')

#main
master = create_window()
top = Frame(master,bg='#AB886D')
center = Frame(master,bg='#D6C0B3')
center2 = Frame(master,bg='#EDDFE0')
bottom = Frame(master,bg='#E4E0E1')
cakeframe = Frame(center,bg='#FFE3E3')
drinkframe = Frame(center,bg='#FFF7D1')
coffeeframe = Frame(center,bg='#ECDFCC')
layout(master)
#create image variable
img1 = PhotoImage(file='image/cake-button.png')
img2 = PhotoImage(file='image/drink-button.png')
cake1 = PhotoImage(file='image/cake1.png')
cake2 = PhotoImage(file='image/cake2.png')
drink1 = PhotoImage(file='image/drink1.png')
drink2 = PhotoImage(file='image/drink2.png')
coffee1 = PhotoImage(file='image/coffee1.png')
coffee2 = PhotoImage(file="image/coffee3.png")
coffee3 = PhotoImage(file='image/coffee4.png')
#crate spy variable
cakespy = IntVar()
drinkspy = IntVar()
coffeespy = IntVar()
camt,damt,cofamt = IntVar(),IntVar(),IntVar()
bottomframe(bottom)
topframe(top)
centerframe(center)
price1 = [120,140]
price2 = [75,80]
price3 = [50,60]
master.mainloop()