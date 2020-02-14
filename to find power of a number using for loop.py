#to find power of a number using for loop
def pow(f,k):
    m=f
    for i in range(k-1):
        f=f*m
    return print(f)
f,k=map(int,input().split())
pow(f,k)