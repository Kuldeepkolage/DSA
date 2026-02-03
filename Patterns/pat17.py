n = int(input("Enter a number:"))
for i in range(0,n):

    for j in range(n-i-1):
        print(" ", end=" ")

    ch = ord('A') 
    for k in range(2*i+1):
        print(chr(ch), end=" ")
        if k < i:
            ch += 1
        else:
            ch -= 1


    for l in range(n-i-1):
        print(" ", end=" ")
    print()
    