n = int(input("Enter a number:"))
for i in range(1,n):
    for ch in range((ord('F') - i), ord('F')):
        print(chr(ch), end=" ")
    print()