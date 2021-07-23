s=input("enter sumthing")
count={}
for i in s:
    count.setdefault(i,0)
    count[i]=count[i]+1
for i in count.keys():
    print(str(i)+' has been repeated '+str(count[i])+' times.')
