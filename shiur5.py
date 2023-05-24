# 1. כתוב פונקציה הקולטת מהמקלדת מספר ומדפיסה האם הוא חיובי או שלילי
def f1():
  num=int(input("Enter your number:"))
  if num>0:
    print("Possitive")
  else:
    print("Negative")
# 2. 
def f2(x,y,z):
  if (x<y)and(x<z):
    return x
  elif (y<x)and(y<z):
    return y
  else:
    return z
print(f2(5,3,4))
#   כתוב מחשבון
print("1 - Add +")
print("2 - Subtract - ")
print("3 - Multiplication *")
print("4 - division /")
print("5 - Remainder of the division(modulo) %")
print("6 - Division without remainder //")
print("7 - Power **")
