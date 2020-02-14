#to convert Binary to Octal number system
def bintooct(r):
    d=int(r,2)
    return oct(d)
r=input()
print(bintooct(r))