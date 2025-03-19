from tkinter import *

top = Tk()
top.title("Bongkodpetr")
top.wm_geometry("1000x500")
top.config(bg='#AEEA94')

top.grid_rowconfigure(0,weight=10)
top.grid_rowconfigure(1,weight=1)

top.grid_columnconfigure((0,1),weight=1)
btn1 = Button(top,text='Cancel',width=20)
btn1.grid(row=1 , column=0 , pady=20, ipady=20 , ipadx=15 , sticky= E , padx = 10)
btn2 = Button(top,text='Login',width=20)
btn2.grid(row=1 , column=1 , pady=20, ipady=20 , ipadx=15 , sticky= W , padx = 10)

top.mainloop()