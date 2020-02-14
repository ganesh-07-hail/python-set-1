#to print Fibonacci series up to n terms
def fib(n):
    f=0
    l=1
    i=0
    while n>i:
        if i<=1:
            m=1
        else:
            m=f+l
            f=l
            l=m
        print(m)
        i+=1
n=int(input())
fib(n)