#insertion

n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    element = int(input("Enter element: "))
    arr.append(element)

for i in range(0, len(arr)-1):
    j = i
    while j >= 0 and arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        j -= 1

print("Sorted array:", arr)