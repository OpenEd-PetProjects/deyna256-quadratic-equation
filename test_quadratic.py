import math
import unittest

from quadratic import discriminant, solve


class RootsTestCase(unittest.TestCase):
    """Единая стратегия сравнения вещественных корней: порядок не важен."""

    def assert_close_pair(self, actual, expected):
        self.assertEqual(len(actual), len(expected))
        for got, want in zip(sorted(actual), sorted(expected)):
            self.assertTrue(
                math.isclose(got, want, rel_tol=1e-9, abs_tol=1e-12),
                f"{actual} != {expected}",
            )


class TestDiscriminant(unittest.TestCase):
    def test_discriminant(self):
        for a, b, c, expected in [(1, -5, 6, 1), (1, 2, 1, 0), (1, 0, 1, -4)]:
            with self.subTest(a=a, b=b, c=c):
                self.assertEqual(discriminant(a, b, c), expected)


class TestTwoRoots(RootsTestCase):
    def test_two_roots(self):
        cases = [
            (1, -5, 6, (2.0, 3.0)),
            (1, 1, -6, (-3.0, 2.0)),
            (1, 0, -2, (-math.sqrt(2), math.sqrt(2))),
            (1, -3, 0, (0.0, 3.0)),
            (2, -4, -3, (1 - math.sqrt(10) / 2, 1 + math.sqrt(10) / 2)),
        ]
        for a, b, c, expected in cases:
            with self.subTest(a=a, b=b, c=c):
                kind, *roots = solve(a, b, c)
                self.assertEqual(kind, "two")
                self.assert_close_pair(roots, expected)


class TestOneRoot(RootsTestCase):
    def test_one_root(self):
        for a, b, c, expected in [(1, -4, 4, 2.0), (4, -4, 1, 0.5), (1, 0, 0, 0.0)]:
            with self.subTest(a=a, b=b, c=c):
                kind, *roots = solve(a, b, c)
                self.assertEqual(kind, "one")
                self.assert_close_pair(roots, (expected,))


class TestNoRoots(unittest.TestCase):
    def test_negative_discriminant(self):
        for a, b, c in [(1, 0, 1), (1, 1, 1)]:
            with self.subTest(a=a, b=b, c=c):
                self.assertEqual(solve(a, b, c), ("none",))


class TestDegenerate(RootsTestCase):
    def test_linear(self):
        for a, b, c, expected in [(0, 2, -4, 2.0), (0, -3, 1.5, 0.5)]:
            with self.subTest(a=a, b=b, c=c):
                kind, *roots = solve(a, b, c)
                self.assertEqual(kind, "linear")
                self.assert_close_pair(roots, (expected,))

    def test_no_roots_and_inf(self):
        self.assertEqual(solve(0, 0, 0), ("inf",))
        self.assertEqual(solve(0, 0, 5), ("none",))


if __name__ == "__main__":
    unittest.main()
