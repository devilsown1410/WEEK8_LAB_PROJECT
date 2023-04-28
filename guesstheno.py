import random as r
c=r.randint(1,10)
print("Welcome to Guess the number")
print('1.Beginner\n2.Intermediate\n3.Advanced')
ch=int(input())
d=0
ce=0
if ch==1:
    while(1):
        print("Enter a no. between 1 and 10")
        c=r.randint(1,10)
        a=int(input("Enter the number"))
        d=d+1
        if a==c:
            print('You guessed in',d,'attempt')
            ce=d
            if ce>0 and ce<=3:
                print("Score = 10")
            elif ce>3 and ce<=5:
                print("Score = 6")
            elif ce>5 and ce<8:
                print("Score = 3")
            break
        else:
            if a>c:
                print('Too High')
            elif abs(a-c)==1:
                print("Too Close")
            else:
                print('Too Low')
    else:
        print("You Loose")
        print("Score = 0")
        print("Correct Ans =",c) 
        
    
if ch==2:
    for i in range(5):
        print("Enter a no. between 1 and 30")
        c=r.randint(1,30)
        a=int(input("Enter the number"))
        d=d+1
        if a==c:
            print('You guessed in',d,'attempt')
            ce=d
            if ce>0 and ce<=3:
                print("Score = 10")
            elif ce>3 and ce<=5:
                print("Score = 6")
            elif ce>5 and ce<8:
                print("Score = 3")
            break
        else:
            if a>c:
                print('Too High')
            elif abs(a-c)==1:
                print("Too Close")
            else:
                print("Too Low")
            print("No. of attempts left",5-(i+1))
    else:
        print("You Loose")
        print("Score = 0")
        print("Correct Ans =",c) 
if ch==3:
    for i in range(3):
        print("Enter a no. between 1 and 50")
        c=r.randint(1,50)
        a=int(input("Enter the number"))
        d=d+1
        if a==c:
            print('You guessed in',d,'attempt')
            ce=d
            if ce>0 and ce<=3:
                print("Score = 10")
            elif ce>3 and ce<=5:
                print("Score = 6")
            elif ce>5 and ce<8:
                print("Score = 3")
            break
        else:
            if a>c:
                print('Too High')
            elif abs(a-c)==1:
                print("Too Close")
            else:
                print("Too Low")
            print("No. of attempts left",3-(i+1))
    else:
        print("You Loose")
        print("Score = 0")
        print("Correct Ans =",c) 

        
                      
                
