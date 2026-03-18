def getElements(arr, n):
    # Edge case: when the array has less than 2 elements
    if n == 0 or n == 1:
        print(-1, -1)  # Print -1 for both second smallest and second largest
        return

    # Initialize variables to track the smallest, second smallest, largest, and second largest elements
    small = float('inf')
    second_small = float('inf')
    large = float('-inf')
    second_large = float('-inf')

    # Find the smallest and largest elements in the array
    for i in range(n):
        small = min(small, arr[i])  
        large = max(large, arr[i])  

    # Find the second smallest and second largest elements
    for i in range(n):
        if arr[i] < second_small and arr[i] != small:
            second_small = arr[i]  # Update second smallest if a smaller element is found
        if arr[i] > second_large and arr[i] != large:
            second_large = arr[i]  # Update second largest if a larger element is found

    # Output the second smallest and second largest elements
    print("Second smallest is", second_small)
    print("Second largest is", second_large)

# Driver code
if __name__ == "__main__":
    n = 6
    arr = [1, 2, 4, 6, 7, 5] 
    
    getElements(arr, n)