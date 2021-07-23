list=[9,6,5,8,4,6,2,2]
finallist=[]
for i in list:
    if i not in finallist:
        finallist.append(i)
print(finallist)
