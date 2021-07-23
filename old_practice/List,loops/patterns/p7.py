x=int(input("enter height of pattern"))
#for i in (1,x+1):
#    for j in (1,i):
#        print("0",end=" ")
#    print(i,end=" ")
#    for j in (i+1,x+1):
#        print("0",end=" ")
#    print("")
for i in range(1,x+1):
    for j in range(1,x+1):
        if i==j:
            print(i,end=" ")
        else:
            print("0",end=" ")
    print("")
