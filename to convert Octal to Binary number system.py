# to convert Octal to Binary number system
def octtobinary(f):
    d= str(int(f, 8))
    decm = int(d)
    return print(f, "in Binary is ", bin(decm))
f=input()
octtobinary(f)