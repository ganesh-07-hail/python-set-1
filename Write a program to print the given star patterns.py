# Write a program to print the given star patterns
def pat(n):
    k=n*2-2
    for i in range(0,n):
        for j in range(0,k):
            print(' ',end='')
        for j in range(0,i+1):
            print('* ',end='')
        k=k-1
        print('\r')
n=int(input())
pat(n)