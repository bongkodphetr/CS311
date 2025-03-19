from tkinter import *
 
def mainwindow() :
    master = Tk()
    master.title("Homework of week 5 : Home Fashion By Bongkodphetr Yotkathok")
    master.geometry('1200x750')
    master.rowconfigure((0, 2), weight=1)
    master.rowconfigure(1, weight=4)
    master.columnconfigure((0, 1), weight=1)
    master.option_add('*font', 'Garamond, 16')
    return master
 
 
def layout(master):
    top = Frame(master, bg='#1B4D3E')
    top.rowconfigure(0, weight=1)
    top.columnconfigure(0, weight=1)
    top.grid(row=0, columnspan=2, sticky='news')
    
    left = Frame(master, bg='#E07A5F')
    left.columnconfigure((0, 1), weight=1)
    left.rowconfigure((0, 1, 2, 3), weight=1)
    left.grid(row=1, column=0, sticky='news')
    
    right = Frame(master, bg="#F1E3D3")
    right.columnconfigure((0, 1), weight=1)
    right.rowconfigure((0, 1, 2, 3), weight=1)
    right.grid(row=1, column=1, sticky='news')
    
    bottom = Frame(master, bg="#1B4D3E")
    bottom.columnconfigure((0, 1), weight=1)
    bottom.rowconfigure(0, weight=1)
    bottom.grid(row=2, columnspan=2, sticky='news')
    return top, left, right, bottom
 
 
def topside(top) :
    title = Label(top, text="Dream Fashion By Bongkodphetr Yotkathok", font=("Garamond", 27, "bold"), bg="#1B4D3E", fg="#FFFFFF")
    title.grid(row=0)
    
def leftside(left) :
    shirts = ["Pink T-Shirt\n225 B.", "Blue T-Shirt\n210 B.", "Lemon T-Shirt\n215 B.", "Orange Shirt\n1000 B."]
    shirtspy = [IntVar() for _ in shirts]
    for i, shirt in enumerate(shirts) :
        Label(left, bg="#E07A5F", image=shirtlist[i]).grid(row=i, column=0)
        Checkbutton(left, bg="#E07A5F", fg="black", text=shirt, variable=shirtspy[i], command=userclick, width=20, anchor=W).grid(row=i, column=1, ipadx=20)
    return shirtspy
 
def rightside(right) :
    shoes = ["VAN Black Color\n2,800 B.", "VAN Blue Color\n2,750 B.", "VAN Red Color\n3,000 B.", "VAN Green Color\n2,900 B."]
    shoespy = [IntVar() for _ in shoes]
    for i, shoe in enumerate(shoes) :
        Label(right, bg="#F1E3D3", image=shoelist[i]).grid(row=i, column=0)
        Checkbutton(right, bg="#F1E3D3", fg="black", text=shoe, variable=shoespy[i], command=userclick, width=20, anchor=W).grid(row=i, column=1)
    return shoespy
 
def bottomside(bottom) :
    global showshirt, showshoe
    showshirt = Label(bottom, bg="#FFDFEF", fg="black")
    showshirt.grid(row=0, column=0)
    showshoe = Label(bottom, bg="#FFDFEF", fg="black")
    showshoe.grid(row=0, column=1)
    return showshirt, showshoe
 
def userclick() :
    total_shirt = 0
    total_shoe = 0    
    shirtprice = [225, 210, 215, 1000]
    shoeprice = [2800, 2750, 3000, 2900]
    for i, item in enumerate(shirtprice):
        total_shirt += shirtspy[i].get() * shirtprice[i]
        total_shoe += shoespy[i].get() * shoeprice[i]
 
    showshirt['text'] = f'Shirt Total price = {total_shirt:0.2f} Baht'
    showshoe['text'] = f'Shoe Total price = {total_shoe:0.2f} Baht'
    
#main
master = mainwindow()
top, left, right, bottom = layout(master)
shirt1 = PhotoImage(file="image/shirt1.png")
shirt2 = PhotoImage(file="image/shirt2.png")
shirt3 = PhotoImage(file="image/shirt3.png")
shirt4 = PhotoImage(file="image/shirt4.png")
shoe1 = PhotoImage(file="image/shoe1.png")
shoe2 = PhotoImage(file="image/shoe2.png")
shoe3 = PhotoImage(file="image/shoe3.png")
shoe4 = PhotoImage(file="image/shoe4.png")
shirtlist = [shirt1, shirt2, shirt3, shirt4]
shoelist = [shoe1, shoe2, shoe3, shoe4]
topside(top)
shirtspy = leftside(left)
shoespy = rightside(right)
showshirt, showshoe = bottomside(bottom)
master.mainloop()