
import random
list1=[2,4,6,8,10,12,14,16,18,20]
list2=[1,3,5,7,9,11,13,15,17,19]
list3=["aba","saba","hana","ana","Yossi","roni"]

# 1. כתוב פונקציה המגדירה רשימה הכוללת 10 מספרים שלמים, הפונקציה תדפיס את תא 3 מהרשימה ובשורה נוספת את תאים 2 עד 4 כולל מהרשימה ותאים חמישי עד הסוף
def f1():
    list1=[1,2,3,4,5,6,7,8,9,10]
    print(list1[2])
    print(list1[1:4])
    print(list1[4:])
    
# 2.   כתוב פונקציה המגדירה רשימה מהמספר 1 עד 10, הפונקציה תשנה את תאי הרשימה כך שבתאים ראשון עד רביעי הסדר מספרים עולה ובתאים חמישי עד שמיני כולל סדר המספרים יור שאר התאים הנותרים ימחקו
def f2():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list1)
    list1[4:]=[8,7,6,5]
    print(list1)
# 3.   כתוב פונקציה המגדירה רשימה בת 10 מספרים עולים, הפונקציה תשנה את הרשימה כך שתאים ראשון עד שישי ישארו בסדר עולה אך תאים שביעי עד שניים עשר יהיו בסדר יורד. על הפונקציה לבצע הדפסה לפני ואחרי השינוי ברשימה  
def f3():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list1)
    list1[6:]=[12,11,10,9,8,7]
    print(list1)    
    
# 4. כתוב פונקציה המגדירה רשימה הכוללת 10 מילים, הפונקציה תדפיס את תאים שלישי עד חמישי כולל ב2 דרכים, 
#     האחת ע"י מספרים חיוביים והשניה מספרים שליליים
def f4():
    list1=["chicken","goose","sheep","cow","cat","dog","mouse","elephant","giraffe","monkey"]
    print(list1[2:5])
    print(list1[-8:-5])

# 5.
import random
def f5(list1):
    num=random.randrange(1,20)
    print(num)
    if num in list1:
        print("True")
    else:
        print("False")
list1=[1,2,3,4,5,6,7,8,9,10]
# 6.
def f6():
    list1.extend(list2)
    list1.sort()
    i=len(list1)-1
    while(i>0):
        print(list1[i],end=" ")
        i=i-1
# 7.
def f7():
    str=""
    i=0
    while(i<len(list3)):
        if(i!=(len(list3)-1)):
             str=str+list3[i]+","
        else:
            str = str + list3[i]
        i=i+1
    print(str)


