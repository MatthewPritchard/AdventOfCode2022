from collections import Counter

with open("AOC 1 Input.txt", 'r') as file:
    counter = Counter()
    entry = 0
    for line in file:
        if line.strip():
            counter[entry] += int(line.strip())
        else:
            entry += 1
    print(sum((y for x, y in counter.most_common(3))))
