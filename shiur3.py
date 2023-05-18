# 1.כתוב תוכנית הקולטת מהמקלדת 2 משתנים שלמים, התוכנית תדפיס את מכפלתם.
x=int(input("Enter your num:"))
y=int(input("Enter your num:"))
print(x*y)
# 2. כתוב תוכנית המגדירה 2 משתנים עשרוניים, התוכנית תדפיס את ההפרש שלהם.
x=10.5
y=5.3
print(x-y)
# 3. כתוב תוכנית המקבלת מהמקלדת מספר חודשים וממירה ומדפיסה את המספר השנים
month=int(input("Enter months:"))
years=month/12
print(round(years,3))
# 4.  y=2x+5 כתוב תוכנית הקולטת את איקס ומדפיסה את וויי על פי הפונקציה.
x=int(input("Enter a value for x:"))
y=(2*x)+5
print(y)
# 5. כתוב תוכנית שבוחרת שני מספרים בין 1 ל-10 באופן רנדומלי ומדפיסה את מכפלתם.
import random
x=random.randrange(1,11)
y=random.randrange(1,11)
print(x*y)


