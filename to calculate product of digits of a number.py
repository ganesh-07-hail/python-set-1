#to calculate product of digits of a number
def productofdigit(g):
    r=1
    for i in range(len(g)):
        r=r*g[i]
    return print(r)
r=list(map(int,input()))
productofdigit(g)
