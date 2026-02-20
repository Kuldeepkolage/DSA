
def find_gcd(n1, n2):
    # Initialize gcd to 1
    gcd = 1

    for i in range(1, min(n1, n2) + 1):

        if n1 % i == 0 and n2 % i == 0:

            gcd = i

    return gcd

if __name__ == "__main__":
    n1, n2 = 20, 15
    
    # Find the GCD of n1 and n2
    gcd = find_gcd(n1, n2)

    print("GCD of", n1, "and", n2, "is:", gcd)
    
                                