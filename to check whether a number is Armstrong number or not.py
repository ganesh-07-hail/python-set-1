#to check whether a number is Armstrong number or not
def armstrong(n):
    s=0
    while(n>0):
        r=n%10
        s=s+r**3
        n=n//10
    return s
n=int(input())
m=armstrong(n)
if n==m:
    print('It is a armstrong number')
else:
    print("it is not a armstrong number")