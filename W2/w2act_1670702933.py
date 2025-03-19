from tkinter import *

def mainwindow() :
    master = Tk()
    master.wm_geometry("600x500+300+100")
    master.wm_title("Week2 : Created by Bongkodpetr Yotkathok")
    master.configure(bg="#98D8EF") #config window backgroud color
    master.option_add('*font','Poppins 16') #config font 

    master.grid_rowconfigure((0,3),weight=5)
    master.grid_rowconfigure((1,2),weight=1)
    master.grid_columnconfigure((0,1),weight=1)
    return(master) 
def widget(master) : 
    heading = Label(master,text="Login Window",font=('Poppins',22,'bold'),bg='#98D8EF',fg='blue')
    heading.grid(row=0 , columnspan= 2)

    userlabel = Label(master,text="Username : ",bg="#98D8EF")
    userlabel.grid(row=1,column=0 ,sticky=E)
    pwdlabel = Label(master,text="Password : ",bg="#98D8EF")
    pwdlabel.grid(row=2,column=0 ,sticky=E)
    
    userbox = Entry(master,width=20)
    userbox.grid(row=1,column=1,sticky=W)
    pwdbox = Entry(master,width=20 , show='*')
    pwdbox.grid(row=2,column=1 , sticky=W)

    btn1 = Button(master,text="Cencel",width=20)
    btn1.grid(row=3 , column=0 , sticky=E , padx=10)
    btn2 = Button(master,text="Login",width=20)
    btn2.grid(row=3 , column=1 , sticky=W , padx=10)

master = mainwindow()
widget(master)  
master.mainloop()