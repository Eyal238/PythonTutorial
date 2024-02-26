# 1. כתוב פונקציה המקבלת רשימת מספרים, הפונקציה תחזיר תשובה בוליאנית האם הפונקציה סימטרית
def f1(list1):
    count=0
    for i in range(len(list1)//2):
        if(list1[i]!=list1[len(list1)-(i+1)]):
            return False
        else:
           count+=1
    if(count==(len(list1)//2)):
        return True

# 2. כתוב פונקציה המקבלת מספר ומדפיסה את סכום הספרות שלו
def f2(num):
    sum=0
    while(num>0):
        sum=sum+(num%10)
        num=num//10
    print(sum)
# 3. כתוב פונקציה המקבלת מהירות רכב ומספר רישוי של הרכב, הפונקציה קולטת מהמקלדת מהירות מקסימאלית ומחזירה 
# תשובה בוליאנית האם לשלוח קנס לבעל הרכב בהתחשב בתנאים הבאים
# אם הרכב נסע במהירות גדולה ב-20 קמש מהמהירות המותרת אך אם מספר הרישוי של הרכב מסתיים ב-7 מותר לרכב לחרוג עד 30
def f3(speedCar,idCar):
    speedMax=int(input("Enter the speed max:"))
    if((speedCar>(speedMax+20))and(idCar%10!=7)):
        return True
    elif((speedCar>(speedMax+30))and(idCar%10==7)):
        return True
    else:
        return False


