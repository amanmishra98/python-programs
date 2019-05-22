from tkinter import *
from random import *
root=Tk()
root.title("Color Game")
root.geometry("460x400")
###############################################################
#read the high score from file cg1.txt
f1=open("C:\\Users\\Aman Mishra\\Desktop\\cg1 file.txt","r")
f2=f1.readlines()
if len(f2)==0:
    high_score=0
    print("file is empty")
else:
    f1.seek(0,0)
    for i in f1:
         list1=i.split(",")
    print(list1)
    list1.pop()
    list2=[]
    for i in list1:
        c1=int(i)
        list2.append(c1)
    print(list2)
    print("max is:",max(list2))
    high_score=max(list2)
#######################################################   
x=0
l=["red","blue","green","cyan","yellow","orange","black","magenta"]
l2=["Red","Blue","Green","Cyan","Yellow","Orange","Black","White","Gray","Purple","Pink"]
color=""
text1=""
y=0
def update_timeText():
    global high_score
    if (state):
        global timer
        timer[1] -= 1
        if timer[1]==59:
            label2.config(text="high score:%d\tscore:%d\t"%(high_score,x))
        if timer[1]==0:
            
            print(high_score)
        if timer[1] ==0:
            pause()
            e1.config(state='disabled')
            l4.config(text="Game Over")

        timeString = pattern.format(timer[0], timer[1])
        l3.configure(text=timeString)
    root.after(1000, update_timeText)
    root.bind('<Return>', press)
def start(r):
    global color
    color=choice(l)
    global text1
    text1=choice(l2)
    l1.config(text=text1)
    l1.config(fg=color)
    global state
    state = True
    update_timeText()

def pause():
    global state
    state = False
state=False
timer = [0, 60, ]
pattern = 'Time left:{1:02d}'

def press(n):
    l3 = ["Red", "Blue", "Green", "Cyan", "Yellow", "Orange", "Black","White","Gray","Purple","Pink"]
    global color
    global x
    global high_score
    a=e1.get()
    if a==color:
        x=x+1
        label2.config(text="high score:%d\tscore:%d\t"%(high_score,x))
        ###################################################################
        #append score in file cg1.txt
        f1=open("C:\\Users\\Aman Mishra\\Desktop\\cg1 file.txt","a")
        a="0,"
        f1.write(a)
        f1.close()
        f=open("C:\\Users\\Aman Mishra\\Desktop\\cg1 file.txt","a")
        text=str(x)
        f.write(text+",")
        f.close()
        #####################################################################
        
    e1.delete(0,10)
    l1.config(text=choice(l3))
    color=choice(l)
    l1.config(fg=color)
#######################################################################  
label1=Label(master=root,text="Type in the color of words,and not the word text!",font=("Helvetica", 15),justify="left")
label2=Label(master=root,text="Press Enter key to start",font=("Helvetica", 15),justify="left")
l3=Label(root, text="00", font=("Helvetica", 15))
l1=Label(master=root,text="hello",font=("bold",50))
l4=Label(master=root,font=("bold",20),fg="Blue")
e1=Entry(master=root)
e1.focus_set()
###############################################################
label1.config(width=50,height=2)
label2.config(width=50,height=2)
l1.config(width=50,height=2)
l4.config(width=10,height=2)
e1.config(width=50)
#pack
label1.pack()
label2.pack()
l3.pack()
l1.pack()
e1.pack()
l4.pack()


root.bind('<Return>',start)
root.mainloop()
##########################
#end
