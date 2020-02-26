from tkinter import *

root=Tk()
root.title("Simple Calculator")

e=Entry(root,width=45,borderwidth=3)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))
def button_clear( ):
    e.delete(0,END)
def button_add():
    first_number=e.get()
    global f_num
    global math
    math="addition"
    f_num=int(first_number)
    e.delete(0,END)
def button_equal():
    second_number=e.get()
    e.delete(0,END)
    if math=="addition":
        e.insert(0, f_num + int(second_number))
    if math=="substraction":
        e.insert(0, f_num - int(second_number))
    if math=="multiplication":
        e.insert(0, f_num * int(second_number))
    if math=="division":
        e.insert(0, f_num / int(second_number))
    if math=="percentage":
        e.insert(0, f_num % int(second_number))
    if math=="square root":
        e.insert(0, f_num ** int(second_number))


    
def button_substraction():
    first_number=e.get()
    global f_num
    global math
    math="substraction"
    f_num=int(first_number)
    e.delete(0,END)
def button_multiplication():
    first_number=e.get()
    global f_num
    global math
    math="multiplication"
    f_num=int(first_number)
    e.delete(0,END)
def button_division():
    first_number=e.get()
    global f_num
    global math
    math="division"
    f_num=int(first_number)
    e.delete(0,END)
def button_per():
    first_number=e.get()
    global f_num
    global math
    math="percentage"
    f_num=int(first_number)
    e.delete(0,END)
def button_sroot():
    first_number=e.get()
    global f_num
    global math
    math="square root"
    f_num=int(first_number)
    e.delete(0,END)
# Define Buttons
my_Button1=Button(root,text="1",padx=40,pady=20,command=lambda:button_click(1))
my_Button2=Button(root,text="2",padx=40,pady=20,command=lambda:button_click(2))
my_Button3=Button(root,text="3",padx=40,pady=20,command=lambda:button_click(3))
my_Button4=Button(root,text="4",padx=40,pady=20,command=lambda:button_click(4))
my_Button5=Button(root,text="5",padx=40,pady=20,command=lambda:button_click(5))
my_Button6=Button(root,text="6",padx=40,pady=20,command=lambda:button_click(6))
my_Button7=Button(root,text="7",padx=40,pady=20,command=lambda:button_click(7))
my_Button8=Button(root,text="8",padx=40,pady=20,command=lambda:button_click(8))
my_Button9=Button(root,text="9",padx=40,pady=20,command=lambda:button_click(9))
my_Button0=Button(root,text="0",padx=40,pady=20,command=lambda:button_click(0))
my_Buttonadd=Button(root,text="+",padx=40,pady=20,command=button_add)
my_Buttonequal=Button(root,text="=",padx=92,pady=20,command=button_equal)
my_Buttonc=Button(root,text="c",padx=40,pady=20,command=button_clear)
my_Buttonsub=Button(root,text="-",padx=40,pady=20,command=button_substraction)
my_Buttonmul=Button(root,text="*",padx=40,pady=20,command=button_multiplication)
my_Buttondiv=Button(root,text="/",padx=40,pady=20,command=button_division)
my_Buttonper=Button(root,text="%",padx=40,pady=20,command=button_per)
my_Buttonsroot=Button(root,text="**",padx=40,pady=20,command=button_sroot)


#put the buttons on the screen

my_Button1.grid(row=3,column=0)
my_Button2.grid(row=3,column=1)
my_Button3.grid(row=3,column=2)

my_Button4.grid(row=2,column=0)
my_Button5.grid(row=2,column=1)
my_Button6.grid(row=2,column=2)

my_Button7.grid(row=1,column=0)
my_Button8.grid(row=1,column=1)
my_Button9.grid(row=1,column=2)

my_Button0.grid(row=4,column=0)
my_Buttonadd.grid(row=4,column=1)
my_Buttonsub.grid(row=4,column=2)

my_Buttonmul.grid(row=5,column=0)
my_Buttonper.grid(row=5,column=1)
my_Buttonsroot.grid(row=5,column=2)

my_Buttonequal.grid(row=6,column=1,columnspan=2)
my_Buttonc.grid(row=6,column=0)



root.mainloop()