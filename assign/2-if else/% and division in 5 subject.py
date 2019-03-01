edc=int(input("enter marks in EDC\n"))
de=int(input("enter marks in DE\n"))
oops=int(input("enter marks in OOPS\n"))
dsa=int(input("enter marks in DSA\n"))
math=int(input("enter marks in Math\n"))
add=edc+de+oops+dsa+math
add<=100
if add<30:
    print("fail")
if add>30:
    per=float((add*100)/100)
    if per>30 and per<45:
        print("percentage is %f"%per)
        print("third devision")
    elif per>45 and per<60:
        print("percentage is %f"%per)
        print("second devision")
    else:
        print("percentage is %f"%per)
        print("first devision")
input()        
