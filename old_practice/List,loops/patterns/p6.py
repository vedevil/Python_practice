n=int(input("give height"))
for i in range(n,-1,-1):
    for j in range(n,i,-1):
        print('*',end=" ")
        
    print("")
    for k in range(i+1):
        print("",end=" ")

