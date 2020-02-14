#to find first and last digit of a number
def num(n):
    c=0
    x=n
    r=0
    z=0
    s=0
    while(n>0):
        c+=1
        if c==1:
            r=n%10
            s=s+r
            n=n//10
            break
    while(c>0):
        r=n%10
        z=z+r
        n=n//10
        if n<10:
            break
    return 'The first and last digits are ',n,' and ',s
n=int(input())
print(num(n))
