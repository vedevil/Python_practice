str=input("Give String")
char=input("Give character")
ans=lambda str,char:str[0]==char.upper() or str[0]==char.lower()
A=ans(str,char[0])
print(A)
