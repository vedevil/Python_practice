def subset(l1,l2,i):
    print(l2)
    if i==len(l1):
        l2.pop()
        return
    else:
        l2.append(l1[i])
        subset(l1,l2,i+1)
original_list=[]
n=int(input("Give no of element"))
for i in range(n):
    x=input("enter next element")
    original_list.append(x)
empty_list=[]
subset(original_list,empty_list,0)
