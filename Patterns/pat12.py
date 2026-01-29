n = int(input("Enter a number:"))
for i in range(0,n):
    for j in range(n-i-1):
        print(" ", end=" ")
    if i%2==0:
        start = 1
    else:
        start = 0   
    for j in range(i+1):
        print(start, end=" ")
        start = 1 - start
    print()