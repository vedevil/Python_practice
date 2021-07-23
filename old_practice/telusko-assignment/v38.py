def fseries(n):
    series=[]
    a=1
    b=1
    series.append(a)
    series.append(b)
    for i in range(3,n+1):
        c=a+b
        a=b
        b=c
        series.append(c)
    return series

num=int(input("Print fibonacci series upto"))
ans=fseries(num)
print(ans)
