def smallest_prime_palindrome(N):
    # Handle small cases directly
    if N <= 2:
        return 2
    elif N <= 3:
        return 3
    elif N <= 5:
        return 5
    elif N <= 7:
        return 7
    elif N <= 11:
        return 11
    
    # Function to check if a number is prime
    def is_prime(n):
        if n < 2:
            return False
        if n % 2 == 0:
            return n == 2
        sqrt_n = int(n**0.5) + 1
        for i in range(3, sqrt_n, 2):
            if n % i == 0:
 