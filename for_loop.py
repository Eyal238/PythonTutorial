# 1. כתוב פונקציה הקולטת 4  מספרים מהמקלדת, הפונקציה תחשב את הממוצע שלהם ותדפיס אותו   
def ave():
    sum=0
    for i in range(4):
        x=int(input("Enter your number:"))
        sum=sum+x
    print(sum/4)
    
# 2. כתוב פונקציה המקבלת 2 מספרים, הפונקציה תדפיס את כל המספרים הזוגיים בטווח של שני המספרים שהתקבלו לפונקציה
def evenRange(x,y):
    for x in range(x,y):
      if x%2==0:
         print(x,end=' ')
            
# 3. כתוב פונקציה המקבלת 2 משתנים, הפונקציה תחזיר את המכפלה שלהם ללא פעולת הכפל
def multi(x,y):
    z = 0
    for i in range(x):
        z = z + y
    print(z) 
    
# 4. כתוב פונקציה המקבלת 2 מספרים, הראשון יהווה בסיס החזקה והשני מעריך החזקה. על הפונקציה להדפיס את החזקה ללא פונקציות עזר כלשהן 
def pow(x, y):
    z = 1
    for i in range(y):
        z = z * x
    print(z) 
# 5. כתוב פונקציה הכוללת את ספריית טורטל המציירת 5 ריבועים כאשר כל אחד מהם מוכל בתוך הריבוע הקודם כך שכל צלע ריבוע קטנה מקודמתה ב10 אינץ
def squares(size):
    for i in range(0,5):
        for i in range(4):
            p1.forward(size)
            p1.left(90)
        size=size+10
#  6.  כתוב פונקציה המקבלת 2 פרמטרים, מספר שורות של המטריצה ומספר העמודות. על הפונקציה להדפיס מטריצת כוכביות * כפי המשתנים שהתקבלו לפונקציה
def matS(x,y):
    for i in range(x):
        print()
        for j in range(y):
            print("*",end="  ")
            
#  7. כתוב פונקציה המקבלת 2 משתנים השני גדול מהראשון המהווים טווח.הפונקציה תדפיס את מספר הפעמים של כל ספרה בטווח. לדוגמא: המשתנה הראשון 1 והשני 4 אז יודפס
#     1
#     2 2
#     3 3 3
def oAO(x,y):
    z=x
    for i in range(x,y):
       for x in range(z):
           print(i,end=' ')
       print()
       z=z+1 

#  8. כתוב פונקציה המקבלת שני פרמטרים המהווים מספרי שורות ועמודות של מטריצה, 
#     הפונקציה תדפיס משולש ישר זוית ע"י הכוכביות כך ששורת העמודות מהווה את הגובה ומספר השורות מהווה את בסיס המשולש
