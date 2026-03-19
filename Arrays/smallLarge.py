def find_smallest_and_largest(array):
    # Check if the array is empty
    if not array:
        return None  # Return None for an empty array

    # Initialize variables to track the smallest and largest elements
    smallest = float('inf')
    largest = float('-inf')

    # Iterate through the array to find the smallest and largest elements
    for num in array:
        if num < smallest:
            smallest = num  # Update smallest if a smaller element is found
        if num > largest:
            largest = num  # Update largest if a larger element is found

    return smallest, largest  # Return the smallest and largest elements as a tuple
# Example usage
if __name__ == "__main__":
    arr = [3, 1, 4, 1, 5, 9]
    smallest, largest = find_smallest_and_largest(arr)
    print("Smallest:", smallest)
    print("Largest:", largest)
    