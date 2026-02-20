class Solution:
    # Function to find all divisors
    def getDivisors(self, N):
        # Create list to store divisors
        res = []

        # Loop from 1 to N
        for i in range(1, N + 1):
            # Check if i is a divisor of N
            if N % i == 0:
                # Add i to result
                res.append(i)

        # Return the list of divisors
        return res

# Create object of Solution class
sol = Solution()

# Input number
N = 36

# Call the function to get divisors
result = sol.getDivisors(N)

# Print the result
print("Divisors of", N, ":", *result)
