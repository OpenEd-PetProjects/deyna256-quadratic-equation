import math


def discriminant(a, b, c):
    """Дискриминант уравнения a*x^2 + b*x + c = 0."""
    return b * b - 4 * a * c


def solve(a, b, c):
    """Решает a*x^2 + b*x + c = 0, возвращает (kind, *корни).

    kind ∈ {"none", "linear", "one", "two", "inf"}.
    """
    if a == 0:
        if b != 0:
            return ("linear", -c / b)
        return ("inf",) if c == 0 else ("none",)
    d = discriminant(a, b, c)
    if d < 0:
        return ("none",)
    if d == 0:
        return ("one", -b / (2 * a))
    root = math.sqrt(d)
    return ("two", (-b - root) / (2 * a), (-b + root) / (2 * a))
