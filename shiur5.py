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
# 5.  לכבוד החגים החליטו בכביש אגרה-"שש" לתת הנחה של 5 אחוז בתשלום נסיעה עבור מספרי רכב שמסתיימים ב- 5 או ב-0, בכביש 6 ישנם 8 קטעי כביש, כך שכול קטע עולה לרכב פרטי 10 שקלים 
#  במידה והרכב נסע ביום אחד מעל 4(כולל) קטעי כביש ניתנת הנחה קבועה של 5 אחוז ומעל 6(כולל) קטעי כביש הנחה של 7 אחוז. כתוב פונקציה המקבלת מספר רכב ומספר קטעי כביש ומחזירה את סכום התשלום הנדרש 
def f5(carNum,roadsNum):
    if (carNum%10==0)or(carNum%10==5):
        if roadsNum<=3:
            result=(10*roadsNum)
        elif roadsNum==4 or roadsNum==5:
            result=(10*roadsNum-(10*roadsNum*5/100))
        elif roadsNum>=6 and roadsNum<=8:
            result=(10*roadsNum-(10*roadsNum*7/100))
        return (result-(result*5/100))
    else:
        if roadsNum<=3:
            return (10*roadsNum)
        elif roadsNum==4 or roadsNum==5:
            return (10*roadsNum-(10*roadsNum*5/100))
        elif roadsNum>=6 and roadsNum<=8:
            return (10*roadsNum-(10*roadsNum*7/100))
    
