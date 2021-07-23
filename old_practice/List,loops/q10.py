def check(l,n) :
    fl=[]
    for i in l:
        if len(i)<=n:
            fl.append(i)
    return fl
list=["abcd","gvgvgh","hbk","dd"]
print(check(list,3))
