#to find one's complement of a binary number
def ones(n):
    t=[]
    for i in range(len(n)):
        if n[i]=='1':
            n[i]='0'
            t.append(n[i])
        elif n[i]=='0':
            n[i]='1'
            t.append(n[i])
        else:
            return 'Invalid'
    a=''.join(t)
    return a
b=list(map(str,input()))
print(ones(b))
