def topten():
    i=1
    while i <=10:
        x= i*i*i
        yield x
        i+=1 
        

val=topten()
for i in val:
    print(i)
