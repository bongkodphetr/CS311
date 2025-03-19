from tkinter import *
from tkinter import messagebox

def createWindow():
    master = Tk()
    master.wm_geometry("1000x800+300+50")
    master.title("GUI4 : Dream cake cafe by Bongkodphetr Yotkathok")
    master.option_add('*font','Daramond 20')
    master.grid_columnconfigure((0,1),weight=1)
    master.grid_rowconfigure((0,2),weight=1) #แถวบนล่าง
    master.grid_rowconfigure(1,weight=5) #แถวกลาง
    return(master)

def frameLayout(master):

    top = Frame(master,bg='#B82132')
    top.grid(row=0,columnspan=2,sticky='news')

    left = Frame(master,bg='#F2B28C')
    left.grid(row=1,column=0,sticky='news')
    #Config row 1 Left
    left.grid_columnconfigure((0,1),weight=1)
    left.grid_rowconfigure((0,1,2,3,4,5),weight=1)
    right = Frame(master,bg='#F6DED8')
    right.grid(row=1,column=1,sticky='news')

    bottom = Frame(master,bg='#B82132')
    bottom.grid(row=2,columnspan=2,sticky='news')

    return(top,left,right,bottom)

def widgets(top,left,right,bottom):
    #TOP
    heading = Label(top,bg='#B82132',text='Dream Cafe by Bongkodphetr Yotkathok',fg='white',font=('Jetbrains Mono',24,'bold'))
    heading.pack(pady=15)
    #RIGHT
    summary = Label(right,bg='#F6DED8',text='Thank you for your shopping\n Total price is',font=('Jetbrains Mono',24,'bold'))
    summary.pack(pady=50)
    showNet = Label(right,bg='#F6DED8',text='Total = 0.00 Baht',font=('Jetbrains Mono',24),fg='blue')
    showNet.pack(pady=15)

    #LEFT AND MERGE ROW-COL
    order1 = Label(left, image=cake1,bg='#F2B28C')
    order1.grid(row=0,column=0,rowspan=2,sticky=E)
    detail1 = Label(left,bg='#F2B28C',text='Chocolate cake\nPrice 160 Baht')
    detail1.grid(row=0,column=1,sticky=S)
    amount1 = Spinbox(left,from_=0,to=100,justify='center',width=10,textvariable=spy1,command=userClick)
    amount1.grid(row=1,column=1,sticky=N)

    order2 = Label(left, image=cake2,bg='#F2B28C')
    order2.grid(row=2,column=0,rowspan=2,sticky=E)
    detail2 = Label(left,bg='#F2B28C',text='Strawberry cake\nPrice 140 Baht')
    detail2.grid(row=2,column=1,sticky=S)
    amount2 = Spinbox(left,from_=0,to=100,justify='center',width=10,textvariable=spy2,command=userClick)
    amount2.grid(row=3,column=1,sticky=N)
    
    order3 = Label(left, image=cake3,bg='#F2B28C')
    order3.grid(row=4,column=0,rowspan=2,sticky=E)
    detail3 = Label(left,bg='#F2B28C',text='Pony Donut\nPrice 75 Baht')
    detail3.grid(row=4,column=1,sticky=S)
    
    amount3 = Spinbox(left,from_=0,to=100,justify='center',width=10,textvariable=spy3,command=userClick)
    amount3.grid(row=5,column=1,sticky=N)
    #BOTTOM
    btn1= Button(bottom,text='Exit Program', command=exit)
    btn1.pack(pady=15,ipadx=20,ipady=5,side=RIGHT,padx=20)
    return(showNet)

def userClick(): #Call back fn
    net = spy1.get()*160 + spy2.get()*140 + spy3.get()*75
    showNet['text'] = f'Total = {net:0.2f} Baht'

#Main
master = createWindow()
cake1 = PhotoImage(file='image/cake1.png')
cake2 = PhotoImage(file='image/cake2.png')
cake3 = PhotoImage(file='image/cake3.png')
spy1,spy2,spy3 = IntVar(),IntVar(),IntVar()
net = 0
top,left,right,bottom = frameLayout(master)
showNet = widgets(top,left,right,bottom)
master.mainloop()