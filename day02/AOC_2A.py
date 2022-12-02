
with open("AOC_2_input.txt") as file:
    totalScore = 0
    for line in file:
        theirs, mine = line.strip().split(" ")

        totalScore += ((((ord(mine)-87)-(ord(theirs)-64))+1) % 3) * 3
        totalScore += ord(mine)-87
    print(totalScore)

"""
result/3
  1 2 3
1 1 2 0
2 0 1 2
3 2 0 1
"""
"""
result/3-1
  1 2 3
1 0 1-1
2-1 0 1
3 1-1 0
"""
"""
mine-theirs
  1 2 3
1 0 1 2
2-1 0 1
3-2-1 0
"""
"""
(mine-theirs)+1
  1 2 3
1 1 2 3
2 0 1 2
3-1 0 1
"""
"""
((mine-theirs)+1)%3
  1 2 3
1 1 2 0
2 0 1 2
3 2 0 1
"""