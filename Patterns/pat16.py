n = int(input("Enter a number:"))
for i in range(0,n):
    ch = ord('A') +  i
    for j in range(0,i+1):
        print(chr(ch), end=" ")
    print()
