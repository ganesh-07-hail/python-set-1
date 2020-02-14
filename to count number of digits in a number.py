#to count number of digits in a number
def dig(g):
    c=0
    while(g > 0):
        g=g//10
        c+= 1
    return c
g= int(input())
print(count(g))
