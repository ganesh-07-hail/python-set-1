#to convert Hexadecimal to Octal number system
def hextooct(n):
    d= str(int(n,16))
    decm = int(d)
    return print(n, "in Octal is ", oct(decm))
n=input()
hextooct(n)