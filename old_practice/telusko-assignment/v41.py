def fac(n):
    if n==0:
        return 1
    else:
        return n*fac(n-1)
num=int(input("Find factorial of"))
ans=fac(num)
print(ans)
