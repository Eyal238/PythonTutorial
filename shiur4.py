# 1.     כתוב פונקציה הקולטת מהמקלדת את שם התלמיד ומדפיסה את המילה שלום ולאחר מכן את שם התלמיד
def f1():
    name=input("Enter name student:")
    print("Hello",name)
# 2.  כתוב פונקציה המקבלת מספר שלם, הפונקציה תדפיס את מספר השלמים המתקבלים בחלוקה ב-5.
def f2(num):
    print(num//5) 
# 3. כתוב פונקציה המקבלת 2 מספרים, הפונקציה תחשב ותחזיר את סכומם
def f3(x,y):
    return x+y
print(f3(4,6))   #  output 10
# 4. כתוב פונקציה המקבלת 3 מספרים, הפונקציה תדפיס את סכומם ותחזיר את הממוצע שלהם.
def f4(x,y,z):
    sum=x+y+z
    print(sum)
    return (sum/3)
print(round(f4(50,65,70),3))

# 5. כתוב פונקציה המקבלת רדיוס של מעגל, הפונקציה תדפיס את היקף ושטח המעגל
import math
def circle1(r):
  pie=math.pi
  P=pie*2*r
  S=pie*r*r
  print("scope = ",P)
  print("area = ",S)