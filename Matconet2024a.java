# 
def f1():
    x1=random.randrange(0,11)
    y1=random.randint(0,10)
    x2=random.randint(0,10)
    y2=random.randint(0,10)
    dis=math.sqrt(((x1-x2)**2)+((y1-y2)**2))
    print(round(dis,3))
    x3 = int(input("Enter x3:"))
    y3 = int(input("Enter y3:"))
    while((x3>=-10)and(x3<=0)and(y3>=-10)and(y3<=0)):
            break
    else:
            x3 = int(input("Enter x3:"))
            y3 = int(input("Enter y3:"))
#    
def f2(list1):
    for i in range(10):
        num=random.randint(0,100)
        list1.append(num)
    print(list1)
    list1.sort()
    list1.reverse()
    print(list1)    
