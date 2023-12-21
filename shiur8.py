#  1.
str1=["aba","saba","adir","david","moran"]
def f1(str1):
  sum=0;
  for i in str1:
    for j in i:
      if j=="a":
        sum=sum+1
  print(sum)

# 2.
#7. כתוב פונקציה המקבלת איבר ראשון של סדרה חשבונית ואת הפרש הסדרה. הפונקציה תדפיס את 10 האיברים של הסדרה.
def f3(a1,diff):
    for i in range(1,11):
        print(a1+(diff*(i-1)),end=" ")

