import random as r
print("ROCK PAPER SCISSOR GAME".center(75))
while(1):
    print("Do you want to play the Game: YES/NO")
    ch=input("Enter Choice").upper()
    if ch=='YES':
        print("1. ROCK vs SCISSOR : ROCK WINS\n2. PAPER vs SCISSOR : SCISSOR\n3. ROCK vs PAPER : PAPER".center(25))
        c=r.choice(['ROCK','PAPER','SCISSOR'])
        u=input("Enter your choice").upper()
        if c==u:
            print("Draw")
        elif (u=='ROCK' and c=='SCISSOR') or (u=='SCISSOR' and c=='PAPER') or (u=='PAPER' and c=='PAPER'):
            print("YOU WON".center(70))
            print("YOUR CHOICE:",u)
            print("COMPUTER CHOICE:",c)
        else:
            print("COMPUTER WINS".center(70))
            print("YOUR CHOICE:",u)
            print("COMPUTER CHOICE:",c)
    elif ch=='NO':
        print("Have a Great Day")
        break
    else:
        print("Invalid Input")
