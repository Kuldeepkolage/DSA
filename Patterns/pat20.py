n = int(input("Enter the number :"))
for i in range(1,2*n-1):
    stars = i
    spaces = 2*(n-2)

    if i>n:
        stars = 2*n-i

    for j in range(1,stars):
        print("*",end="")

    for k in range(1,spaces):
        print(" ",end="")

    for l in range(1,stars):
        print("*",end="")   
    print()

    if i<n:
        spaces-=2   
    else:
        spaces+=2
