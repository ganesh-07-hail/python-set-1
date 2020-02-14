#to find sum of all prime numbers between 1 to n
def prime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
                break
        else:
            return True
    else:
        return False
def sum_prime(n):
    s=0
    for i in range(1,n):
        p=prime(i)
        if (p):
            s=s+i
    return print(s)
n=int(input())
prime(n)