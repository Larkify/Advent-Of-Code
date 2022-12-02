puzzleInput = open("./Day 2/input.txt", "r")

score = 0

for line in puzzleInput:
    opponent = line.split()[0]
    player = line.split()[1]

    # Rock
    if opponent == "A":
        if player == "X":
            score += 3 + 0
        elif player == "Y":
            score += 1 + 3
        else:
            score += 2 + 6
    # Paper
    elif opponent == "B":
        if player == "X":
            score += 1 + 0
        elif player == "Y":
            score += 2 + 3
        else:
            score += 3 + 6
    # Scissors
    else:
        if player == "X":
            score += 2 + 0
        elif player == "Y":
            score += 3 + 3
        else:
            score += 1 + 6

print(score)
    