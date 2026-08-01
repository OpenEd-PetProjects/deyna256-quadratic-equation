import math
import unittest

from quadratic import discriminant, solve


class TestDiscriminant(unittest.TestCase):
    def test_discriminant(self):
        for a, b, c, expected in [(1, -5, 6, 1), (1, 2, 1, 0), (1, 0, 1, -4)]:
            with self.subTest(a=a, b=b, c=c):
                self.assertEqual(discriminant(a, b, c), expected)


class TestTwoRoots(unittest.TestCase):
    def test_two_roots(self):
        cases = [
            (1, -5, 6, (2.0, 3.0)),
            (1, 1, -6, (-3.0, 2.0)),
            (1, 0, -2, (-math.sqrt(2), math.sqrt(2))),
            (1, -3, 0, (0.0, 3.0)),
        ]
        for a, b, c, expected in cases:
            with self.subTest(a=a, b=b, c=c):
                kind, x1, x2 = solve(a, b, c)
                self.assertEqual(kind, "two")
                self.assertEqual(sorted((x1, x2)), sorted(expected))


if __name__ == "__main__":
    unittest.main()
