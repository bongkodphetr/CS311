from tkinter import *
 
def createwindow() :
    master = Tk()
    master.wm_geometry('1000x700+300+50')
    master.title("GUI4 : Dream cake cafe by Bongkodphetr Yotkathok")
    master.option_add('*font','Garamond 18')
    master.grid_columnconfigure((0,1),weight=1)
    master.grid_rowconfigure((0,2),weight=1)
    master.grid_rowconfigure(1,weight=5)
    return(master)
 
def framelayout(master) :
    top = Frame(master,bg='#2973B2')
    top.grid(row=0,columnspan=2,sticky='news')
    top.grid_columnconfigure((0),weight=1)
    top.grid_columnconfigure((1),weight=2)
    left = Frame(master,bg='#9ACBD0')
    left.grid_columnconfigure((0,1),weight=1)
    left.grid_rowconfigure((0,1,2,3,4,5),weight=1)
    left.grid(row=1,column=0,sticky='news')
    right = Frame(master,bg='#F2EFE7')
    right.grid(row=1,column=1,sticky='news')
    bottom = Frame(master,bg='#A7B49E')
    bottom.grid(row=2,columnspan=2,sticky='news')
    return(top,left,right,bottom)
 
def widgets(top,left,right,bottom) :
    # heading = Label(top,bg='#2973B2',text='Dream Cafe by Bongkodphetr Yotkathok',fg='white',font=('Jetbrains Mono',22,'bold'))
    # heading.pack(pady=15)
    order1 = Label(left,image=cake1,bg='#9ACBD0')
    order1.grid(row=0,column=0,rowspan=2,sticky=E)
    detail1 = Label(left,bg='#9ACBD0',text='Chocolate cake\nPrice 160 baht')
    detail1.grid(row=0,column=1,sticky=S)
    amount1 = Checkbutton(left,text='Price : 160 B',bg='#9ACBD0',fg='#3674B5',variable=spy1,command=userclick)
    amount1.grid(row=1,column=1,sticky=N)
    order2 = Label(left,image=cake2,bg='#9ACBD0')
    order2.grid(row=2,column=0,rowspan=2,sticky=E)
    detail2 = Label(left,bg='#9ACBD0',text='Strawberry cake\nPrice 140 baht')
    detail2.grid(row=2,column=1,sticky=S)
    amount2 = Checkbutton(left,text="Price : 140 B",bg='#9ACBD0',fg='#3674B5',variable=spy2,command=userclick)
    amount2.grid(row=3,column=1,sticky=N)
    order3 = Label(left,image=cake3,bg='#9ACBD0')
    order3.grid(row=4,column=0,rowspan=2,sticky=E)
    detail3 = Label(left,bg='#9ACBD0',text='Pony Donut\nPrice 75 baht')
    detail3.grid(row=4,column=1,sticky=S)
    amount3 = Checkbutton(left,text="Price : 75 B",bg='#9ACBD0',fg='#3674B5',variable=spy3,command=userclick)
    amount3.grid(row=5,column=1,sticky=N)
    summary = Label(right,bg='#F2EFE7',text="Thank you for your shopping\n Total price is",font=('Jetbrains Mono',22))
    summary.pack(pady=50)
    shownet = Label(right,bg='#F2EFE7',text="Total = 0.00 Baht",font=("Garamond",22),fg='blue')
    shownet.pack(pady=25)
    btn1 = Button(top,text="Exit Program",command=exit)
    btn1.grid(row=0, column=1, sticky='S')
    return(shownet)
 
def userclick() : #call back function
    net = spy1.get()*160 + spy2.get()*140 + spy3.get()*75
    shownet['text'] = f"Total = {net:0.2f} Baht"
 
#main
master = createwindow()
cake1 = PhotoImage(file="image/cake1.png")
cake2 = PhotoImage(file='image/cake2.png')
cake3 = PhotoImage(file='image/cake3.png')
spy1,spy2,spy3 = IntVar(),IntVar(),IntVar()
net =  0
top,left,right,bottom = framelayout(master)
shownet = widgets(top,left,right,bottom)
master.mainloop()
 