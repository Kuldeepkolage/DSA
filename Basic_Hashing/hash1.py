n = int(input("Enter the size of the array: "))

arr = list(map(int, input("Enter the elements of the array: ").split()))

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

q = int(input("Enter the number of queries: "))

while q > 0:
    number = int(input("Enter the number to query: "))
    print(freq.get(number, 0))
    q -= 1