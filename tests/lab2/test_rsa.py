import unittest
from src.lab2.rsa import is_prime
from src.lab2.rsa import gcd
from src.lab2.rsa import multiplicative_inverse
from math import gcd as python_gcd


class Test(unittest.TestCase):
    def test_is_prime(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                  103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                  211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
                  331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
                  449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577,
                  587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
                  709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839,
                  853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983,
                  991, 997]
        for x in range(1, 999):
            if x in primes:
                expected = True
            else:
                expected = False
            assert is_prime(x) == expected

    def test_gcd(self):
        assert gcd(0, 10) == 10
        assert gcd(30, 666) == 6
        assert gcd(773616, 999999) == 3
        assert gcd(0, 0) == 0
        for i in range(1, 999):
            for j in range(1, 999):
                assert gcd(i, j) == python_gcd(i, j)

    def test_multiplicative_inverse(self):
        assert multiplicative_inverse(3, 26) == 9
        assert multiplicative_inverse(9999, 19999) == 19997
        assert multiplicative_inverse(0, 19999) is None
