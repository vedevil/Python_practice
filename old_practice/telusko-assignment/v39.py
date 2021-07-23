def fac(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

num=int(input("Calculate fac of"))
factorial=fac(num)
print(factorial)
