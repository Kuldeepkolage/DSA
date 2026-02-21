def f(i,n):
    if i<1:
        return
    f(i-1,n)
    print(i)

n=3
f(n,n)