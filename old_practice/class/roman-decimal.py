class conversion:
    def __init__(self):
        self.decimal=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        self.roman=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    def r_to_d(self,str):
        dec=0
        i=0
        l=len(str)
        while i<l and str[i]=='M':
            dec+=1000
            i+=1
        if i<l:
            if str[i]=='D':
                dec+=500
                i+=1
            elif str[i]=='C' and str[i+1]=='M':
                dec+=900
                i+=2
            elif str[i]=='C' and str[i+1]=='D':
                dec+=400
                i+=2
        while i<l and str[i]=='C':
            dec+=100
            i+=1
        if i<l:
            if str[i]=='L':
                dec+=50
                i+=1
            elif str[i]=='X' and str[i+1]=='C':
                dec+=90
                i+=2
            elif str[i]=='X' and str[i+1]=='L':
                dec+=40
                i+=2
        while i<l and str[i]=='X':
            dec+=10
            i+=1
        if i<l:
            if str[i]=='V':
                dec+=5
                i+=1
            elif str[i]=='I' and str[i+1]=='X':
                dec+=9
                i+=2
            elif str[i]=='I' and str[i+1]=='V':
                dec+=4
                i+=2
        while i<l and str[i]=='I':
            dec+=1
            i+=1
        return dec
    def d_to_r(self,num):
        roman=''
        while num>0:
            for i in range(len(self.decimal)):
                if num//self.decimal[i]!=0:
                    roman+=self.roman[i]
                    num-=self.decimal[i]
                    break
        return roman
con=conversion()
num=int(input("Enter decimal num"))
r=con.d_to_r(num)
print(r)
s=input("Enter roman numeral")
d=con.r_to_d(s)
print("its decimal representation is:",d)

