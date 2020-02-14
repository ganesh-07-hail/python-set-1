#to check whether a number is Strong number or not
def strong_num(n):
    s=0
    while(n):
        x=1
        f=1
        r=n%10
        while(x<=r):
            f*=x

            x+=1
        s=s+f
        n//=10
    return s
n=int(input())
m=strong_num(n)
if m==n:
    print("It is a strong number")
else:
    print("It is not a strong number")
