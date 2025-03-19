from tkinter import *
from tkinter import messagebox
import sqlite3

def connection() :
    print("Connection")
    conn = sqlite3.connect("db/member.db")
    cursor = conn.cursor()
    return(conn,cursor)

def mainwindow() :  
    master = Tk()
    w = 1000
    h = 800
    x = master.winfo_screenwidth()/2 - w/2
    y = master.winfo_screenheight()/2 - h/2
    master.geometry("%dx%d+%d+%d"%(w,h,x,y))
    master.config(bg='#EDDFE0')
    master.title("Login Application : ")
    master.option_add('*font',"Garamond 24 bold")
    master.grid_rowconfigure(0,weight=1)
    master.grid_rowconfigure(1,weight=4)
    master.grid_columnconfigure((0),weight=1)
    # master.grid_columnconfigure((1),weight=4)
    return(master)
def layout() :
    # left = Frame(master,bg='#AB886D')
    top.grid(row=0,sticky='news')
    top.rowconfigure((0,1),weight=1)
    top.columnconfigure(0,weight=1)
    # right = Frame(master,bg='#D6C0B3')
    center.grid(row=1,sticky='news')
    center.rowconfigure((0,3),weight=2)
    center.rowconfigure((1,2),weight=1)
    center.columnconfigure((0,1),weight=1)

def loginwindow() :
    global userentry,pwdentry
    Label(top,image=img1,bg='#493628').grid(row=0,sticky='nswe')
    Label(top,text="Login Window",bg='#493628',font=('Garamond',32,'bold'),fg='white').grid(row=1,column=0,columnspan=2,sticky='news',ipady=30)
    Label(center,text="Username : ",bg='#D6C0B3').grid(row=1,column=0,padx=10,pady=20,sticky='e')
    Label(center,text="Password : ",bg='#D6C0B3').grid(row=2,column=0,padx=10,pady=20,sticky='e')
    userentry = Entry(center,textvariable=userinfo)
    userentry.grid(row=1,column=1,padx=10,pady=20,sticky='w')
    pwdentry = Entry(center,show='*',textvariable=pwdinfo)
    pwdentry.grid(row=2,column=1,padx=10,pady=20,sticky='w')
    Button(center,text="Login",width=20,command=loginclick).grid(row=3,column=1,padx=10,pady=60,ipady=20,sticky='w')
    Button(center,text="Register",width=20,command=registerclick).grid(row=3,column=0,padx=10,pady=60,ipady=20,sticky='e')

def registerclick() :
    global name,username,password,cfpassword
    print("Register Click")
    center.grid_forget()
    top.grid(row=0,sticky='news')
    top.rowconfigure((0,1),weight=1)
    top.columnconfigure(0,weight=1)
    register.grid(row=1,sticky='news')
    register.rowconfigure((0,1,2,3,4),weight=1)
    register.columnconfigure((0,1),weight=1)
    Label(top,text="Register Window",bg='#493628',font=('Garamond',32,'bold'),fg='white').grid(row=1)
    Label(register,text="Full Name : ",bg='#D6C0B3').grid(row=0, column=0,sticky=E, padx=10)
    Label(register,text="Username : ",bg='#D6C0B3').grid(row=1, column=0,sticky=E, padx=10)
    Label(register,text="Password : ",bg='#D6C0B3').grid(row=2, column=0,sticky=E, padx=10)
    Label(register,text="Confirm Password : ",bg='#D6C0B3').grid(row=3, column=0,sticky=E, padx=10)
    name = Entry(register)
    name.grid(row=0, column=1,sticky=W,padx=10)
    username = Entry(register)
    username.grid(row=1, column=1,sticky=W,padx=10)
    password = Entry(register,show='*')
    password.grid(row=2, column=1,sticky=W,padx=10)
    cfpassword = Entry(register,show='*')
    cfpassword.grid(row=3, column=1,sticky=W,padx=10)
    Button(register,text="Register Submit",width=20,command=registersubmit).grid(row=4, columnspan=2 , ipady=10, pady=10)
    

def registersubmit() : 
    print("Register Submit")

    if name.get() =="":
        messagebox.showwarning("Admin","Please enter full name")
        name.focus_force()
    elif username.get() =="":
        messagebox.showwarning("Admin","please enter username")
        username.focus_force()
    elif password.get() == "" :
        messagebox.showwarning("Admin","Please enter password")
        password.focus_force()
    elif cfpassword.get() == "" :
        messagebox.showwarning("Admin","Please enter confirm password")
        cfpassword.focus_force()
    elif password.get() != cfpassword.get() :
        messagebox.showwarnin("Admin","Your password and confirm not match")
        password.delete(0,END)
        cfpassword.delete(0,END)
        password.focus_force()
    else :
        sql = "select * from login where user=?"
        cursor.execute(sql, [username.get()])
        result = cursor.fetchone()
        if result:
            messagebox.showwarning("Admin","Username is already exist")
            username.delete(0, END)
            username.focus_force()
        else :
            sql = "select * from login where name=? collate nocase"
            cursor.execute(sql,[name.get()])
            result = cursor.fetchall()
            if result :
                messagebox.showwarning("Admin","You have already register\n Please back to login")
                name.selection_range(0, END)
                name.focus_force()
            else:
                sql = "insert into login values (?,?,?)"
                cursor.execute(sql, [username.get(),password.get(),name.get()])
                conn.commit()
                messagebox.showinfo("Admin","Register successfully")
                backtologin()

def loginclick() :
    print("Login Click")
    if userinfo.get() == "" :
        messagebox.showwarning("Admin","Please enter username")
        userentry.focus_force()
    elif pwdinfo.get() == "" :
        messagebox.showwarning("Admin","Please enter password")
        pwdentry.focus_force()
    else :
        sql = "select * from login where user=?"             
        cursor.execute(sql,[userinfo.get()])
        result = cursor.fetchall()
        if result :
            sql = "select * from login where user=? and pwd=?"
            cursor.execute(sql,[userinfo.get(),pwdinfo.get()])
            result = cursor.fetchone()
            if result :
                messagebox.showinfo("Admin","Login Successful")
                welcomepage(result[2])
            else :
                messagebox.showwarning("Admin","Invalid Password")
                pwdentry.selection_range(0,END)
                pwdentry.focus_force()
        else :
            messagebox.showwarning("Admin","Invalid Username")
            userentry.selection_range(0,END)
            userentry.focus_force()

def welcomepage(name) :
    print(name)
    top.grid_forget()
    center.grid_forget()
    top2.grid(row=0,sticky='news')
    top2.grid_rowconfigure(0,weight=1)
    top2.grid_columnconfigure(0,weight=1)
    welcome.grid(row=1,sticky='news')
    welcome.grid_rowconfigure((0,1,2),weight=1)
    welcome.grid_columnconfigure((0,1),weight=1)
    Label(top2,text="Welcome to My Application",bg="#493628",fg="white",font=('Garamond',32,'bold')).grid(row=0,sticky='news',ipady=30)
    Label(welcome,image=img2,bg='#D6C0B3').grid(row=1,column=0,rowspan=2)
    Label(welcome,text="Information : \n"+name,bg='#D6C0B3').grid(row=1,column=1,sticky=S,ipadx=20)
    Button(welcome,text="Back to Login",command=backtologin,bg='#E4E0E1',width=20).grid(row=2,column=1,ipady=10)


def backtologin() :
    top2.grid_forget()
    welcome.grid_forget()
    register.grid_forget()
    top.grid(row=0,sticky='news')
    center.grid(row=1,sticky='news')
    userentry.delete(0,END)
    pwdentry.delete(0,END)
    userentry.focus_force()

#main
#call connection function
conn,cursor = connection()
master = mainwindow()
img1 = PhotoImage(file="images/login2.png")
img2 = PhotoImage(file="images/profile.png")
icon1 = PhotoImage(file="images/icon1.png")
top = Frame(master,bg='#493628')
top2 = Frame(master,bg='#493628')
center = Frame(master,bg='#D6C0B3')
welcome = Frame(master,bg='#D6C0B3')
register = Frame(master,bg='#D6C0B3')
userinfo = StringVar()
pwdinfo = StringVar()
layout()
loginwindow()
master.mainloop()
cursor.close()
conn.close()
# End of w9_act1.py