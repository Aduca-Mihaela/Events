def f1():
    a,b=1,2
    l=[a]
    a=7
    l2=l+[a]
    l[0]=8
    print(a,l,l2)

f1()