def equal(l1,l2) :
    ans=0
    for x in l1 :
        for y in l2:
            if x==y:
                ans=1
                return ans
    return ans
list1=[7,9,5,3,5]
list2=[4,1,4,1,0]
print(equal(list1,list2))
