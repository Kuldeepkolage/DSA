def f(i):
    if i >= n/2:
        return
    arr[i], arr[n-1-i] = arr[n-1-i], arr[i]
    f(i+1)

arr = [1, 2, 3, 4, 5]
n = len(arr)
f(0)
print(arr)