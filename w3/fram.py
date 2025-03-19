from tkinter import *
master = Tk()

master.wm_geometry("1000x700+300+100")
master.grid_rowconfigure(1,weight=3)
master.grid_rowconfigure((0,2), weight=1)
master.grid_columnconfigure(0,weight=2)
master.grid_columnconfigure(1,weight=1)

top= Frame(master,bg='#B1C29E')
top.grid(row=0, columnspan=2, sticky='news')
left = Frame(master,bg='#FADA7A')
left.grid(row=1, column=0, sticky='news')
rigt = Frame(master,bg='#F0A04B')
rigt.grid(row=1, column=1, sticky='news')
bottom = Frame(master,bg='#B1C29E')
bottom.grid(row=2, columnspan=2, sticky='news')

master.mainloop()