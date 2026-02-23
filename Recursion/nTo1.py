def f(n,i):
    if i > n:
        return
    print(n)
    f(n-1,i)

n = 5
f(n,1)