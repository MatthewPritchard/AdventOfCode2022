with open("AOC 1 Input.txt", 'r') as infile:
    highest = float("-Infinity")
    current = 0
    for line in infile:
        if not line.strip():
            highest = max(current, highest)
            current = 0
        else:
            current += int(line.strip())
    print(highest)
