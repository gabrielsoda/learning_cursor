# Determine if a number is prime.
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:  # Check for 2 first
        return True
    if n % 2 == 0:  # Then check if even (excluding 2)
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Example tests for is_prime function
if __name__ == "__main__":
    test_cases = [0, 1, 2, 3, 4, 5, 9, 11, 15, 17, 19, 20, 23, 25, 29]
    for n in test_cases:
        print(f"is_prime({n}) = {is_prime(n)}")

