# to find HCF (GCD) of two numbers
def gcd(n,m):
    if m!=0:
        return gcd(m,n%m)
    else:
        return n
n,m=map(int,input().split())
print(gcd(n,m))
