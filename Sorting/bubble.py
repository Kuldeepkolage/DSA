n=int(input("Enter the number of elements: "))
arr=[]
for i in range(n):
    element=int(input("Enter element: "))
    arr.append(element) 

    for i in range(len(arr)-1):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
print("Sorted array:", arr)
