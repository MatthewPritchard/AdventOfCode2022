from functools import reduce


def priority(item: int):
    return item - (96 if item > 95 else 38)


with open("AOC_3_input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    total = 0
    for i in range(0, len(lines), 3):
        group = [set(rucksack) for rucksack in lines[i:i + 3]]
        result = reduce(lambda x, y: x.intersection(y), group)
        total += priority(ord(result.pop()))
    print(total)
