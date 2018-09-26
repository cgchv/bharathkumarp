import random
min=1
max=6
roll="yes"
p1,p2=0,0

while roll=="yes" or roll=="y":
    print("Roll the dice player1")
    p=random.randint(min,max)
    if(p==6):
        q=random.randint(min,max)
        p=p+q
        print(p)
    p1=p1+p
    print(p1)
    if(p1>=50):
        break
    print("Roll the dice player2")
    q=random.randint(min,max)
    if(q==6):
        k=random.randint(min,max)
        q=q+k
        print(q)
    p2=p2+q
    print(p2)
    if(p2>=50):
        break
    roll=input("Roll the dice again")
if(p1>=50 or p2>=50):    
    if(p1>p2):
       print("p1 Wins!!!")
    elif(p2>p1):
       print("p2 Wins!!!")
    else:
       print("Match Drawn")
    
    
