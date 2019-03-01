a=int(input("enter no of month\n"))
if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
    if a==1:
        print("a is jan")
        print("31 days")
    if a==3:
        print("a is mar")
        print("31 days")
    if a==5:
        print("a is may")
        print("31 days")
    if a==7:
        print("a is july")
        print("31 days")
    if a==8:
        print("a is aug")
        print("31 days")
    if a==10:
        print("a is oct")
        print("31 days")
    if a==12:
        print("a is dec")
        print("31 days")

elif a==4 or a==6 or a==9 or a==11:
    if a==4:
        print("a is apr")
        print("30 days")
    if a==6:
        print("a is jun")
        print("30 days")    
    if a==9:
        print("a is sep")
        print("30 days")
    if a==11:
        print("a is nov")
        print("30 days")
else:
    print("a is feb")
    print("28 days")
input()    
        
