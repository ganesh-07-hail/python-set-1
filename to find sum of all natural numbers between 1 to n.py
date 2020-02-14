# to find sum of all natural numbers between 1 to n
def sum(n):
    f=0
    t=n
    for i in range(1,n+1):
        if t%2==0:
            f=f+i
            t-=1
    return print(f)
n=int(input())
sum(n)
