#to find sum of all even numbers between 1 to n
def sum(g):
    s=0
    t=g
    for i in range(1,g+1):
        if t%2!=0:
            s=s+i
        t-=1
    return print(s)
g=int(input())
sum(g)
