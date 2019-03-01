a=[]
c=int(input())
for i in range(1,c+1):
    n1=input()
    n2=input()
    a.append(n)
for i in range(1,a+1):
    x=input()
    y=input()
for i in range(1,a+1):
    try:
        b=int(x)/int(y)
        print(b)
    except ZeroDivisionError as e:
        print("Error code:",e)
    except ValueError as e:
        print("Error code:",e)
