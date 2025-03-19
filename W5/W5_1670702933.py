from tkinter import *

def mainwindow() :
    root = Tk()
    root.title("Class Activity of Week5 : Dream cake cafe by Bongkodphetr Yotkathok")
    root.geometry("1200x750")
    root.rowconfigure((0,2), weight=1)
    root.grid_rowconfigure(1,weight=4)
    root.grid_columnconfigure((0,1), weight=1)
    root.option_add('*font', 'Garamond,16')
    return(root)

def layout(master) :
    top = Frame(master, bg='#543A14')
    top.rowconfigure(0, weight=1)
    top.columnconfigure(0, weight=1)
    top.grid(row=0, columnspan=2, sticky='news')

    left = Frame(master, bg='#FFF0DC')
    left.grid_rowconfigure((0,1,2,3,4), weight=1)
    left.grid_columnconfigure((0,1,2), weight=1)
    left.grid(row=1, column=0, sticky='news')

    right = Frame(master, bg='#997C70')
    right.grid_rowconfigure((0,1,2,3,4), weight=1)
    right.grid_columnconfigure((0,1,2), weight=1)
    right.grid(row=1, column=1, sticky='news')

    bottom = Frame(master, bg='#543A14')
    bottom.columnconfigure((0,1),weight=1)
    bottom.rowconfigure(0,weight=1)
    bottom.grid(row=2, columnspan=2, sticky='news')

    return(top,bottom,left,right)

def topside(top) :
    title = Label(top,text="Dream House Cafe by Bongkodphetr Yotkathok",font=("Garamond",22),bg="#543A14",fg='white')
    title.grid(row=0)

def leftside(left) :
    cakemenu = ["Stawberry Cake\n125 B.","Cheese Cake\n110 B.","Babybloom Cake\n140 B.","Chocolate Cake\n100 B."]
    cakespy = [IntVar() for i in cakemenu]
    for i ,cake in enumerate(cakemenu):
        Label(left, bg='#FFF0DC', image=cakelist[i]).grid(row=i, column=0)
        Label(left, bg='#FFF0DC', text=cake).grid(row=i, column=1)
        Spinbox(left, from_=0, to=200,width=10,justify='center',textvariable=cakespy[i],command=userclick).grid(row=i,column=2)

    return(cakespy)
def rightside(right) :
    drinkmenu = ["Hot Latte\n80 B.","Hot Cappuccino\n70 B.","Hot Caramel Latte\n100 B."," Hot Chocolate\n90 B."]
    drinkspy = [IntVar() for i in drinkmenu ]
    for i,drink in enumerate(drinkmenu):
        Label(right,bg='#997C70', image=drinklist[i]).grid(row=i,column=0)
        Label(right,bg='#997C70',text=drink,fg="#FFF").grid(row=i, column=1)
        Spinbox(right, from_=0, to=200, width=10,justify='center', textvariable=drinkspy[i],command=userclick).grid(row=i, column=2)
    return(drinkspy)
def bottomside(bottom) :
    showcake = Label(bottom, bg='#543A14')
    showcake.grid(row=0,column=0)
    showdrink = Label(bottom, bg='#543A14')
    showdrink.grid(row=0,column=1)
    return(showcake,showdrink)

def userclick() :
    totalcake = 0
    totaldrink = 0
    cakeprice = [125,110,140,100]
    drinkprice = [80,70,100,90]
    for i , item in enumerate(cakeprice) :
        totalcake += cakespy[i].get() * cakeprice[i]
        totaldrink += drinkspy[i].get() * drinkprice[i]
    showcake['text'] = f'Total price = {totalcake: 0.2f} Baht'
    showcake['bg'] = "#FFF0DC"
    showdrink['text'] = f"total price = {totaldrink:0.2f} Baht"
    showdrink['bg'] = "#FFF0DC"
#main program
master = mainwindow()
top,bottom,left,right = layout(master)
cake1 = PhotoImage(file="image/cake1.png")
cake2 = PhotoImage(file="image/cake2.png")
cake3 = PhotoImage(file="image/cake3.png")
cake4 = PhotoImage(file="image/cake4.png")
drink1 = PhotoImage(file="image/coffee1.png")
drink2 = PhotoImage(file="image/coffee2.png")
drink3 = PhotoImage(file="image/coffee3.png")
drink4 = PhotoImage(file="image/coffee4.png")
cakelist = [cake1,cake2,cake3,cake4]
drinklist = [drink1,drink2,drink3,drink4]
topside(top)
cakespy = leftside(left)
drinkspy = rightside(right)
showcake,showdrink = bottomside(bottom)
master.mainloop()