n=int(input("Enter number"))
print("Divisors are", end=" = ")
for i in range (2,n+1):
    if n%i==0:
        print(i,end=" ")
print()
