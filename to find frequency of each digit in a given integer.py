#to find frequency of each digit in a given integer
def fre(n):
    c=0
    for i in range(len(n)):
        for j in range(1,len(n)):
            if n[i]==n[j]:
                c+=1
        if c==0:
            print('Frequency of ',n[i],' is ',c+1)
        print('Frequency of ',n[i],' is ',c)
        c=0
n=list(map(int,input()))
fre(n)
