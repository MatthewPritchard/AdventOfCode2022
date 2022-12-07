from itertools import pairwise
from fractions import Fraction


def findLimit(pegs, distances, a):
    current = a
    while True:
        first, last = narrow(pegs, distances, current)
        if first == current:
            return first, last
        current = first


def narrow(pegs, distances, a):
    current = a
    for i in range(len(pegs) - 1):
        if current > distances[i]:
            current = distances[i] - 1
            for j in range(i, 0, -1):
                current = distances[j - 1] - current
            return current, -1
        current = distances[i] - current
    return a, current


def solution(pegs):
    print(pegs)
    distances = [j - i for i, j in pairwise(pegs)]
    first, last = findLimit(pegs, distances, 1)
    first2, last2 = findLimit(pegs, distances, distances[0] - 1)
    print(first, last, first2, last2)
    if Fraction(first, last2) <= 2 <= Fraction(first2, last):
        return
    else:
        return [-1, -1]


print(solution([4, 17, 50]))
print(solution([4, 30, 50]))
