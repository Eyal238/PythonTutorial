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
            
# 3.             
