count=0;
list=["abc","aba","121","xyz"]
for i in list:
    if i[0]==i[len(i)-1] and len(i)>2:
        count +=1;
print(count)
