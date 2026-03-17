# Function to sort the array and return the largest element
def sortArr(arr):
    # Sort the array in ascending order
    arr.sort()
    
    # Return the last element (largest element) after sorting
    return arr[-1]

# Driver code
if __name__ == "__main__":
    # Initialize arrays
    arr1 = [2, 5, 1, 3, 0]
    arr2 = [8, 10, 5, 7, 9]
    
    # Find and output the largest element in both arrays
    print("The Largest element in the array is:", sortArr(arr1))
    print("The Largest element in the array is:", sortArr(arr2))