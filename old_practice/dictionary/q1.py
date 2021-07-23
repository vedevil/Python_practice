import operator
data = {7:5,5:2,6:4,2:7}
updated=sorted(data.items(),key=lambda x:x[0])
print(updated)
