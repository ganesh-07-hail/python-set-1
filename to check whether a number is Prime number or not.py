#to check whether a number is Prime number or not
def prime(e):
    if e>1:
        for i in range(2,e):
            if e%i==0:
                return False
                break
        else:
            return True
    else:
        return False
e=int(input())
print(prime(e))