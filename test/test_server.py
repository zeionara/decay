import unittest

import sys
sys.path.append('../src/')

import server

class TestCheckData(unittest.TestCase):
    def test_positive_integer_number(self):
        assert server.check_data('17') == 17

    def test_positive_float_number(self):
        assert server.check_data('17.17') is None

    def test_zero(self):
        assert server.check_data('0') is None

    def test_negative_integer_number(self):
        assert server.check_data('-17') is None

    def test_negative_float_number(self):
        assert server.check_data('-17.17') is None

    def test_invalid_string(self):
        assert server.check_data('cogito') is None

    def test_empty_string(self):
        assert server.check_data('') is None

class TestIsPrime(unittest.TestCase):
    def test_prime_number(self):
        assert server.is_prime(17)

    def test_even_number(self):
        assert not server.is_prime(4)

    def test_positive_float_number(self):
        with self.assertRaises(ValueError) as context:
            server.is_prime(17.17)

    def test_zero(self):
        with self.assertRaises(ValueError) as context:
            server.is_prime(0)

    def test_one(self):
        with self.assertRaises(ValueError) as context:
            server.is_prime(1)

    def test_negative_integer_number(self):
        with self.assertRaises(ValueError) as context:
            server.is_prime(-17)

    def test_negative_float_number(self):
        with self.assertRaises(ValueError) as context:
            server.is_prime(-17.17)

    def test_string(self):
        with self.assertRaises(ValueError) as context:
            server.is_prime('aaa')

class TestGetPossiblePrimes(unittest.TestCase):
    def test_positive_integer_number(self):
        primes = server.get_possible_primes(17)
        assert primes == [2, 3, 5, 7]
    
    def test_positive_float_number(self):
        with self.assertRaises(ValueError) as context:
            server.get_possible_primes(17.17)

    def test_zero(self):
        with self.assertRaises(ValueError) as context:
            server.get_possible_primes(0)

    def test_one(self):
        with self.assertRaises(ValueError) as context:
            server.get_possible_primes(1)

    def test_negative_integer_number(self):
        with self.assertRaises(ValueError) as context:
            server.get_possible_primes(-17)

    def test_negative_float_number(self):
        with self.assertRaises(ValueError) as context:
            server.get_possible_primes(-17.17)

    def test_string(self):
        with self.assertRaises(ValueError) as context:
            server.get_possible_primes('aaa')

class TestFactorize(unittest.TestCase):

    def test_prime_number(self):
        primes = server.factorize(17)
        assert primes == (17,)

    def test_positive_integer(self):
        primes = server.factorize(24)
        assert primes == (2, 2, 2, 3)
    
    def test_positive_float_number(self):
        with self.assertRaises(ValueError) as context:
            server.factorize(17.17)

    def test_zero(self):
        with self.assertRaises(ValueError) as context:
            server.factorize(0)

    def test_one(self):
        with self.assertRaises(ValueError) as context:
            server.factorize(1)

    def test_negative_integer_number(self):
        with self.assertRaises(ValueError) as context:
            server.factorize(-17)

    def test_negative_float_number(self):
        with self.assertRaises(ValueError) as context:
            server.factorize(-17.17)

    def test_string(self):
        with self.assertRaises(ValueError) as context:
            server.factorize('aaa')

class TestIsPositiveInteger(unittest.TestCase):

    def test_positive_integer_number(self):
        assert server.is_positive_integer(17)
    
    def test_positive_float_number(self):
        assert not server.is_positive_integer(17.17)

    def test_zero(self):
        assert not server.is_positive_integer(0)

    def test_negative_integer_number(self):
        assert not server.is_positive_integer(-17)

    def test_negative_float_number(self):
        assert not server.is_positive_integer(-17.17)

    def test_string(self):
        assert not server.is_positive_integer('aaa')

if __name__ == '__main__':
    unittest.main()
