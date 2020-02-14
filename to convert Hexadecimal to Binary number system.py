# to convert Hexadecimal to Binary number system
def hextobinary(n):
    d= str(int(n,16))
    decm = int(d)
    return print(n,"in Binary is ", bin(decm))
n=input()
print(hextobinary(n))