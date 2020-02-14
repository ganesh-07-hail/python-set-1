# to print all Armstrong numbers between 1 to n
def armstrong(n):
    s=0
    t=n
    while(n>0):
        r=n%10
        s=s+r**3
        n=n//10
    if t==s:
        return True
def armnum(n):
    t=n
    for i in range(1,n+1):
        a=armstrong(i)
        if a==True:
            print(i)
n=int(input())
armnum(n)