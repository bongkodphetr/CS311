from tkinter import *
from tkinter import messagebox
import sqlite3

def connection() :
    conn = sqlite3.connect('db/member.db')
    cursor = conn.cursor()
    return(conn,cursor)


def mainwindow() :  
    master = Tk()
    w = 1000
    h = 700
    x = master.winfo_screenwidth()/2 - w/2
    y = master.winfo_screenheight()/2 - h/2
    master.geometry("%dx%d+%d+%d"%(w,h,x,y))
    master.config(bg='#EDDFE0')
    master.title("Login Application : ")
    master.option_add('*font',"Garamond 24 bold")
    master.grid_rowconfigure(0,weight=1)
    master.grid_rowconfigure(1,weight=3)
    master.grid_columnconfigure((0),weight=1)
    # master.grid_columnconfigure((1),weight=4)
    return(master)
def layout() :
    # left = Frame(master,bg='#AB886D')
    top.grid(row=0,sticky='news')
    top.rowconfigure(0,weight=1)
    top.columnconfigure(0,weight=1)
    # right = Frame(master,bg='#D6C0B3')
    center.grid(row=1,sticky='news')
    center.rowconfigure((0,1,2,3,4),weight=1)
    center.columnconfigure((0,1),weight=1)

def loginwindow() :
    global userentry,pwdentry
    Label(top,image=img1,bg='#493628').grid(row=0,sticky='nswe')
    Label(center,text="Login Window",bg='#493628',font=('Garamond',32,'bold'),fg='white').grid(row=0,column=0,columnspan=2,sticky='news',ipady=30)
    Label(center,text="Username : ",bg='#D6C0B3',).grid(row=1,column=0,padx=10,pady=20,sticky='e')
    Label(center,text="Password : ",bg='#D6C0B3').grid(row=2,column=0,padx=10,pady=20,sticky='e')
    userentry = Entry(center,textvariable=userinfo)
    userentry.grid(row=1,column=1,padx=10,pady=20,sticky='w')
    pwdentry = Entry(center,show='*',textvariable=pwdinfo)
    pwdentry.grid(row=2,column=1,padx=10,pady=20,sticky='w')
    Button(center,text="Login",bg='#E4E0E1',width=20, command=loginclick).grid(row=4,column=1,padx=10,pady=60,ipady=20,sticky='w')
    Button(center,text="Register",bg='#E4E0E1',width=20).grid(row=4,column=0,padx=10,pady=60,ipady=20,sticky='e')

def loginclick() :
    if userinfo.get() == "" :
        messagebox.showwarning("Admin","Please enter username")
        userentry.focus_force()
    elif pwdinfo.get() == "" :
        messagebox.showwarning("Admin","Please enter password")
        pwdentry.focus_force()
    else :
        sql = "select * from login where user=?"
        cursor.execute(sql,[userinfo.get()])
        result = cursor.fetchone()
        if result :
            sql = "select * from login where user=? and pwd=?"
            cursor.execute(sql,[userinfo.get(), pwdinfo.get()])
            result = cursor.fetchone()
            if result :
                welcomepage(result[2]+" "+result[3])
            else :
                messagebox.showwarning("Admin","Invalid password")
                pwdentry.delete(0, END)
                pwdentry.focus_force()
        else :
            messagebox.showwarning("Admin","Invalid username")
            userentry.select_range(0, END)
            userentry.focus_force()

def welcomepage(name) :
    top.grid_forget()
    center.grid_forget()
    top2.grid(row=0 , sticky='news')
    top2.rowconfigure(0,weight=1)
    top2.columnconfigure(0,weight=1)
    Label(top2, bg='#493628', text='Welcome to My Application',font=('garamond', 32, 'bold'),fg="white").grid(row=0)
    welcome.grid(row=1,sticky='news')
    welcome.rowconfigure((0,1),weight=1)
    welcome.columnconfigure((0,1),weight=1)
    Label(welcome,bg='#D6C0B3',image=img2).grid(row=0, column=0, rowspan=2)
    Label(welcome,bg='#D6C0B3',text="Information :\n"+ name).grid(row=0, column=1,sticky=S)
    Button(welcome, text="Exit Program",width=15, command=exit).grid(row=1,column=1)
#main
#call connection function
conn,cursor = connection()
master = mainwindow()
img1 = PhotoImage(file="images/login2.png")
img2 = PhotoImage(file="images/profile.png")
icon1 = PhotoImage(file="images/icon1.png")
top = Frame(master,bg='#AB886D')
top2 = Frame(master,bg='#493628')
center = Frame(master,bg='#D6C0B3')
welcome = Frame(master,bg='#D6C0B3')
userinfo = StringVar()
pwdinfo = StringVar()
layout()
loginwindow()
master.mainloop()
cursor.close()
conn.close()
# End of w9_act1.py