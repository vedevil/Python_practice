import math
n=int(input("enter num"))
for i in range(2,math.ceil(n/2)+1):
    if n%i==0:
        print("Number is not prime")
        break
else:
    print("number is prime")
