#to convert Binary to Hexadecimal number system
def bintohex(n):
    x=int(n,2)
    return hex(x)
n=input()
print(bintohex(n))