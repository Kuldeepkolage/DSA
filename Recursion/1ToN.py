def f(i,n):
    if i > n:
        return
    print(i)
    f(i+1,n)
    
n = 5
f(1,n)