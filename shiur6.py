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
