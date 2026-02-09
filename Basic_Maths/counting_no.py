n = int(input("Enter a number: "))
cnt = 0
while (n > 0):
    lastdigit = n % 10
    print(lastdigit)
    cnt += 1
    n = n // 10
print("Total digits: ", cnt)