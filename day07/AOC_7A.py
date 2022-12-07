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
    size = sum((j if type(j) == int else sizes(name+"/"+i, j, dirs) for i, j in d.items() if i != ".."))
    dirs[name] = size
    return size


directories = Counter()
sizes("/", structure, directories)
print(sum([j for i, j in directories.items() if j < 100000]))
print(directories.most_common())
