from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk() # นี้คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #นี้คือชื้อโปรแกรม
GUI.geometry('500x400') #นี้คือขนาดของโปรแกรม


la01=Label(GUI,text='ข้อมูลการเงิน',bg="yellow",font=('Angsana New',30),fg='red')
la01.place(x=175,y=50)

frame=Frame(GUI,bd="5",r=GROOVE ,padx=10,pady=10)
frame.pack(pady=120,ipadx=10)

def GG():
    name='สมชาย'
    no='123-43451-2345'
    messagebox.showinfo('เลขที่บัญชี','ชื่อ {} ''เลขบัญชี {}'.format(name,no))
    
B1 = Button(frame,text='เลขที่บัญชี',command=GG)
B1.pack(ipadx=10,ipady=10,side=RIGHT) 

def GG2():
    money=3000000
    messagebox.showinfo('จำนวนเงิน',f'{money:,.2f} บาท')
    
FB1 =Frame(GUI) 
FB1.place(x=10,y=300)
B2 = ttk.Button(frame,text='เงินเดือน',command=GG2)
B2.pack(ipadx=10,ipady=10,side=LEFT )


GUI.mainloop()
