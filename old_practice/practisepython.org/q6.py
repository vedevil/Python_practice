import math as m
str=input("Enter string")
l=len(str)
result=0
count=0
for i in range(m.floor(l/2)):
    if str[i]==str[-i-1]:
        count+=1
    if count==m.floor(l/2):
        print("String is palindrome")
        result=1
if result==0:
    print("String is not palindrome")
