# to convert Octal to Hexadecimal number system
def octtohex(n):
    d= str(int(n,8))
    h=int(d)
    return print(n, "in Decimal is ",hex(h))
n=input()
octtohex(n)