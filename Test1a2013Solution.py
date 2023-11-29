import math


#1.
def f1(r):
    S=math.pi*r**2
    P=2*math.pi*r
    print(round(S,3))
    print(round(P,3))
#2.
def f2():
    count=0
    num=int(input("Enter your number:"))
    if(num%2==0):
        print("even.")
    else:
        print("odd.")
    while(num>0):
        count+=1
        num=num//10
    print(count)
    
