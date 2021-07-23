def last(n) :
    return n[-1]

def sort_last(l) :
    return sorted(l,key=last)

list=[(2,3),(1,2),(8,5),(8,4)]
print(sort_last(list))
