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
#3.
def f3():
    arr1=[]
    for i in range(5):
        num=int(input("Enter number:"))
        arr1.append(num)
        if(arr1[i]>99):
            arr1[i]=1
        elif(arr1[i]<100):
            arr1[i]=0
    print(arr1)
    
