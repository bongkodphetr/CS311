from tkinter import *

def mainwindow() :
    master = Tk()
    master.wm_geometry("600x500+300+100")
    master.wm_title("Week2 : Created by Bongkodpetr Yotkathok")
    master.configure(bg="#98D8EF") #config window backgroud color
    master.option_add('*font','Poppins 16') #config font 

    master.grid_rowconfigure((0,6),weight=5)
    master.grid_rowconfigure((1,2,3,4,5),weight=1)
    master.grid_columnconfigure((0,1),weight=1)
    return(master) 
def widget(master) : 
    heading = Label(master,text="Registration Form",font=('Poppins',22,'bold'),bg='#98D8EF',fg='blue')
    heading.grid(row=0 , columnspan= 2)

    namelabel = Label(master,text="Name : ",bg="#98D8EF")
    namelabel.grid(row=1,column=0 ,sticky=E)
    Idlabel = Label(master,text="Student ID : ",bg="#98D8EF")
    Idlabel.grid(row=2,column=0 ,sticky=E)
    depart_label = Label(master,text="Department : ",bg="#98D8EF")
    depart_label.grid(row=3,column=0 ,sticky=E)
    Secu_label = Label(master,text="Security Question : ",bg="#98D8EF")
    Secu_label.grid(row=4,column=0 ,sticky=E)
    
    namebox = Entry(master,width=20)
    namebox.grid(row=1,column=1,sticky=W)
    idbox = Entry(master,width=20 , show='*')
    idbox.grid(row=2,column=1 , sticky=W)
    depart_box = Entry(master,width=20)
    depart_box.grid(row=3,column=1,sticky=W)
    sec_box = Entry(master,width=20 , show='*')
    sec_box.grid(row=4,column=1 , sticky=W)

    btn1 = Button(master,text="Cencel",width=20)
    btn1.grid(row=5 , column=0 , sticky=E , padx=30)
    btn2 = Button(master,text="Login",width=20)
    btn2.grid(row=5 , column=1 , sticky=W , padx=30)

    heading = Label(master,text="Created by Bongkodphetr Yotkathok, ID=1670702933",font=('Poppins',13,'normal'),bg='#98D8EF',fg='blue')
    heading.grid(row=6 , columnspan= 2)
master = mainwindow()
widget(master)  
master.mainloop()