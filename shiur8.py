#  1.
str1=["aba","saba","adir","david","moran"]
def f1(str1):
  sum=0;
  for i in str1:
    for j in i:
      if j=="a":
        sum=sum+1
  print(sum)

# 2.
def f2():
    sum=0
    num = random.randrange(100, 1000)
    print(num)
    while(num>0):
        sum=(num%10)+sum
        num=num//10
    print(sum)

# 3.
def f3():
    multiplication=1
    num = random.randrange(100, 1000)
    print(num)
    while(num>0):
        multiplication=(num%10)*multiplication
        num=num//10
    print(multiplication)
# 4.
def f4(list2):
    print(list2)
    for i in range(len(list2)):
        if list2[i]>0:
           list2[i]=1
        else:
           list2[i]=-1
    print(list2)
# 5.
def f5():
    list1=[]
    list2=[]
    for i in range(10):
        num=int(input("Enter num:"))
        if num%2==0:
            list1.append(num)
        else:
            list2.append(num)
    print(list1)
    print(list2)


#7. כתוב פונקציה המקבלת איבר ראשון של סדרה חשבונית ואת הפרש הסדרה. הפונקציה תדפיס את 10 האיברים של הסדרה.
def f3(a1,diff):
    for i in range(1,11):
        print(a1+(diff*(i-1)),end=" ")
# 9.
def f9(height):
    for i in range(height):
        for j in range(i+1):
            print("*",end=" ")
        print()
