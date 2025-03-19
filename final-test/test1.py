from tkinter import *

def createWindow():
    master = Tk()
    master.geometry('800x700')
    master.option_add("*font","tahoma 14")
    master.title("Final")
    master.configure(bg='blue')
    master.grid_rowconfigure((0,2), weight=1)
    master.grid_rowconfigure(1,weight=5)
    master.grid_columnconfigure(0,weight=1)
    master.grid_columnconfigure(1,weight=3)
    return(master)

def layout(master):
    top.grid_columnconfigure((0,1,2), weight=1)
    top.grid_rowconfigure((0),weight=1)
    top.grid(row=0,columnspan=2, sticky='news')

    bottom.grid_rowconfigure(0, weight=1)
    bottom.grid_columnconfigure((0,1),weight=1)
    bottom.grid(row=2, columnspan=2, sticky='news')

def topframe(top):
    Button(top,text='Cake Menu', image=cake1,compound='top').grid(row=0, column=0, sticky='news')
    Button(top,text='Cake Menu', image=cake1,compound='top').grid(row=0, column=1, sticky='news')
    Button(top,text='Cake Menu', image=cake1,compound='top').grid(row=0, column=2, sticky='news')

def bottomframe(bottom): 
    Button(bottom,text='Reset Submit', image=icon1,compound='bottom').grid(row=0,column=0,sticky='news')
    Button(bottom,text='Exit',image=icon1, compound='bottom',command=exit).grid(row=0, column=1 , sticky='news')



master = createWindow()

top = Frame(master,bg="red")
bottom = Frame(master,bg='green')
cake1 = PhotoImage(file='image/cake1.png')
icon1 = PhotoImage(file='image/icon1.png')
layout(master)
topframe(top)
bottomframe(bottom)
master.mainloop()