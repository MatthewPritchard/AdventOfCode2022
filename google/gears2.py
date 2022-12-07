from fractions import Fraction
from itertools import tee


def pairwise(iterable):  # patching python2.7 so much
    """s -> (s0,s1), (s1,s2), (s2, s3), ..."""
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def valid(pegs, a):
    distances = [j - i for i, j in pairwise(pegs)]
    current = a
    for i in range(len(pegs) - 1):
        if current > distances[i] or current < 1:
            return False
        current = distances[i] - current
    return True


def solution(pegs):
    total = Fraction(0)
    i = -1
    for j, peg in enumerate(pegs):
        if j in (0, len(pegs) - 1):
            total += i * Fraction(2 * peg)
        else:
            total += i * Fraction(4 * peg)
        i *= -1
    if len(pegs) % 2 == 0:
        total /= 3
    if not valid(pegs, total):
        return [-1, -1]
    else:
        return [total.numerator, total.denominator]
