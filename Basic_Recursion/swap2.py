def f(l,r):
    if l >=r:
        return
    arr[l], arr[r] = arr [r], arr [l]
    f(l+1, r-1)

arr = [1, 2, 3, 4, 5]
n = len(arr)
f(0, n-1)
print(arr)