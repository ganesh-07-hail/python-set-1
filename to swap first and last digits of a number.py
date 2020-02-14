#to swap first and last digits of a number
def swap():
    l=[12345789]
    l=list(map(int, str(l[0])))
    y=[]
    print(l[0])
    y=l[0]
    l[0]=l[len(l)-1]
    l[len(l)-1]=y
    return print(l)
swap()
