from tkinter import *
from tkinter import messagebox
 
def createwindow() :
    master = Tk()
    master.wm_geometry('1000x700+300+50')
    master.title("Figure shop by Bongkodphetr Yotkathok")
    master.option_add('*font','Garamond 18')
    master.grid_columnconfigure((0),weight=1)
    master.grid_columnconfigure((1),weight=2)
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

    order1 = Label(left,image=fig1,bg='#9ACBD0')
    order1.grid(row=0,column=0,rowspan=2,sticky=E)
    amount1 = Checkbutton(right,text='Skullpanda price = 380 bahts',bg='#F2EFE7',fg='#3674B5',variable=spy1,command=userclick)
    amount1.pack(pady=60)

    order2 = Label(left,image=fig2,bg='#9ACBD0')
    order2.grid(row=2,column=0,rowspan=2,sticky=E)

    amount2 = Checkbutton(right,text="Dimoo price = 450 B",bg='#F2EFE7',fg='#3674B5',variable=spy2,command=userclick)
    amount2.pack(pady=80)
    order3 = Label(left,image=fig3,bg='#9ACBD0')
    order3.grid(row=4,column=0,rowspan=2,sticky=E)

    amount3 = Checkbutton(right,text="Crybaby price = 350 B",bg='#F2EFE7',fg='#3674B5',variable=spy3,command=userclick)
    amount3.pack(pady=90)


    btn1 = Button(top, text="CLICK ME", image=icon1, compound=LEFT, command=btn1click) 
    btn1.grid(row=0, ipadx=15)
    btn2 = Button(top,text="EXIT PROGRAM",image=icon2, compound=LEFT , command=exit)
    btn2.grid(row=0,column=1, ipady=5,sticky='S')
    shownet = Label(bottom,bg='#A7B49E' ,text="Total Price = 0.00 Bahts",font=("Jetbrains Mono Bold",22),fg='blue')
    shownet.pack(pady=25 ,anchor='center')   
    return(shownet)

def btn1click():
    messagebox.showinfo("Hello","Wellcome to Art toy shop by\nPopmart Officail Store:\n1.Skullpanda\n2.Dimoo\n3.Crybaby")
 
def userclick():
    net = spy1.get()*380 + spy2.get()*450 + spy3.get()*350
    shownet['text'] = f"Total = {net:0.2f} Baht"
 
#main
master = createwindow()
fig1 = PhotoImage(file="image/fig1.png").subsample(3,3)
fig2 = PhotoImage(file='image/fig2.png').subsample(3,3)
fig3 = PhotoImage(file='image/fig3.png').subsample(3,3)
icon1 = PhotoImage(file='image/icon1.png')
icon2 = PhotoImage(file='image/icon2.png')
spy1,spy2,spy3 = IntVar(),IntVar(),IntVar()
net =  0
top,left,right,bottom = framelayout(master)
shownet = widgets(top,left,right,bottom)
master.mainloop()
 