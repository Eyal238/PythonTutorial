# 1. כתוב פונקציה הקולטת מהמקלדת מספר ומדפיסה האם הוא חיובי או שלילי
def f1():
  num=int(input("Enter your number:"))
  if num>0:
    print("Possitive")
  else:
    print("Negative")
# 2. כתוב פונקציה המקבלת 3 מספרים ומחזירה את המספר הקטן מביניהם
def f2(x,y,z):
  if (x<y)and(x<z):
    return x
  elif (y<x)and(y<z):
    return y
  else:
    return z
print(f2(5,3,4))
# 3.  כתוב פונקציה לביצוע פעולת חישוב בין שני מספרים, עבור כל פעולות החשבון שנמצאות בטבלה בשקף השני של מצגת 3. הפונקציה מקבלת מספר, סוג הפעולה ועוד מספר. ומחזירה את התוצאה בהתאם לחישוב 
def f4(x,operation,y):
   if operation=="+":
       return x+y
   elif operation=="-":
       return x-y
   elif operation=="*":
       return x * y
   elif operation=="/":
       return x / y
   elif operation=="//":
       return x//y
   elif operation == "%":
       return x%y
   elif operation=="**":
       return x**y
# 4.  בחנות גלידות ניתן לקנות קרטיב בשקל ועשרים אגורות. מחיר עשרה קרטיבים הוא 10 שקלים. וקרטון של 54 קרטיבים ניתן לקנות ב-50 שקלים. כך גם אם נקנו מעל 50 אך פחות מ-54. 
#    לא ניתן לקנות מעל 108 קרטיבים בקנייה אחת. כלומר עד 2 קרטונים. כתוב פונקציה המקבלת את מספר הקרטיבים שנקנו ומדפיסה את המחיר 
def f4(amount):
  if amount==1:
    print(1.2)
  elif (amount>1)and(amount<10):
    print(amount*1.2)
  elif amount==10:
    print(10)
  elif (amount>10)and(amount<50):
    complete=amount//10
    remainder=amount%10
    print((complete*10)+(remainder*1.2))
  elif (amount>=50)and(amount<55):
    print(50)
  elif (amount>54)and(amount<108):
    complete=(amount-54)//10
    remainder=(amount-54)%10
    print(50+(complete*10)+(remainder*1.2))
  elif amount==108:
    print(100)
