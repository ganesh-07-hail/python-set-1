#to convert Hexadecimal to Decimal number system
def hextodeci(n):
    d= str(int(n,16))
    decm = int(d)
    return print('Hexa value ->',n, "in decimal is ",decm)
n=input()
hextodeci(n)