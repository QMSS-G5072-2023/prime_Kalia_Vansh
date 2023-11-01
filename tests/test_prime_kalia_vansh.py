from prime_kalia_vansh import prime_kalia_vansh
import math

def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(7) is True
    assert is_prime(8) is False
    assert is_prime(9) is False

@pytest.mark.parametrize("n, expected", [
    (2, True),
    (7, True),
    (8, False),
    (9, False),
    (-1, False),
    (0, False),
    (1, False)
])
def test_is_prime_param(n, expected):
    assert is_prime(n) == expected