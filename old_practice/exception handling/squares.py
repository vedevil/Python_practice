f1=open('abc.txt','r')
f2=open('sqabc.txt','w')
for i in f1:
    f2.write("Square of ")
    z=i
    f2.write(z)
    f2.write(" ")
    f2.write("is: ")
    f2.write(str(int(i)*int(i)))
    f2.write("\n")

