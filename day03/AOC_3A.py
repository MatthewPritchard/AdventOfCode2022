def priority(item: int):
    return item - (96 if item > 95 else 38)


with open("AOC_3_input.txt") as f:
    total = 0
    for line in f:
        line = line.strip()
        head = set(line[:len(line) // 2])
        tail = set(line[len(line) // 2:])

        char = ord(head.intersection(tail).pop())
        total += priority(char)
    print(total)
