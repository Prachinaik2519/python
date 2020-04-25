from tkinter import*
import os
import matplotlib.pyplot as plt
from PIL import ImageTk,Image

import sqlite3
import pandas as pd



def blood_bank():
    df = pd.read_excel (r'C:\\Users\\hp\\Desktop\\excel12.xlsx')
    print (df)
def blood_bank_contact_info():
    df1 = pd.read_excel (r'C:\\Users\\hp\\Desktop\\excel.xlsx')
    print (df1)
def screen_4():
    values = [60, 80, 90, 55, 10, 30 ,25 ,15 ]
    colors = ['b', 'g', 'r', 'c', 'm', 'y' , 'blue','blue']
    labels = ['A+', 'B+', 'AB+', 'o+', 'o-', 'AB-','A-','B-',]
    explode = (0.2, 0, 0, 0, 0, 0,0 ,0)
    plt.pie(values, colors=colors, labels=labels,
    explode=explode, autopct='%1.1f%%',
    counterclock=False, shadow=True)
    plt.title('blood availablity Index')
    plt.show()
 
   









def register_user():
    username_info = username.get()
    password_info = password.get()

    file=open(username_info,"W")
    file.write(username_info+"\n")
    file.write(username_info)
    file.close()
    
    username_entry.delete(0,END)
    password_entry.delete(0,END)

    Label(screen1 ,text = "registration successful",fg = "green").pack()


    
    
        
def register():
    screen1 = Tk()
    screen1.title("register")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry

    username = StringVar()
    password = StringVar()

    Label(screen1,text="please enter details below").pack()
    Label(screen1,text= " ").pack()
    Label(screen1,text="username * ").pack()
    username_entry =Entry(screen1,textvariable=username)
    username_entry.pack() 
    Label(screen1,text= " ").pack()
    Label(screen1,text="password * ").pack()
    password_entry=Entry(screen1,textvariable=password)
    password_entry.pack()
    Label(screen1,text= " ").pack()
    Button(screen1,text = "register",height ="10",width="10").pack()

    
    
    
    



screen5 = Tk()
screen5.geometry('500x500')
screen5.title("Registration Form")


Fullname=StringVar()
Email=StringVar()
var = IntVar()
c=StringVar()
var1= IntVar()



def database():
   name1=Fullname.get()
   email=Email.get()
   gender=var.get()
   location=c.get()
   blood=var1.get()
   conn = sqlite3.connect('Form.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Programming TEXT)')
   cursor.execute('INSERT INTO Student (FullName,Email,Gender,location,blood) VALUES(?,?,?,?,?)',(name1,email,gender,location,blood,))
   conn.commit()



label_0 = Label(screen5, text="Registration form for ",width=20,font=("bold", 20))
label_0.pack()
label_01 = Label(screen5, text="  EMERGENCY!! ",width=20,font=("bold", 20),fg = "red")
label_01.pack()
label_02 = Label(screen5, text="blood requirement",width=20,font=("bold", 20))
label_02.pack()



label_1 = Label(screen5, text="FullName",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(screen5,textvar=Fullname)
entry_1.place(x=240,y=130)

label_2 = Label(screen5, text="Email",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(screen5,textvar=Email)
entry_2.place(x=240,y=180)

label_3 = Label(screen5, text="Gender",width=20,font=("bold", 10))
label_3.place(x=70,y=230)

Radiobutton(screen5, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(screen5, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

label_4 = Label(screen5, text="location",width=20,font=("bold", 10))
label_4.place(x=70,y=280)

list1 = ['mumbai','pune','nagour','Nashik','satara','Sangali'];

droplist=OptionMenu(screen5,c, *list1)
droplist.config(width=15)
c.set('select your location') 
droplist.place(x=240,y=280)

label_4 = Label(screen5, text="blood group",width=20,font=("bold", 10))
label_4.place(x=85,y=330)
var2= IntVar()
Checkbutton(screen5, text="A+", variable=var1).place(x=235,y=330)

Checkbutton(screen5, text="B+", variable=var2).place(x=290,y=330)
Checkbutton(screen5, text="AB+", variable=var2).place(x=335,y=330)
Checkbutton(screen5, text="O+", variable=var2).place(x=390,y=330)
Checkbutton(screen5, text="B-", variable=var2).place(x=435,y=330)
Checkbutton(screen5, text="-AB+", variable=var2).place(x=490,y=330)
Checkbutton(screen5, text="B-", variable=var2).place(x=535,y=330)
Checkbutton(screen5, text="A-", variable=var2).place(x=590,y=330)

Button(screen5, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=380)

    

    

    
    

def first_screen():
    screen = Tk()
    screen.geometry("300x500")
    screen.title("blood donor")
    Label(screen ,text = "welcomet to blood donor system!!!",bg="grey",font = ("calibri",13)).pack()
    Label(screen,text= "").pack()
    

    Button(screen ,text = "register as new user for blood donation",height ="5",width="35",command=register).pack()
    Label(screen ,text= "").pack()
    Button(screen,text = "BLOOD availability",height ="5",width="20", command = screen_4).pack()
    Label(screen,text= "").pack()

    Button(screen,text = "Nearby blood bank",height ="5",width="20",command=blood_bank).pack()
    Label(screen,text= "").pack()
    Button(screen,text = "blood bank contact info",height ="5",width="20",command=blood_bank_contact_info).pack()
    
    screen.mainloop()
    

first_screen()
    
