str1="APQR"
str2="ABCD"
for i in range(4):
    for j in range(4):
        if j>i:
            print(str1[j],end=" ")
        else:
            print(str2[j],end=" ")
    print("")

