from prime_kalia_vansh import prime_kalia_vansh
import math

def test_is_prime_param(param=[(2, True), (7, True), (4, False), (10, False), (0, False), (1, False), (-3, False)]):
    for number, is_prime_expected in param:
        is_prime_actual = prime_kalia_vansh.is_prime(number)
        assert is_prime_expected == is_prime_actual, f"Value {number} is not a prime number (Expected: {is_prime_expected}, Actual: {is_prime_actual})"