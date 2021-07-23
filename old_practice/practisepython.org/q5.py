def createlist(l):
    n=int(input("What is the length you want"))
    for i in range(n):
        x=int(input("enter next value"))
        l.append(x)
    return l
list1=[]
list2=[]
list1=createlist(list1)
list2=createlist(list2)
commonlist=[]
for i in list1:
    if i in list2 and i not in commonlist:
            commonlist.append(i)
print("Common elements are:",commonlist)
