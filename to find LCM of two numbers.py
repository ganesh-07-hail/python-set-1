# to find LCM of two numbers
def lcm(n,m):
    return (n*m)/gcd(n,m)
def gcd(x,y):
    if y!=0:
        return gcd(y,x%y)
    else:
        return x
n,m=map(int,input().split())
print(int(lcm(n,m)))