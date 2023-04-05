from tkinter import*
from turtle import bgcolor

def click(event):
    global scvalue
    text=event.widget.cget("text")
    #print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(screen.get())
            scvalue.set(value)
            screen.update()
    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()



root=Tk()
root.geometry("300x250")
root.title("CALCULATOR")
root.configure(background="white")
top=Frame(root,bg='black',width=250,height=150,bd=5,relief=RIDGE)
top.grid(row=0,column=0)

scvalue=StringVar()
scvalue.set("")

bottom=Frame(root,bg='light green',width=300,height=150,relief=RIDGE)
bottom.grid(row=1,column=0)

screen=Entry(top,font=("arial",20,"bold"),textvar=scvalue,background="powder blue")
screen.grid(row=0,column=0)




#saare button hai idher
button1=Button(bottom,text="C",font=('arial 15 bold'),width=5,height=1,bg='orange')
button1.grid(row=0,column=0,sticky=N+S+E+W)
button1.bind("<Button-1>",click)

button2=Button(bottom,text="/",font=('arial 15 bold'),width=5,height=1,bg='gainsboro')
button2.grid(row=0,column=1,sticky=N+S+E+W)
button2.bind("<Button-1>",click)

button3=Button(bottom,text="*",font=('arial 15 bold'),width=5,height=1,bg='gainsboro')
button3.grid(row=0,column=2,sticky=N+S+E+W)
button3.bind("<Button-1>",click)

button4=Button(bottom,text="-",font=('arial 15 bold'),width=5,height=1,bg='gainsboro')
button4.grid(row=0,column=3,sticky=N+S+E+W)
button4.bind("<Button-1>",click)

button5=Button(bottom,text="7",font=('arial 15 bold'),fg='white',width=5,height=1,bg='black')
button5.grid(row=1,column=0,sticky=N+S+E+W)
button5.bind("<Button-1>",click)

button6=Button(bottom,text="8",font=('arial 15 bold'),fg='white',width=5,height=1,bg='black')
button6.grid(row=1,column=1,sticky=N+S+E+W)
button6.bind("<Button-1>",click)

button7=Button(bottom,text="9",font=('arial 15 bold'),fg='white',width=5,height=1,bg='black')
button7.grid(row=1,column=2,sticky=N+S+E+W)
button7.bind("<Button-1>",click)

button8=Button(bottom,text="+",font=('arial 15 bold'),width=5,height=1,bg='gainsboro')
button8.grid(row=1,column=3,sticky=N+S+E+W)
button8.bind("<Button-1>",click)

button9=Button(bottom,text="4",font=('arial 15 bold'),fg='white',width=5,height=1,bg='black')
button9.grid(row=2,column=0,sticky=N+S+E+W)
button9.bind("<Button-1>",click)

button10=Button(bottom,text="5",font=('arial 15 bold'),fg='white',width=5,height=1,bg='black')
button10.grid(row=2,column=1,sticky=N+S+E+W)
button10.bind("<Button-1>",click)

button11=Button(bottom,text="6",font=('arial 15 bold'),fg='white',width=5,height=1,bg='black')
button11.grid(row=2,column=2,sticky=N+S+E+W)
button11.bind("<Button-1>",click)
button12=Button(bottom,text="=",font=('arial 15 bold'),width=5,height=1,bg='gainsboro')
button12.grid(row=2,column=3,sticky=N+S+E+W)
button12.bind("<Button-1>",click)
button13=Button(bottom,text="1",font=('arial 15 bold'),fg='white',width=5,height=1,bg='black')
button13.grid(row=3,column=0,sticky=N+S+E+W)
button13.bind("<Button-1>",click)
button14=Button(bottom,text="2",font=('arial 15 bold'),fg='white',width=5,height=1,bg='black')
button14.grid(row=3,column=1,sticky=N+S+E+W)
button14.bind("<Button-1>",click)
button15=Button(bottom,text="3",font=('arial 15 bold'),fg='white',width=5,height=1,bg='black')
button15.grid(row=3,column=2,sticky=N+S+E+W)
button15.bind("<Button-1>",click)
button16=Button(bottom,text="0",font=('arial 15 bold'),fg='white',width=5,height=1,bg='black')
button16.grid(row=3,column=3,sticky=N+S+E+W)
button16.bind("<Button-1>",click)
root.mainloop()