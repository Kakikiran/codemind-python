n=int(input())
s=0
for i in range (1,n+1):
    if n%i==0:
        s=s+1
if s==2:
    print("prime")
else:
    print("not a prime")