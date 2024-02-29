# 3. כתוב פונקציה המקבלת מחרוזת, הפונקציה תדפיס רק את התווים שמספרי התאים שווים לסדרת פיבונאצ'י.
def f3(str1):
    a=1
    b=2
    i=0
    while a<len(str1):
        print(str1[a],end=" ")
        if(b<len(str1)):
            print(str1[b],end=" ")
        a=a+b
        b=a+b
