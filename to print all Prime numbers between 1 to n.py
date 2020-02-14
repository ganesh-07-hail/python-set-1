#to print all Prime numbers between 1 to n.
def prime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                break
        else:
            return True
    else:
        return False
def sum_prime(n):
    for i in range(1,n):
        p=prime(i)
        if p==True:
            print(i)
n=int(input())
sum_prime(n)