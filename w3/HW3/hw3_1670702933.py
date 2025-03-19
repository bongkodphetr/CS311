from tkinter import *
from tkinter import messagebox


def createLayout():
        master = Tk()
        master.wm_geometry("1000x800")
        master.title('Art Toy Shop created by Bongkodphetr Yotkathok')
        master.grid_rowconfigure((0,2), weight=1)
        master.grid_rowconfigure(1,weight=5)
        master.grid_columnconfigure(0,weight=15)
        master.grid_columnconfigure(1,weight=1)
        master.configure(bg='#493D9E')
        master.option_add('*Font', 'Helvetica 12')
        return(master)

def framLayout(master):
        top = Frame(master, bg='#9ACBD0')
        top.grid(row=0, columnspan=2, sticky='news')

        left = Frame(master, bg='#ff6161')
        left.grid_columnconfigure(0,weight=1)
        left.grid_rowconfigure((0,1,2),weight=2)
        left.grid(row=1, column=0, sticky='news')
        
        right = Frame(master, bg='#F2B28C')
        right.grid_rowconfigure((0,1,2),weight=1)
        right.grid_columnconfigure(0,weight=1)
        right.grid(row=1, column=1, sticky='news')
        bottom = Frame(master, bg='#3B6790')
        bottom.grid_rowconfigure(0,weight=1)
        bottom.grid_columnconfigure((0,1,2,3),weight=1)
        bottom.grid(row=2, columnspan=3, sticky='news')
        return(top,left,right,bottom)

def createWidget(top,left,right,bottom):
         heading = Label(top,text='Dashboard by Bongkodphetr Yotkathok' ,pady=10, fg='white', font=('JetBrains Mono',30,'bold'),bg='#9ACBD0')
         heading.pack(pady=5)
         name = Label(left,text='Bongkodphetr Yotkathok' , font=('JetBrains Mono',26,'bold'),bg='#ff6161')
         name.place(x=280 ,y=200)
         position = Label(left,text='Student' ,  font=('JetBrains Mono',22,'bold'),bg='#ff6161')
         position.place(x=280 ,y=250)
         fac = Label(left,text='Information Technology and Innovation' ,  font=('JetBrains Mono',15,'bold'),bg='#ff6161')
         fac.place(x=280 ,y=300)
         skill = Label(right,bg='#A9BFA8', image=skill1)
         skill.grid(row=1, pady=10)
         skill_bar = Label(left,bg='#A9BFA8',image=skill2)
         skill_bar.place(x=100,y=450)
         ava = Label(left,bg='#ff6161', image=avatar)
         ava.place(x=10,y=100)

         btn1 = Button(bottom,text='CLICK ME1')
         btn1.grid(row=0,column=0,sticky=E,padx=10,ipadx=15,pady=15,ipady=30)
         btn3 = Button(bottom,text='CLICK ME2')
         btn3.grid(row=0,column=1,sticky=E,padx=10,ipadx=15,pady=15,ipady=30)
         btn4 = Button(bottom,text='CLICK ME3')
         btn4.grid(row=0,column=2,sticky=E,padx=10,ipadx=15,pady=15,ipady=30)
         btn2 = Button(bottom,text='EXIT',command=quit)
         btn2.grid(row=0,column=3,sticky=E,padx=10,ipadx=30,pady=15,ipady=30)
def order1Click():
        messagebox.showinfo('Admin:', 'You ordered Skullpanda')

def order2Click():
        messagebox.showinfo('Admin:', 'You selected Dimoo')

def order3Click():
        messagebox.showinfo('Admin:', 'You selected Crybaby')
#Main


master = createLayout()
skill1 = PhotoImage(file='skill.png').subsample(1)
skill2 = PhotoImage(file='barcolor.png').subsample(2)
avatar =PhotoImage(file='male.png').subsample(2)
top,left,right,bottom = framLayout(master)
createWidget(top,left,right,bottom)
master.mainloop()


