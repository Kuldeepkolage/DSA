# Function to check if a given number is prime
def checkPrime(n):
    cnt = 0  # Initialize a counter variable to count the number of factors

    # Loop through numbers from 1 to n
    for i in range(1, n + 1):
        # If n is divisible by i without any remainder
        if n % i == 0:
            cnt += 1  # Increment the counter

    # If the number of factors is exactly 2 (1 and the number itself), it's prime
    return cnt == 2

# Driver code
n = 1483  # Example number
isPrime = checkPrime(n)  # Function call to check if the number is prime

if isPrime:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
