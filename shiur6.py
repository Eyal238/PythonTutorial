# 1.  כתוב פונקציה הקולטת מהמקלדת 7 ציונים של תלמיד, הציונים צריכים להיות בין 0 ל100.  
#     הפונקציה תבצע בדיקת קלט. כלומר-במידה ונתון אינו תקין התוכנית תבקש שוב את הכנסת הציון. בגמר הכנסת הנתונים הפונקציה תדפיס את ממוצע הציונים
def f1():
    x=0
    sum=0
    while x<7:
      print("Enter your grade",x+1,":")
      grade=int(input())
      if (grade>-1)and(grade<101):
         x=x+1
         sum=sum+grade
    ave=round(sum/7,3)
    print("The average is:",ave)

# 2. כתוב פונקציה הקולטת 5 ציונים בין 0 ל- 100 מהמקלדת, על הפונקציה לבדוק תקינות קלט ולהדפיס את הציון המקסימלי והמינימלי מתוך הציונים שנקלטו.
def f2():
    i=0
    min=100
    max=0
    while i<5:
       x=int(input("Enter your score:"))
       if (x>=0)and(x<=100):
           if x<min:
               min=x
           if x>max:
               max=x
           i=i+1
       else:
           print("Sorry.is not a score. ")
    print("The max grade is:",max)
    print("The min grade is:",min)
    
# 3.  במבחן מחשבים נבחנו חמישה תלמידים, כתוב פונקציה הקולטת את שמם של התלמידים ואת הציונים שלהם. 
# הפונקציה תדפיס את:  א)שם התלמיד בעל הציון הגבוה ביותר.   ב) מספר התלמידים שעברו את הציון 60
def f3():
    i=0
    maxGrade=0
    count=0
    while i<5:
        print("Enter name",i+1,":")
        name=input()
        print("Enter grade",i+1,":")
        grade=int(input())
        if(grade>=0)and(grade<=100):
            if (grade>maxGrade):
                maxGrade=grade
                maxName=name
            if grade>59:
                count=count+1
            i=i+1
    print("The name with the highest score is:",maxName)
    print("The number of students with a score higher than 60 is:",count)
#  כתוב פונקציה המקבלת 2 מספרים, הפונקציה תחזיר את המכפלה שלהם אך ללא שימוש בפעולת הכפל.
def f4(x,y):
    z=0
    while x>0:
        z=z+y
        x=x-1
    return z

