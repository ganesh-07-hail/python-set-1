# to find all prime factors of a number
def prime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
        else:
            return True
    else:
        return False
def factors_num(n):
    for i in range(1,n+1):
        if n%i==0:
            p=prime(i)
            if p==True:
                print(i)
n=int(input())
factors_num(n)