l=['cat','bat','mat','rat']
a=''
for i in range(len(l)):
    if len(l)==0 or len(l)==1:
        break
    else:
        if i==len(l)-1:
            a=a+' and'
            a=a+' '+l[i]
        elif i==0:
            a=a+l[0]
        else:
            a=a+', '+l[i]
print(a)            

