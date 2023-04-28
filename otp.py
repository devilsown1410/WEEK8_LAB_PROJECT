import random as r
n=int(input("Enter length of otp"))
x=r.random()
ans=str(x)
print(ans)
ans=ans[-1:-n-1:-1]
print(ans)
