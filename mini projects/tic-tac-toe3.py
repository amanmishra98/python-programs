'''tic-tac-toe player vs computer'''
#to understand this game we can remove hash comments like print(l1)
from numpy import *
from random import *
arr=array([['a','b','c'],['d','e','f'],['g','h','i']])
flag=0
for i in arr:
    print(i)
l1=['a','b','c','d','e','f','g','h','i']
##################################################################################
for l in range(9):
    if l%2==0:
        print("1st player's chance\n")
        y1=input("enter your choise\n")
        l1.remove(y1)
        #print(l1)
        for i in range(3):
            for j in range(3):
                if y1==arr[i][j]:
                    arr[i][j]='X'

    else:
        print("computer's chance\n")
        y2=choice(l1)
        l1.remove(y2)
        #print(l1)
        for i in range(3):
            for j in range(3):
                if y2==arr[i][j]:
                    arr[i][j]='0'

######################################################################################
    #conditions of winning
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



#####################################################################################
        ################################################################
    print(arr)

    if flag == 1:
        if l % 2 == 0:
            print("*****first player is winner*****")
        else:
            print("*****computer is winner*****")
        print("**game over**")
        break
    elif l >= 8:
        print("###****Game is draw****###")