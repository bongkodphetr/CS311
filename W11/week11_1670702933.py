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
    w = 1200
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
    Label(top,text="Login Window",bg='#493628',font=('JetBrains Mono',32,'bold'),fg='white').grid(row=1,column=0,columnspan=2,sticky='news',ipady=30)
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
    Label(top,text="Register Window",bg='#493628',font=('JetBrains Mono',32,'bold'),fg='white').grid(row=1)
    Label(register,text="Full Name : ",bg='#D6C0B3').grid(row=0,column=0,padx=10,sticky=E)
    Label(register,text="Username : ",bg='#D6C0B3').grid(row=1,column=0,padx=10,sticky=E)
    Label(register,text="Password : ",bg='#D6C0B3').grid(row=2,column=0,padx=10,sticky=E)
    Label(register,text="Confirm Password : ",bg='#D6C0B3').grid(row=3,column=0,padx=10,sticky=E)
    name = Entry(register)
    name.grid(row=0,column=1,padx=10,sticky=W)
    username = Entry(register)
    username.grid(row=1,column=1,padx=10,sticky=W)
    password = Entry(register,show='*')
    password.grid(row=2,column=1,padx=10,sticky=W)
    cfpassword = Entry(register,show='*')
    cfpassword.grid(row=3,column=1,padx=10,sticky=W)
    Button(register,text="Register Submit",width=20,command=registersubmit).grid(row=4,columnspan=2,pady=10,ipady=10)
    

def registersubmit() : 
    print("Register Submit")
    if name.get() == "" :
        messagebox.showwarning( "Admin","Please enter Full Name")
        name.focus_force()
    elif username.get() == "" :
        messagebox.showwarning( "Admin","Please enter Username")
        username.focus_force()
    elif password.get() == "" :         
        messagebox.showwarning( "Admin","Please enter Password")
        password.focus_force()
    elif cfpassword.get() == "" :
        messagebox.showwarning( "Admin","Please enter Confirm Password")
        cfpassword.focus_force()
    elif password.get() != cfpassword.get() :
        messagebox.showwarning( "Admin","Password and Confirm Password not match")
        password.delete(0,END)
        cfpassword.delete(0,END)
        password.focus_force()
    else :
        sql = "select * from login where user=?"
        cursor.execute(sql,[username.get()])
        result = cursor.fetchone()
        if result :
            messagebox.showwarning("Admin","Username already exists")
            username.delete(0,END)
            username.focus_force()
        else :
            sql = "select * from login where name=? collate nocase"
            cursor.execute(sql,[name.get()])
            result = cursor.fetchone()
            if result :
                messagebox.showwarning("Admin","You have already registered")
                name.delete(0,END)
                name.focus_force()
            else :
                sql = "insert into login values (?,?,?)"
                cursor.execute(sql,[username.get(),password.get(),name.get()])
                conn.commit()
                messagebox.showinfo("Admin","Register Successful")
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
    Label(top2,text="Welcome to My Application",bg="#493628",fg="white",font=('JetBrains Mono',32,'bold')).grid(row=0,sticky='news',ipady=30)
    Label(welcome,image=img2,bg='#D6C0B3').grid(row=0,column=0,rowspan=2)
    Label(welcome,text="Information : \n"+name,bg='#D6C0B3').grid(row=0,column=1,rowspan=2,ipadx=20)
    Button(welcome,text="Back to Login",command=backtologin,bg='#E4E0E1',width=20).grid(row=2,column=0,ipady=10,sticky=E,padx=10)
    Button(welcome,text="Update Data",command=updateclick,bg='#E4E0E1',width=20).grid(row=2,column=1,ipady=10,sticky=W,padx=10)


def updateclick() :
    global searchentry
    print("Update Click")
    top2.grid_forget()
    welcome.grid_forget()
    top.grid(row=0,sticky='news')
    top.rowconfigure((0,1),weight=1)
    top.columnconfigure(0,weight=1)
    update.grid(row=1,sticky='news')
    update.grid_rowconfigure((0),weight=1)
    update.grid_columnconfigure((0),weight=1)
    update.grid_columnconfigure((1),weight=2)
    left.grid(row=0,column=0,rowspan=5,sticky='news')
    left.grid_rowconfigure((0,1,2,3,4),weight=1)
    left.grid_columnconfigure((0,1,2),weight=1)
    #Label(top,image=img1,bg='#493628')
    Label(top,text="Update Window",bg='#493628',font=('JetBrains Mono',32,'bold'),fg='white').grid(row=1)
    Label(left,text="Username : ",bg='#F5EFE7').grid(row=0 , column=0, sticky=E)
    searchentry = Entry(left)
    searchentry.grid(row=0,column=1,sticky=W)
    Button(left,text="Search",command=searchclick).grid(row=0,column=2, sticky=W)


def searchclick() :
    print("Search Click")
    if searchentry.get() == "" : #ถ้าช่องว่าง
        messagebox.showwarning("Admin","Please enter username")
        searchentry.focus_force()
    else :
        sql = "select * from login where user=?"
        cursor.execute(sql,[searchentry.get()])
        result = cursor.fetchone()
        if result : 
            # print(result)
            updatepage(result)
        else : #ถ้าไม่เจอ
            messagebox.showwarning("Admin","Username not found")
            searchentry.delete(0, END)
            searchentry.focus_force()
            userupdate.delete(0,END)
            pwdupdate.delete(0, END)
            cfupdate.delete(0, END)
            nameupdate.delete(0, END)
            right.grid_forget()
            

            

def updatepage(result) :
    global  nameupdate,userupdate,pwdupdate,cfupdate
    right.grid(row=0,column=1,rowspan=5,sticky='news')
    right.grid_rowconfigure((0,1,2,3,4),weight=1)
    right.grid_columnconfigure((0,1),weight=1)
    Label(right,text="Full Name : ",bg='#D8C4B6').grid(row=0, column=0, sticky=E, padx=10)
    Label(right,text="Username : ",bg='#D8C4B6').grid(row=1, column=0, sticky=E, padx=10)
    Label(right,text="Password : ",bg='#D8C4B6').grid(row=2, column=0, sticky=E, padx=10)
    Label(right,text="Confirm Password : ",bg='#D8C4B6').grid(row=3, column=0, sticky=E, padx=10)

    userinfo.set(result[0])
    pwdinfo.set(result[1])
    cfinfo.set(result[1])
    nameinfo.set(result[2])

    nameupdate = Entry(right,textvariable=nameinfo,fg='blue')
    nameupdate.grid(row=0, column=1, sticky=W, padx=10 )

    userupdate = Entry(right,textvariable=userinfo,fg='blue',state=DISABLED)
    userupdate.grid(row=1, column=1, sticky=W, padx=10 )

    pwdupdate = Entry(right,textvariable=pwdinfo,fg='blue',show='*')
    pwdupdate.grid(row=2, column=1, sticky=W, padx=10 )
    
    cfupdate = Entry(right,textvariable=cfinfo,fg='blue',show='*')
    cfupdate.grid(row=3, column=1, sticky=W, padx=10 )
    
    Button(right,text="Update",command=updatesubmit).grid(row=4 , column=1, sticky=W, padx=10)
    Button(right,text="Go to Login",command=backtologin).grid(row=4 , column=0, sticky=E, padx=10 )

def updatesubmit() :
    print('Update Submit')
    if nameinfo.get() == "" :
        messagebox.showwarning("Admin","Please enter Full Name")
        nameupdate.focus_force
    elif pwdinfo.get() == "" :
        messagebox.showwarning("Admin","Please enter Password")
        pwdupdate.focus_force
    elif cfinfo.get() == "" :
        messagebox.showwarning("Admin", "Please enter Confirm Password")
        cfupdate.focus_force()
    elif pwdinfo.get() != cfinfo.get() :
        messagebox.showwarning("Admin","Password and Confirm Passowrd not match")
        pwdupdate.delete(0, END)
        cfupdate.delete(0, END)
    else :
        sql = """ 
            update login
            set name=?, pwd=?
            where user=?
        """ 
        cursor.execute(sql, [nameinfo.get(),pwdinfo.get(),userinfo.get()])
        conn.commit()
        messagebox.showinfo("Admin", "Update Successfully")        
        searchentry.delete(0,END)
        nameupdate.delete(0,END)
        userupdate.delete(0,END)
        pwdupdate.delete(0,END)
        cfupdate.delete(0,END)
        backtologin()
        
def backtologin() :
    top2.grid_forget()
    welcome.grid_forget()
    register.grid_forget()
    update.grid_forget()
    left.grid_forget()
    right.grid_forget()
    userentry.delete(0,END)
    pwdentry.delete(0,END)
    userentry.focus_force()
    top.grid(row=0,sticky='news')
    center.grid(row=1,sticky='news')


#main
#call connection function
conn,cursor = connection()
master = mainwindow()
img1 = PhotoImage(file="images/login2.png")
img2 = PhotoImage(file="images/profile.png").subsample(2,2)
icon1 = PhotoImage(file="images/icon1.png")
top = Frame(master,bg='#493628')
top2 = Frame(master,bg='#493628')
center = Frame(master,bg='#D6C0B3')
welcome = Frame(master,bg='#D6C0B3')
register = Frame(master,bg='#D6C0B3')
update = Frame(master,bg='#D6C0B3')
left = Frame(update,bg='#F5EFE7')
right = Frame(update,bg='#D8C4B6')
userinfo = StringVar()
pwdinfo = StringVar()
cfinfo = StringVar()
nameinfo = StringVar()
layout()
loginwindow()
master.mainloop()
cursor.close()
conn.close()
# End of w9_act1.py