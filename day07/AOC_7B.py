from collections import Counter

with open("input.txt") as f:
    structure: dict[str, dict | int] = {"/": dict()}
    contents = structure
    for line in f:
        tokens = line.strip().split(" ")
        if line.startswith("$ cd"):
            contents = contents[tokens[-1]]
        elif line.startswith("$ ls"):
            pass
        elif line.startswith("dir"):
            contents[tokens[-1]] = {"..": contents}
        elif tokens[0].isnumeric():
            contents[tokens[1]] = int(tokens[0])


def sizes(name: str, d: dict, dirs: Counter):
    size = sum((l if type(l) == int else sizes(name + "/" + k, l, dirs) for k, l in d.items() if k != ".."))
    dirs[name] = size
    return size


total = 70_000_000
current = 41_412_830
directories = Counter()
sizes("/", structure, directories)
for i, j in reversed(directories.most_common()):
    if total - current + j > 30000000:
        print(j)
        break
