def f(i):
    if i >= n/2:
        return True
    if s[i] != s[n-1-i]:
        return False
    return f(i+1)

s = "madam"
n = len(s)
print(f(0))