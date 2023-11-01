import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

"""
   Check for Prime Numbers

    This function verifies whether a provided number is a prime number. A prime number is defined as a number greater than 1 that has no divisors other than 1 and itself.

    Parameters:
    - n (int): The number to be examined.

    Returns:
    - bool: Returns True if 'n' is a prime number, and False otherwise.

    Example:
    >>> is_prime(5)
    True

    >>> is_prime(4)
    False
    
"""
    