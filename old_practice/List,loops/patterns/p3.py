num=int(input("ENTER NUMBER"))
for i in range(num,0,-1):
    for j in range (num,i-1,-1):
        print(j,end=" ")
    print()
