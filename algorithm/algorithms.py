from functools import reduce
from math import sin, cos, sqrt, pi
from random import randint


def linear_algorithm(a, b, x):
    try:
        y = sin(a / b) + sin(a / b) ** 2 + cos(x ** 2) + cos(sqrt(x))
        y = round(y, 2)
    except ZeroDivisionError:
        y = "cannot be divided by 0"
    except ValueError:
        y = "it is impossible to find the root of a negative number"
    return y


def branches_algorithm(r, c, b):
    try:
        if r > 0:
            y = (pi * r ** 2) / (2 * pi * r + 21 * r)
        else:
            y = (c ** 2 + b ** 2) / (pi * r ** 2)
        y = round(y, 2)
    except ZeroDivisionError:
        y = "cannot be divided by 0"
    return y


def cyclic_algorithm(n, p):
    n, p = n + 1, p + 1
    if n < 2 or p < 2:
        return "the upper limit must be greater than 0"

    try:
        f = (reduce(lambda x, y: x * y, (randint(1, 100) for i in range(1, n))) + sum(
            (randint(1, 100) for i in range(1, p)))) / \
            sum(sum(randint(1, 100) + randint(1, 100) for i in range(1, p)) for j in range(1, n))
        f = round(f, 2)
    except ZeroDivisionError:
        f = "cannot be divided by 0"
    return f
