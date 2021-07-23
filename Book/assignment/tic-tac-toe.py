import random
board={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
def printboard(b,a):
    if a==0:
        l=list(b.keys())
    else:
        l=list(b.values())
    print(str(l[0])+'|'+str(l[1])+'|'+str(l[2]))
    print('-+-+-')
    print(str(l[3])+'|'+str(l[4])+'|'+str(l[5]))
    print('-+-+-')
    print(str(l[6])+'|'+str(l[7])+'|'+str(l[8]))
def update(s,m,b):
    if b[int(move)]!=' ':
        print('Sorry it is occupied try other')
        return 1
    else:
        b[int(move)]=s
        return 0
def chturn(p1,p2,t):
    if t==p1:
        return p2
    else:
        return p1
print('WELCOME TO TIC-TAC-TOE')
print('please make every move according to given naming convention')
printboard(board,0)
p1=input('Enter name of player1: ')
p2=input('Enter name of player2: ')
print('Lets begin '+p1+' vs '+p2)
players=[p1,p2]
turn=random.choice(players)
if turn==p1:
    p1sym='x'
    p2sym='o'
else:
    p1sym='o'
    p2sym='x'
symbol={p1:p1sym,p2:p2sym}
count=0
while True:
    print('Now '+turn+' turns.',end='')
    move=input('Your move is: ')
    z=update(symbol[turn],move,board)
    if z==1:
        continue
    printboard(board,1)
    turn=chturn(p1,p2,turn)
    count+=1
    if count==9:
        break
print('winner is:')
