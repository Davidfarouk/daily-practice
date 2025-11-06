def solve(n):
    """Fibonacci using recursion"""
    if n <= 1:
        return n
    return solve(n-1) + solve(n-2)

def factorial(n):
    """Calculate factorial"""
    if n <= 1:
        return 1
    return n * factorial(n-1)

def is_prime(n):
    """Check if number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
