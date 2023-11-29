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
#4.
def f4a(list1):
    max1=0
    max2=0
    for i in range(10):
      if (list1[i]>max2):
          max2=list1[i]
      if(max2>max1):
          temp=max2
          max2=max1
          max1=temp
    print("max1=",max1, "max2=",max2)
#4.
def f4b(list1):
    max1=(max(list1))
    list1.remove(max1)
    max2=max(list1)
    print("max1=",max1,"max2=",max2)
