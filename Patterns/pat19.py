n = int(input("Enter a number:"))
for i in range(1, n + 1):
    for ch in range((ord('F') - i), ord('F')):
        print(chr(ch), end=" ")
    print()