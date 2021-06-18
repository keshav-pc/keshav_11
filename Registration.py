import pymysql
from tkinter import *
r=Tk()
def submit():
 str1=fname.get()       #first name          
 str3=email.get()       # Email
 str4=username.get()    # username
 str5=password.get()    # password
 str6=phone.get()       # Cell no.
 str7=address.get()     # address 
  ###################### SQL ############################################
 print(str1,"\n",str3,"\n",str4,"\n",str5,"\n",str6,"\n",str7)
 db=pymysql.connect("localhost","root","root","register")               # Db login details 
 cursor=db.cursor()
 sql= "insert into data(fname,email,username,password,phone,address)"   # Db query 
 values('"+str1+"','"+str3+"','"+str4+"','"+str5+"','"+str6+"','"+str7+"')
 cursor.execute(sql)
 print("successfully data inserted")
 db.commit()
 db.close()
                ######################### Table #####################################
r.title("Registration page")    
l1=Label(r,text="Register Here",font=( 'times new roman',28,"bold"),bg="Black",fg="yellow",)
l1.grid(row=1,column=1,columnspan="4")

fname=StringVar()
l1=Label(r,text="Full Name: ",font="san-serif")
l1.grid(row=7, column=2)
e1=Entry(r,textvariable=fname)
e1.grid(row=7, column=3)

email=StringVar()
l3=Label(r,text="Email: ",font="san-serif")
l3.grid(row="9",column="2")
e3=Entry(r,textvariable=email)
e3.grid(row="9",column="3")

username=StringVar()
l1=Label(r,text="Username: ",font="san-serif")
l1.grid(row="10",column="2")
e1=Entry(r,textvariable=username)
e1.grid(row="10",column="3")

password=StringVar()
l2=Label(r,text="Password: ",font="san-serif")
l2.grid(row="11",column="2")
e2=Entry(r,textvariable=password)
e2.grid(row="11",column="3")

phone=StringVar()
l5=Label(r,text="Phone Number: ",font="san-serif")
l5.grid(row="12",column="2")
e5=Entry(r,textvariable=phone)
e5.grid(row="12",column="3")

address=StringVar()
l4=Label(r,text="Address: ",font="san-serif")
l4.grid(row="13",column="2")
e4=Entry(r,textvariable=address)
e4.grid(row="13",column="3")

c1=Checkbutton(r,text="I accept all the terms and conditions.")
c1.grid(row="15",column=1,columnspan="4")

b=Button(r,text="Submit", command=submit,bg="green",fg="white",font="san-serif")
b.grid(row="16",column=1,columnspan="4")
r.mainloop()
