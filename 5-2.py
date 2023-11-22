import unittest
import math


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a



def reduce_fraction(frac):
    common = gcd(frac[0], frac[1])
    return [frac[0] // common, frac[1] // common]



def add_frac(frac1, frac2):
    lcm = frac1[1] * frac2[1] // gcd(frac1[1], frac2[1])
    numerator = frac1[0] * (lcm // frac1[1]) + frac2[0] * (lcm // frac2[1])
    result = [numerator, lcm]
    return reduce_fraction(result)



def sub_frac(frac1, frac2):
    lcm = frac1[1] * frac2[1] // gcd(frac1[1], frac2[1])
    numerator1 = frac1[0] * (lcm // frac1[1])
    numerator2 = frac2[0] * (lcm // frac2[1])
    result = [numerator1 - numerator2, lcm]
    return reduce_fraction(result)



def mul_frac(frac1, frac2):
    numerator = frac1[0] * frac2[0]
    denominator = frac1[1] * frac2[1]
    result = [numerator, denominator]
    return reduce_fraction(result)




def div_frac(frac1, frac2):
    result = [frac2[1], frac2[0]]
    return mul_frac(frac1, result)


def is_positive(frac):
    return frac[0] * frac[1] > 0


def is_zero(frac):
    return frac[0] == 0


def cmp_frac(frac1, frac2):
    result = sub_frac(frac1, frac2)
    if result[0] > 0:
        return 1
    elif result[0] == 0:
        return 0
    else:
        return -1


def frac2float(frac):
    return frac[0] / frac[1] if frac[1] != 0 else float('inf')




class TestFractions(unittest.TestCase):

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([3, 4], [1, 4]), [1, 2])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([2, 3], [3, 4]), [1, 2])

    def test_div_frac(self):
        self.assertEqual(div_frac([3, 5], [4, 3]), [9, 20])

    def test_is_positive(self):
        self.assertTrue(is_positive([2, 3]))
        self.assertFalse(is_positive([-2, 3]))

    def test_is_zero(self):
        self.assertTrue(is_zero([0, 5]))
        self.assertFalse(is_zero([3, 7]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([2, 5], [1, 5]), 1)
        self.assertEqual(cmp_frac([1, 3], [1, 3]), 0)
        self.assertEqual(cmp_frac([1, 7], [2, 14]), 0)
        self.assertEqual(cmp_frac([5, 8], [7, 8]), -1)

    def test_frac2float(self):
        self.assertAlmostEqual(frac2float([1, 2]), 0.5)
        self.assertAlmostEqual(frac2float([3, 4]), 0.75)


if __name__ == '__main__':
    unittest.main()
