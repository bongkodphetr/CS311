from tkinter import *
from tkinter import ttk


def createwindow():
    master = Tk()
    master.geometry('800x600+300+100')
    master.option_add("*font", "tahoma 12")
    master.title("Product Selection Application by Bongkodphetr Yotkathok 1670702933")
    master.configure(bg='#d2b48c')
    master.grid_rowconfigure((0, 2), weight=1)
    master.grid_rowconfigure(1, weight=5)
    master.grid_columnconfigure(0, weight=1)
    master.grid_columnconfigure(1, weight=3)
    return master

def layout(master):
    top.grid_columnconfigure((0, 1, 2), weight=1)
    top.grid_rowconfigure(0, weight=1)
    top.grid(row=0, columnspan=2, sticky='news')
    
    bottom.grid_rowconfigure(0, weight=1)
    bottom.grid_columnconfigure(0, weight=1)
    bottom.grid(row=2, columnspan=2, sticky='news')

def topframe(top):
    Button(top,text='OS', image=icon1, compound='top', bg='#d2b48c', command=osframe).grid(row=0, column=0, sticky='news')
    Button(top, text='Monitor',image=icon3, compound='top', bg='#d2b48c', command=monitorframe).grid(row=0,column=1, sticky='news')
    Button(top, text='Mouse', image=icon5, compound='top', bg='#d2b48c', command=mouseframe).grid(row=0, column=2, sticky='news')

def bottomframe(bottom):
    Button(bottom, text='CHECK PRODUCTS', command=checkproducts).grid(row=0, column=0,sticky='news')


def osframe():

    monitorleft.grid_forget()
    monitorright.grid_forget()
    mouseleft.grid_forget()
    mouseright.grid_forget()
    checkoutframe.grid_forget()
    
    osleft.grid_columnconfigure(0, weight=1)
    osleft.grid_rowconfigure((0,1,2), weight=1)
    osleft.grid(row=1, column=0, sticky='news')
    
    osright.grid_columnconfigure((0,1), weight=1)
    osright.grid_rowconfigure((0,1,2,3), weight=1)
    osright.grid(row=1, column=1, sticky='news')
    Label(osleft, bg='#8b4513', image=maclogo, compound='bottom').grid(row=0)
    
    Checkbutton(osright, bg='#d2b48c', variable=oscheck[0]).grid(row=0, column=0, sticky='w')
    Label(osright, bg='#d2b48c', text='Mac OS X V.1, Price = 10,900 baht.').grid(row=0, column=0, sticky='w', padx=20)
    Entry(osright, font=('tahoma',12,'bold'), width=5, justify='center', textvariable=osspy[0]).grid(row=0, column=1)
    
    Checkbutton(osright, bg='#d2b48c', variable=oscheck[1]).grid(row=1, column=0, sticky='w')
    Label(osright, bg='#d2b48c', text='Mac OS X V.2, Price = 12,900 baht.').grid(row=1, column=0, sticky='w', padx=20)
    Entry(osright, font=('tahoma', 12,'bold'), width=5, justify='center', textvariable=osspy[1]).grid(row=1, column=1)
    
    Label(osleft, bg='#8b4513', image=winlogo, compound='bottom').grid(row=1)
    
    Checkbutton(osright, bg='#f5f5dc', variable=oscheck[2]).grid(row=2, column=0, sticky='w')
    Label(osright, bg='#f5f5dc', text='Windows OS 10, Price = 7,900 baht.').grid(row=2, column=0, sticky='w', padx=20)
    Entry(osright, font=('tahoma', 12,'bold'), width=5, justify='center', textvariable=osspy[2]).grid(row=2, column=1)
    
    Checkbutton(osright, bg='#f5f5dc', variable=oscheck[3]).grid(row=3, column=0, sticky='w')
    Label(osright, bg='#f5f5dc', text='Windows OS 11, Price = 9,900 baht.').grid(row=3, column=0, sticky='w', padx=20)
    Entry(osright, font=('tahoma',12,'bold'), width=5, justify='center', textvariable=osspy[3]).grid(row=3, column=1)

def monitorframe():

    osleft.grid_forget()
    osright.grid_forget()
    mouseleft.grid_forget()
    mouseright.grid_forget()
    checkoutframe.grid_forget()
    
    monitorleft.grid_columnconfigure(0, weight=1)
    monitorleft.grid_rowconfigure((0,1,2), weight=1)
    monitorleft.grid(row=1, column=0, sticky='news')
    
    monitorright.grid_columnconfigure((0,1), weight=1)
    monitorright.grid_rowconfigure((0,1,2,3), weight=1)
    monitorright.grid(row=1, column=1, sticky='news')
    

    Label(monitorleft, bg='#8b4513',image=maclogo, compound='bottom').grid(row=0)
    

    Checkbutton(monitorright, bg='#d2b48c', variable=monitorcheck[0]).grid(row=0, column=0, sticky='w')
    Label(monitorright, bg='#d2b48c', text='Max Monitor 13", Price = 12,900 baht.').grid(row=0, column=0, sticky='w', padx=20)
    Entry(monitorright, font=('tahoma',12, 'bold'), width=5, justify='center', textvariable=monitorspy[0]).grid(row=0, column=1)
    

    Checkbutton(monitorright, bg='#d2b48c', variable=monitorcheck[1]).grid(row=1, column=0, sticky='w')
    Label(monitorright, bg='#d2b48c', text='Max Monitor 15", Price = 15,900 baht.').grid(row=1, column=0, sticky='w', padx=20)
    Entry(monitorright, font=('tahoma',12, 'bold'), width=5, justify='center', textvariable=monitorspy[1]).grid(row=1, column=1)
    
   
    Label(monitorleft, bg='#8b4513', image=winlogo, compound='bottom').grid(row=1)

    Checkbutton(monitorright, bg='#f5f5dc', variable=monitorcheck[2]).grid(row=2, column=0, sticky='w')
    Label(monitorright, bg='#f5f5dc', text='Win Monitor 13", Price = 12,500 baht.').grid(row=2, column=0, sticky='w', padx=20)
    Entry(monitorright, font=('tahoma', 12, 'bold'), width=5, justify='center', textvariable=monitorspy[2]).grid(row=2, column=1)

    Checkbutton(monitorright, bg='#f5f5dc', variable=monitorcheck[3]).grid(row=3, column=0, sticky='w')
    Label(monitorright, bg='#f5f5dc', text='Win Monitor 15", Price = 15,500 baht.').grid(row=3, column=0, sticky='w', padx=20)
    Entry(monitorright, font=('tahoma', 12, 'bold'), width=5, justify='center', textvariable=monitorspy[3]).grid(row=3, column=1)

def mouseframe():

    osleft.grid_forget()
    osright.grid_forget()
    monitorleft.grid_forget()
    monitorright.grid_forget()
    checkoutframe.grid_forget()
    
    mouseleft.grid_columnconfigure(0, weight=1)
    mouseleft.grid_rowconfigure((0, 1, 2), weight=1)
    mouseleft.grid(row=1, column=0, sticky='news')
  
    mouseright.grid_columnconfigure((0, 1), weight=1)
    mouseright.grid_rowconfigure((0, 1, 2, 3), weight=1)
    mouseright.grid(row=1, column=1, sticky='news')
    
    Label(mouseleft, bg='#8b4513', image=maclogo, compound='bottom').grid(row=0)
    
    Checkbutton(mouseright, bg='#d2b48c', variable=mousecheck[0]).grid(row=0, column=0, sticky='w')
    Label(mouseright, bg='#d2b48c', text='Max Magic Mouse1, Price = 3,000 baht.').grid(row=0, column=0, sticky='w', padx=20)
    Entry(mouseright, font=('tahoma', 12,'bold'), width=5, justify='center', textvariable=mousespy[0]).grid(row=0, column=1)
    Checkbutton(mouseright, bg='#d2b48c', variable=mousecheck[1]).grid(row=1, column=0, sticky='w')
    Label(mouseright, bg='#d2b48c', text='Max Magic Mouse2, Price = 4,000 baht.').grid(row=1, column=0, sticky='w', padx=20)
    Entry(mouseright, font=('tahoma', 12, 'bold'), width=5, justify='center', textvariable=mousespy[1]).grid(row=1, column=1)
    
    Label(mouseleft, bg='#8b4513', image=winlogo, compound='bottom').grid(row=1)

    Checkbutton(mouseright, bg='#f5f5dc', variable=mousecheck[2]).grid(row=2, column=0, sticky='w')
    Label(mouseright, bg='#f5f5dc', text='Window Dream Mouse1, Price = 2,500 baht.').grid(row=2, column=0, sticky='w', padx=20)
    Entry(mouseright, font=('tahoma', 12, 'bold'), width=5, justify='center', textvariable=mousespy[2]).grid(row=2, column=1)
    Checkbutton(mouseright, bg='#f5f5dc', variable=mousecheck[3]).grid(row=3, column=0, sticky='w')
    Label(mouseright, bg='#f5f5dc', text='Window Dream Mouse2, Price = 3,000 baht.').grid(row=3, column=0, sticky='w', padx=20)
    Entry(mouseright, font=('tahoma', 12,'bold'), width=5, justify='center', textvariable=mousespy[3]).grid(row=3, column=1)

def checkproducts():
    global summac, sumwin
    summac, sumwin = 0, 0
    osleft.grid_forget()
    osright.grid_forget()
    monitorleft.grid_forget()
    monitorright.grid_forget()
    mouseleft.grid_forget()
    mouseright.grid_forget()
    
    checkoutframe.grid_columnconfigure(0, weight=1)
    checkoutframe.grid_rowconfigure((0, 1,2, 3), weight=1)
    checkoutframe.grid(row=1, columnspan=2, sticky='news')

    for i, price in enumerate(osprices[:2]):
        if oscheck[i].get() == 1:
            summac += osspy[i].get() * osprices[i]
    for i, price in enumerate(monitorprices[:2]):
        if monitorcheck[i].get() == 1:
            summac += monitorspy[i].get() * monitorprices[i]
    for i, price in enumerate(mouseprices[:2]):
        if mousecheck[i].get() == 1:
            summac += mousespy[i].get() * mouseprices[i]
    for i, price in enumerate(osprices[2:]):
        if oscheck[i+2].get() == 1:
            sumwin += osspy[i + 2].get() * osprices[i + 2]
    for i, price in enumerate(monitorprices[2:]):
        if monitorcheck[i + 2].get() == 1:
            sumwin += monitorspy[i + 2].get() * monitorprices[i + 2]
    for i, price in enumerate(mouseprices[2:]):
        if mousecheck[i + 2].get() == 1:
            sumwin += mousespy[i + 2].get() * mouseprices[i + 2]
    
    total = summac + sumwin
    
    Label(checkoutframe, text=f'Total Mac Product = {summac:,.2f}', bg='#ffb6c1').grid(row=1, sticky='news')
    Label(checkoutframe, text=f'Total Windows Product = {sumwin:,.2f}', bg='#ffb6c1').grid(row=2, sticky='news')
    Label(checkoutframe, text=f'All Total Product = {total:,.2f}', font=('tahoma', 16, 'bold'), fg='blue', bg='#ffb6c1').grid(row=3)
master = createwindow()
icon1 = PhotoImage(file="image/os1.png")
icon2 = PhotoImage(file="image/os2.png")
icon3 = PhotoImage(file="image/monitor1.png") 
icon4 = PhotoImage(file="image/monitor2.png") 
icon5 = PhotoImage(file="image/mouse1.png") 
maclogo = PhotoImage(file="image/apple.png") 
winlogo = PhotoImage(file="image/windows.png") 

osprices = [10900, 12900, 7900, 9900]
monitorprices = [12900, 15900, 12500, 15500]
mouseprices = [3000, 4000, 2500, 3000]

osspy = [IntVar() for _ in osprices]
monitorspy = [IntVar() for _ in monitorprices]
mousespy = [IntVar() for _ in mouseprices]
oscheck = [IntVar() for _ in osprices]
monitorcheck = [IntVar() for _ in monitorprices]
mousecheck = [IntVar() for _ in mouseprices]
top = Frame(master, bg='#d2b48c')
osleft = Frame(master, bg='#8b4513') 
osright = Frame(master, bg='#d2b48c')
monitorleft = Frame(master, bg='#8b4513')
monitorright = Frame(master, bg='#d2b48c')
mouseleft = Frame(master, bg='#8b4513')
mouseright = Frame(master, bg='#d2b48c')
bottom = Frame(master, bg='#d2b48c')
checkoutframe = Frame(master, bg='#ffb6c1') 

layout(master)
topframe(top)
bottomframe(bottom)
osframe()
master.mainloop()