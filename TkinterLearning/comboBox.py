from tkinter.ttk import *
from tkinter import *

#(Combobox) 实质上是带文本框的上拉列表框
#组合框控件常用方法有：获得所选中的选项值get()和获得所选中的选项索引current()

def calc(event):
       a = float(t1.get())
       b = float(t2.get())
       dic = {0:a+b,1:a-b,2:a*b,3:a/b}
       c = dic[comb.current()]
       lbl.config(text=str(c))

root = Tk()
root.title('四则运算')
root.geometry('320x240')

t1 = Entry(root)
t1.place(relx=0.1,rely=0.1,relwidth=0.2,relheight=0.1)

t2 = Entry(root)
t2.place(relx=0.5,rely=0.1,relwidth=0.2,relheight=0.1)

var = StringVar()

comb = Combobox(root,textvariable=var,values=['加','减','乘','除',])
comb.place(relx=0.1,rely=0.5,relwidth=0.2)
comb.bind('<<ComboboxSelected>>',calc)

lbl=Label(root,text='结果')
lbl.place(relx=0.5,rely=0.7,relwidth=0.2,relheight=0.3)

root.mainloop()
