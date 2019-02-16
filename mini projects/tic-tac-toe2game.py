'''tic-tac-toe game '''#we have to set invalid attempt in this program
from numpy import *
arr=array([['a','b','c'],['d','e','f'],['g','h','i']])
flag=0
##################################################################
for i in arr:
    print(i,end="  ")
    print()
##################################################################
for l in range(9):
    if l%2==0:
        print("first player's chance")
    else:
        print("second player's chance")
  ###################################################################
    y=input("enter your move\n")
##################################################################
    for i in range(3):
        for j in range(3):

            if y==arr[i][j]:
                if l % 2 == 0:
                    arr[i][j]='X'
                    #break
                else:
                    arr[i][j]='0'
                    #break #why did i write break here

   #################################################################
    if arr[0][0] == arr[0][1] and  arr[0][0] == arr[0][2]:
        flag=1
        print("*****************")

    elif arr[1][0] == arr[1][1] and  arr[1][0] == arr[1][2]:
        flag=1
        print("*****************")

    elif arr[2][0] == arr[2][1] and  arr[2][0] == arr[2][2]:
        flag=1
        print("*****************")

    elif arr[0][0] == arr[1][0] and  arr[0][0] == arr[2][0]:
        flag = 1
        print("*****************")

    elif arr[0][0] == arr[1][1] and  arr[0][0] == arr[2][2]:
        flag = 1
        print("*****************")

    elif arr[0][2] == arr[1][1] and  arr[1][1] == arr[2][0]:
        flag = 1
        print("*****************")

    elif arr[0][1] == arr[1][1] and  arr[0][1] == arr[2][1]:
        flag=1
        print("*****************")

    elif arr[0][2] == arr[1][2] and  arr[0][2] == arr[2][2]:
        flag=1
        print("*****************")


################################################################
    print(arr)

    if flag==1:
        if l%2==0:
            print("*****first player is winner*****")
        else:
            print("*****second player is winner*****")
        print("**game over**")
        break
    elif l>=8:
        print("###****Game is draw****###")









