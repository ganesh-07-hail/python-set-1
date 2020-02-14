# to print all Strong numbers between 1 to n
def isstrong_num(n):
    s=0
    t=n
    while(n):
        x=1
        f=1
        r=n%10
        while(x<=r):
            f*=x
            x+=1
        s=s+f
        n//=10
    if s==t:
        return True
def strong_num(n):
    for i in range(1,n+1):
        s=isstrong_num(i)
        if s==True:
            print(i)
n=int(input())
strong_num(n)
