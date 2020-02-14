#to print all alphabets from a to z. - using while loop
def alpha(n):
    while(n<=90):
        print(chr(n),end=' ')
        n+=1
n=65
alpha(n)