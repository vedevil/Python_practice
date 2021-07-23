
def count(l):
	even=0
	odd=0
	for i in l:
		if i%2==0:
			even+=1
		else:
			odd+=1
	return even,odd
lst=[7,5,9,7,8]
e,o=count(lst)
print(e)
print(o)
