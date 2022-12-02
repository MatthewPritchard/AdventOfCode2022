with open("AOC_2_input.txt") as file:
    totalScore = 0
    for line in file:
        theirs, result = line.strip().split(" ")
        if result == "X":
            totalScore += 0  # redundant
            totalScore += (((ord(theirs) - 65) + 2) % 3)+1
        elif result == "Y":
            totalScore += 3
            totalScore += ord(theirs) - 64
        else:
            totalScore += 6
            totalScore += (((ord(theirs) - 65) + 1) % 3) + 1
    print(totalScore)