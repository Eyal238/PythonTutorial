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


