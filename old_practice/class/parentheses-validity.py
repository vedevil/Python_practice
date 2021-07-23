class validity:
    def __init__(self):
        self.open=['[','{','<','(']
        self.close=[']','}','>',')']
    def parenthesis(self,str):
        myStack=[]
        valid=0
        count=0
        l=len(str)
        for i in range(l):
            if str[i] in self.open:
                myStack.append(str[i])
            else:
                q=str[i]
                p=myStack.pop()
                for j in range(4):
                    if p==self.open[j] and q==self.close[j]:
                        count+=2
                        break
        if count==l:
            valid=1
        return valid
sample=validity()
s=input("Enter sample parenthesis set\n")
if sample.parenthesis(s):
    print('valid')
else:
    print('invalid')
