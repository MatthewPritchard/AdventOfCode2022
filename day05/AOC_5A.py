from collections import defaultdict, deque
import re

with open("input.txt") as f:
    stacks = defaultdict(deque)
    for line in f:
        if "[" in line:
            for i, char in enumerate(line):
                if char.isalpha():
                    stacks[((i - 1) // 4) + 1].appendleft(char)
        elif line.startswith("move"):
            count, start, end = (int(i) for i in re.findall(r"\d+", line))
            for i in range(count):
                stacks[end].append(stacks[start].pop())
        else:
            pass

    print("".join(i[1].pop() for i in sorted(stacks.items(), key=lambda x: x[0])))
