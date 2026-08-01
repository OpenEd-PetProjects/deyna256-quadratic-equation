import math


def discriminant(a, b, c):
    """Дискриминант уравнения a*x^2 + b*x + c = 0."""
    return b * b - 4 * a * c


def solve(a, b, c):
    """Решает a*x^2 + b*x + c = 0, возвращает (kind, *корни).

    Пока не поддержано вырождение a == 0.
    """
    if a == 0:
        raise NotImplementedError("вырожденный случай a == 0")
    d = discriminant(a, b, c)
    if d < 0:
        return ("none",)
    if d == 0:
        return ("one", -b / (2 * a))
    root = math.sqrt(d)
    return ("two", (-b - root) / (2 * a), (-b + root) / (2 * a))
