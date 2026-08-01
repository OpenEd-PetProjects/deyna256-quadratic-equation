import unittest

from quadratic import discriminant


class TestDiscriminant(unittest.TestCase):
    def test_discriminant(self):
        for a, b, c, expected in [(1, -5, 6, 1), (1, 2, 1, 0), (1, 0, 1, -4)]:
            with self.subTest(a=a, b=b, c=c):
                self.assertEqual(discriminant(a, b, c), expected)


if __name__ == "__main__":
    unittest.main()
