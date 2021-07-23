def tos(lst):
    return ''.join(lst)
def permute(s,si,ei):
    print('list after function call : ',s)
    print("new_si=",si)
    print("new_ei=",ei)
    if si==ei:
        print(tos(s))
    else:
        for i in range(si,ei+1):
            print("list before swap: ",s)
            print("i=",i)
            print("si=",si)
            print("ei=",ei)
            s[si],s[i]=s[i],s[si]
            permute(s,si+1,ei)
            s[si],s[i]=s[i],s[si]
s="ABC"
lgth=len(s)
l=list(s)
permute(l,0,lgth-1)
