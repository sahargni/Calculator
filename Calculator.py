
#Sahar-Ganjkhani #calculator

from tkinter import *

root=Tk()
equation=StringVar()
root.title("my calculator")
root.configure(background="lightblue")
h=Label(root,textvariable=equation,font=("Tohoma",30,"bold"),pady=10)
h.grid(columnspan=4)
h.bind("")

def set_number(num):
    equation.set(equation.get()+num)
    
def calcilate_equation():
    equation.set(eval(equation.get()))

def back():
    last_nembers=equation.get()[:-1]
    equation.set(last_nembers)
    

    
btn1=Button(root,text="1",bg="lightblue",fg="magenta",width=5,height=2,relief=RIDGE ,font=("Tohoma",30,"bold"),command=lambda:set_number("1"))
btn1.grid(row=1,column=0)

btn2=Button(root,text="2",bg="lightblue",fg="magenta",width=5,height=2,relief=RIDGE,font=("Tohoma",30,"bold"),command=lambda:set_number("2"))
btn2.grid(row=1,column=1)

btn3=Button(root,text="3",bg="lightblue",fg="magenta",width=5,height=2,relief=RIDGE,font=("Tohoma",30,"bold"),command=lambda:set_number("3"))
btn3.grid(row=1,column=2)

btn4=Button(root,text="4",bg="lightblue",fg="magenta",width=5,height=2,relief=RIDGE,font=("Tohoma",30,"bold"),command=lambda:set_number("4"))
btn4.grid(row=2,column=0)

btn5=Button(root,text="5",bg="lightblue",fg="magenta",width=5,height=2,relief=RIDGE,font=("Tohoma",30,"bold"),command=lambda:set_number("5"))
btn5.grid(row=2,column=1)

btn6=Button(root,text="6",bg="lightblue",fg="magenta",width=5,height=2,relief=RIDGE,font=("Tohoma",30,"bold"),command=lambda:set_number("6"))
btn6.grid(row=2,column=2)

btn7=Button(root,text="7",bg="lightblue",fg="magenta",width=5,height=2,relief=RIDGE,font=("Tohoma",30,"bold"),command=lambda:set_number("7"))
btn7.grid(row=3,column=0)

btn8=Button(root,text="8",bg="lightblue",fg="magenta",width=5,height=2,relief=RIDGE,font=("Tohoma",30,"bold"),command=lambda:set_number("8"))
btn8.grid(row=3,column=1)

btn9=Button(root,text="9",bg="lightblue",fg="magenta",width=5,height=2,relief=RIDGE,font=("Tohoma",30,"bold"),command=lambda:set_number("9"))
btn9.grid(row=3,column=2)

btn0=Button(root,text="0",bg="lightblue",fg="magenta",width=5,height=2,relief=RIDGE,font=("Tohoma",30,"bold"),command=lambda:set_number("0"))
btn0.grid(row=4,column=1)

btnclear=Button(root,text="c",bg="lightblue",fg="magenta",width=5,height=2,relief=RIDGE,font=("Tohoma",30,"bold"),command=lambda:equation.set(""))
btnclear.grid(row=4,column=0)

btnequal=Button(root,text="=",bg="lightblue",fg="magenta",width=5,height=2,relief=RIDGE,font=("Tohoma",30,"bold"),command=calcilate_equation)
btnequal.grid(row=4,column=2)

btnplus=Button(root,text="+",bg="lightblue",fg="magenta",width=5,height=2,relief=RIDGE,font=("Tohoma",30,"bold"),command=lambda:set_number("+"))
btnplus.grid(row=1,column=3)

btnmul=Button(root,text="*",bg="lightblue",fg="magenta",width=5,height=2,relief=RIDGE,font=("Tohoma",30,"bold"),command=lambda:set_number("*"))
btnmul.grid(row=2,column=3)

btntafriq=Button(root,text="-",bg="lightblue",fg="magenta",width=5,height=2,relief=RIDGE,font=("Tohoma",30,"bold"),command=lambda:set_number("-"))
btntafriq.grid(row=3,column=3)

btntaqsim=Button(root,text="/",bg="lightblue",fg="magenta",width=5,height=2,relief=RIDGE,font=("Tohoma",30,"bold"),command=lambda:set_number("/"))
btntaqsim.grid(row=4,column=3)

btnbackspace=Button(root,text="b",bg="lightblue",fg="magenta",width=5,height=2,relief=RIDGE,font=("Tohoma",30,"bold"),command=back)
btnbackspace.grid(row=0,column=3)

mainloop()