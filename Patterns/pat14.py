n = int(input("Enter number of rows for pattern: "))
for i in range (0,n):
    for ch in range(ord('A'), ord('A') + i):
        print(chr(ch), end=" ")
    print() 