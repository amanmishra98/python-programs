from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("tic-tac-toe")
root.geometry("355x500")
root.wm_minsize(width=70,height=100)
#root.maxsize(width=100,height=100)
####################################################
count1=0
flag1=0
flag=0
def click1():
    global flag
    global flag1
    if flag==0 and l1["text"]=="":
        l1.configure(text="X",bg="yellow")
        flag = 1
        flag1=flag1+1
        #print(flag1)
    elif flag==1 and l1["text"]=="":
        l1.configure(text="0",bg="cyan")
        flag=0
        flag1=flag1+1
        #print(flag1)
    winX()
    win0()
def click2():
    global flag
    global flag1
    if flag==0 and l2["text"]=="":
        l2.configure(text="X",bg="yellow")
        flag=1
        flag1=flag1+1
        #print(flag1)
    elif flag==1 and l2["text"]=="":
        l2.configure(text="0",bg="cyan")
        flag=0
        flag1=flag1+1
        #print(flag1)
    winX()
    win0()
def click3():
    global flag
    global flag1
    if flag==0 and l3["text"]=="":
        l3.configure(text="X",bg="yellow")
        flag=1
        flag1 = flag1 + 1
        #print(flag1)
    elif flag==1 and l3["text"]=="":
        l3.configure(text="0",bg="cyan")
        flag=0
        flag1 = flag1 + 1
        #print(flag1)
    winX()
    win0()
def click4():
    global flag
    global flag1
    if flag==0 and l4["text"]=="":
        l4.configure(text="X",bg="yellow")
        flag=1
        flag1 = flag1 + 1
        #print(flag1)
    elif flag==1 and l4["text"]=="":
        l4.configure(text="0",bg="cyan")
        flag=0
        flag1 = flag1 + 1
        #print(flag1)
    winX()
    win0()
def click5():
    global flag
    global flag1
    if flag==0 and l5["text"]=="":
        l5.configure(text="X",bg="yellow")
        flag=1
        flag1 = flag1 + 1
        #print(flag1)
    elif flag==1 and l5["text"]=="":
        l5.configure(text="0",bg="cyan")
        flag=0
        flag1 = flag1 + 1
        #print(flag1)
    winX()
    win0()
def click6():
    global flag
    global flag1
    if flag==0 and l6["text"]=="":
        l6.configure(text="X",bg="yellow")
        flag=1
        flag1 = flag1 + 1
        #print(flag1)
    elif flag==1 and l6["text"]=="":
        l6.configure(text="0",bg="cyan")
        flag=0
        flag1 = flag1 + 1
        #print(flag1)
    winX()
    win0()
def click7():
    global flag
    global flag1
    if flag==0 and l7["text"]=="":
        l7.configure(text="X",bg="yellow")
        flag=1
        flag1 = flag1 + 1
        #print(flag1)
    elif flag==1 and l7["text"]=="":
        l7.configure(text="0",bg="cyan")
        flag=0
        flag1 = flag1 + 1
        #print(flag1)
    winX()
    win0()
def click8():
    global flag
    global flag1
    if flag==0 and l8["text"]=="":
        l8.configure(text="X",bg="yellow")
        flag=1
        flag1 = flag1 + 1
        #print(flag1)
    elif flag==1 and l8["text"]=="":
        l8.configure(text="0",bg="cyan")
        flag=0
        flag1 = flag1 + 1
        #print(flag1)
    winX()
    win0()
def click9():
    global flag
    global flag1
    if flag==0 and l9["text"]=="":
        l9.configure(text="X",bg="yellow")
        flag=1
        flag1 = flag1 + 1
        #print(flag1)
    elif flag==1 and l9["text"]=="":
        l9.configure(text="0",bg="cyan")
        flag=0
        flag1 = flag1 + 1
        #print(flag1)
    winX()
    win0()
    #tie()
########################################################################
def winX():
    global flag1
    if l1["text"]=="X" and l2["text"]=="X" and l3["text"]=="X":
        messagebox.showinfo("congrtulation", "1st player is winner")
        quit()
    elif l4["text"]=="X" and l5["text"]=="X" and l6["text"]=="X":
        messagebox.showinfo("congrtulation", "1st player is winner")
        quit()
    elif l7["text"]=="X" and l8["text"]=="X" and l9["text"]=="X":
        messagebox.showinfo("congrtulation", "1st player is winner")
        quit()
    elif l1["text"]=="X" and l4["text"]=="X" and l7["text"]=="X":
        messagebox.showinfo("congrtulation", "1st player is winner")
        quit()
    elif l2["text"]=="X" and l5["text"]=="X" and l8["text"]=="X":
        messagebox.showinfo("congrtulation", "1st player is winner")
        quit()
    elif l3["text"]=="X" and l6["text"]=="X" and l9["text"]=="X":
        messagebox.showinfo("congrtulation", "1st player is winner")
        quit()
    elif l1["text"]=="X" and l5["text"]=="X" and l9["text"]=="X":
        messagebox.showinfo("congrtulation", "1st player is winner")
        quit()
    elif l3["text"]=="X" and l5["text"]=="X" and l7["text"]=="X":
        messagebox.showinfo("congrtulation", "1st player is winner")
        quit()
    else:
        if flag1==9:
            messagebox.showinfo("oops", "game is tie")

####################################################################
def win0():
    if l1["text"]=="0" and l2["text"]=="0" and l3["text"]=="0":
        messagebox.showinfo("congrtulation", "2nd player is winner")
        quit()
    elif l4["text"]=="0" and l5["text"]=="0" and l6["text"]=="0":
        messagebox.showinfo("congrtulation", "2nd player is winner")
        quit()
    elif l7["text"]=="0" and l8["text"]=="0" and l9["text"]=="0":
        messagebox.showinfo("congrtulation", "2nd player is winner")
        quit()
    elif l1["text"]=="0" and l4["text"]=="0" and l7["text"]=="0":
        messagebox.showinfo("congrtulation", "2nd player is winner")
        quit()
    elif l2["text"]=="0" and l5["text"]=="0" and l8["text"]=="0":
        messagebox.showinfo("congrtulation", "2nd player is winner")
        quit()
    elif l3["text"]=="0" and l6["text"]=="0" and l9["text"]=="0":
        messagebox.showinfo("congrtulation", "2nd player is winner")
        quit()
    elif l1["text"]=="0" and l5["text"]=="0" and l9["text"]=="0":
        messagebox.showinfo("congrtulation", "2nd player is winner")
        quit()
    elif l3["text"]=="0" and l5["text"]=="0" and l7["text"]=="0":
        messagebox.showinfo("congrtulation", "2nd player is winner")
        quit()
 #####################################################################
def exit():
    quit()

 ############################################################333####33
l1=Button(master=root,command=click1)
l2=Button(master=root,command=click2)
l3=Button(master=root,command=click3)
l4=Button(master=root,command=click4)
l5=Button(master=root,command=click5)
l6=Button(master=root,command=click6)
l7=Button(master=root,command=click7)
l8=Button(master=root,command=click8)
l9=Button(master=root,command=click9)
label1=Label(master=root,text="1st player is X",bg="black",fg="white")
label2=Label(master=root,text="2nd player is 0",bg="black",fg="white")
b1=Button(master=root,text="exit",bg="red",command=exit)
##########################################

#########################################
l1.config(width=6,height=2)
l2.config(width=6,height=2)
l3.config(width=6,height=2)
l4.config(width=6,height=2)
l5.config(width=6,height=2)
l6.config(width=6,height=2)
l7.config(width=6,height=2)
l8.config(width=6,height=2)
l9.config(width=6,height=2)
b1.config(width=6,height=1)

#########################################
l1.grid(ipady=30,ipadx=30,row=0,column=0)
l2.grid(ipady=30,ipadx=30,row=0,column=1)
l3.grid(ipady=30,ipadx=30,row=0,column=2)
l4.grid(ipady=30,ipadx=30,row=1,column=0)
l5.grid(ipady=30,ipadx=30,row=1,column=1)
l6.grid(ipady=30,ipadx=30,row=1,column=2)
l7.grid(ipady=30,ipadx=30,row=2,column=0)
l8.grid(ipady=30,ipadx=30,row=2,column=1)
l9.grid(ipady=30,ipadx=30,row=2,column=2)
label1.place(x=0,y=350,width=500,height=60)
label2.place(x=0,y=400,width=500,height=60)
b1.place(x=130,y=460)
#########################################

root.mainloop()
