def gets(s,n) :
    fl=[]
    x=s.split(" ")
    for i in x:
        if len(i)>=n:
            fl.append(i)

    return fl
txt=input("Enter a string")
print(gets(txt,4))
