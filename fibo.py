def fibo(n):
    c=2
    b=1
    a=c
    lst=[0,1,1,2]
    #it requires further improvement
    #i am going to add feature which is able to give fibonacci sequence between any no.
    while len(lst)<n:
        a=c
        c=c+b
        lst.append(c)
        b=a
        
    return lst
        
