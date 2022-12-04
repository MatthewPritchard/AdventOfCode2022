with open("input.txt") as f:
    count = 0
    for line in f:
        (a, b), (c, d) = ((int(j) for j in i.split("-")) for i in line.strip().split(","))
        if (a in range(c, d + 1) or b in range(c, d + 1)) or (c in range(a, b + 1) or d in range(a, b + 1)):
            count += 1
    print(count)
