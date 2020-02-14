#to print multiplication table of any number
def table(l,n):
    for i in range(1,n+1):
        print(l,' x ',i,'=',l*i)
print('Enter the number of the table  :',end=' ')
l=int(input())
print('last num :',end=' ')
n=int(input())
table(l,n)