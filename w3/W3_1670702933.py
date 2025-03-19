from tkinter import *
from tkinter import messagebox

def createWindow():
        master = Tk()
        master.wm_geometry("1000x800")
        master.title('Art Toy Shop created by Bongkodphetr Yotkathok')
        master.grid_rowconfigure((0,2), weight=1)
        master.grid_rowconfigure(1,weight=5)
        master.grid_columnconfigure((0,1), weight=1)
        master.configure(bg='#493D9E')
        master.option_add('*Font', 'Helvetica 12')
        return(master)
def framLayout(master) :
        top = Frame(master, bg='#3A3960')   
        top.grid(row=0, columnspan=2, sticky='news')

        left = Frame(master, bg='#A9BFA8')
        left.grid_columnconfigure(0,weight=1)
        left.grid_rowconfigure((0,1,2),weight=1)
        left.grid(row=1, column=0, sticky='news')
        
        right = Frame(master, bg='#5E686D')
        right.grid_rowconfigure((0,1,2),weight=1)
        right.grid_columnconfigure(0,weight=1)
        right.grid(row=1, column=1, sticky='news')
        bottom = Frame(master, bg='#FFF2AF')
        bottom.grid_rowconfigure(0,weight=1)
        bottom.grid_columnconfigure((0,1),weight=1)
        bottom.grid(row=2, columnspan=2, sticky='news')
        return(top,left,right,bottom)

def createWidget(top,left,right,bottom) :
        heading = Label(top,text='Art Toy by Popmart Official Store' , fg='#E7D283', font=('comic sans ms',22,'bold'),bg='#3A3960')
        heading.pack(pady=15)
        figure1 = Label(left,bg='#A9BFA8', image=toy1)
        figure1.grid(row=0)
        figure2 = Label(left,bg='#A9BFA8', image=toy2)
        figure2.grid(row=1)
        figure3 = Label(left,bg='#A9BFA8', image=toy3)
        figure3.grid(row=2)

        order1 = Button(right, text="Select Figure1", image=icon, compound=LEFT, command=order1Click)
        order1.grid(row=0, ipadx=15)
        order2 = Button(right, text="Select Figure2", image=icon, compound=LEFT, command=order2Click)
        order2.grid(row=1, ipadx=15)
        order3 = Button(right, text="Select Figure3", image=icon, compound=LEFT, command=order3Click)
        order3.grid(row=2, ipadx=15)
        btn1 = Button(bottom,text='Order')
        btn1.grid(row=0,column=0,sticky=E,padx=10,ipadx=15,pady=15)
        btn2 = Button(bottom,text='Exit',command=quit)
        btn2.grid(row=0,column=1,sticky=W,padx=10)

def order1Click():
        messagebox.showinfo('Admin:', 'You ordered Skullpanda')

def order2Click():
        messagebox.showinfo('Admin:', 'You selected Dimoo')

def order3Click():
        messagebox.showinfo('Admin:', 'You selected Crybaby')
#Main

master = createWindow()
toy1 = PhotoImage(file='image/skullpanda.png').subsample(3,3)
toy2 = PhotoImage(file='image/dimoo.png').subsample(3,3)
toy3 = PhotoImage(file='image/crybaby.png').subsample(3,3)
icon = PhotoImage(file='image/icon1.png')
top,left,right,bottom = framLayout(master)
createWidget(top,left,right,bottom)
master.mainloop()