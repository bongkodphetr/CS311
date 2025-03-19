from tkinter import *
# >29 = red, >24 = orange, >22 = yellow, >18.4 = lightgreen
def mainwindow() : 
    root = Tk()
    root.geometry('500x500+400+200')
    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=2)
    root.rowconfigure((0,1,2,3),weight=1)
    root.title("Binding : BMI Calculating")
    root.option_add("*font","courier 12")
    return root

def toplayout(root) :
    frame1 = Frame(root,bg='lightpink')
    frame1.columnconfigure((0,1),weight=1)
    frame1.grid(row=0,column=0,columnspan=2,sticky='news')
    spy1 = IntVar()
    spy1.set(2)
    Radiobutton(frame1,image=boy,bg='lightpink',variable=spy1,value=1).grid(row=0,column=0,pady=10)
    Radiobutton(frame1,image=girl,bg='lightpink',variable=spy1,value=2).grid(row=0,column=1,pady=10)
    return spy1

def widget(root) :
    Label(root,text="weight (kg.)").grid(row=1,column=0,sticky="news",padx=20)
    Label(root,text="height (cm.)").grid(row=2,column=0,sticky="news",padx=20,pady=15)
    #crate weight scale widget
    w = Scale(root,from_=1,to=100,length=200,width=30,orient=HORIZONTAL,bg='lightblue')
    w.grid(row=1,column=1,sticky="news",pady=20,padx=20)
    w.set(50)
    w.bind('<B1-Motion>',bmi)
    w.bind('<Button-1>',bmi)
    #create height scale widget
    h = Scale(root,from_=100,to=200,length=200,width=30,orient=HORIZONTAL,bg='yellow')
    h.set(160)
    h.grid(row=2,column=1,sticky="news",pady=15,padx=20)
    h.bind('<B1-Motion>',bmi)
    h.bind('<Button-1>',bmi)
    #create a label to display bmi and set co
    lbBmi = Label(root,textvariable=cal_bmi,font='Garamond 40 bold')
    lbBmi.grid(row=3,columnspan=2,pady=10,sticky="news",ipady=15)
    return(h,w,lbBmi)
    
def bmi(e) :
    bmi = w.get()/ (h.get()/100)**2
    cal_bmi.set("BMI = %0.2f"%bmi)
    zone = ""
    if spy1.get() == 1 :
        if bmi > 29.99 : 
            zone = "red"
        elif bmi > 24.99 :
            zone = "orange"
        elif bmi > 18.99 :
            zone = "lightgreen"
        else :
            zone = 'red'
    else :
        if bmi > 29.99 : 
            zone = "red"
        elif bmi > 23.99 :
            zone = "orange"
        elif bmi > 18.01 :
            zone = "lightgreen"
        else :
            zone = 'red'
    lbBmi['bg'] = zone

root = mainwindow()
boy = PhotoImage(file="image/boy.png")
girl = PhotoImage(file="image/girl.png")
cal_bmi = StringVar()
spy1 = toplayout(root)
h,w,lbBmi = widget(root)
root.mainloop()