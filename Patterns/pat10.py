n = int(input("Enter the number of rows: "))

for i in range(1, 2*n):
    if i <= n:
        stars = i
    else:
        stars = (2*n - i)

    for j in range(1, stars+1):
        print("*", end="")
    print()    
