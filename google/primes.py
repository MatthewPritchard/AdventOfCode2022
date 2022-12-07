from itertools import chain, islice


def solution(i):
    """
    This solution uses the seive of eratosthenes to generate primes as needed,
    and then iterates over those primes keeping track of the index of the
    first digit of each prime to extract substrings
    """
    primes = eratosthenes(
        1000000)  # I'm not sure of the scaling rule needed here, but the constraints specify n between 10 and 10000
    current = 0
    remaining = 5
    result = ""
    for j in primes:
        digits = len(str(j))
        if not (current + digits < i):
            substr = str(j)[max(0, i - current): min(digits, (i + 5) - current)]
            remaining -= len(substr)
            result += substr
        assert remaining >= 0
        if remaining == 0:
            break
        current += digits
    return result


def solution2(i):
    primes = (str(i) for i in eratosthenes(1000000))
    return "".join(islice(chain.from_iterable(primes), i, i + 5))


"""
// working out

current      0  1  2  3  45  67  89  1011
primes      [2, 3, 5, 7, 11, 13, 17, 1 9, 101, 1001,]

i=7
01234  56789  1011121314
        [012  3 4]
54321, 54323, 5 4 3 2 7
"""


def eratosthenes(n):
    """
    textbook (literally my university textbook) seive of eratosthenes
    """
    multiples = set()
    for i in range(2, n + 1):
        if i not in multiples:
            yield i
            multiples.update(range(i * i, n + 1, i))


print(solution(0), solution2(0))
print(solution(2), solution2(2))
print(solution(5), solution2(5))
print(solution(10), solution2(10))