n = int(input("Enter a number: "))
while (n > 0):
    lastdigit = n % 10
    print(lastdigit)
    n = n // 10
