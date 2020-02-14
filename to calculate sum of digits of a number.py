# to calculate sum of digits of a number
def sumofdig(g):
    r=0
    for i in range(len(g)):
        r=r+g[i]
    return print(r)
g=list(map(int,input()))
sumofdig(g)
