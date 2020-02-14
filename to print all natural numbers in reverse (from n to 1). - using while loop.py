to print all natural numbers in reverse (from n to 1). - using while loop
def revnum(g):
    x=g
    while(g>0 and x>0):
        print(x)
        x-=1
        g=+1
n=int(input())
revnum(n)