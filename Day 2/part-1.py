puzzleInput = open("./Day 2/input.txt", "r")

score = 0

for line in puzzleInput:
    opponent = line.split()[0]
    player = line.split()[1]

    # Rock
    if player == "X":
        score += 1
        if opponent == "A":
            score += 3
        elif opponent == "B":
            score += 0
        else:
            score += 6
    # Paper
    elif player == "Y":
        score += 2
        if opponent == "A":
            score += 6
        elif opponent == "B":
            score += 3
        else: 
            score += 0
    # Scissors
    else:
        score += 3
        if opponent == "A":
            score += 0
        elif opponent == "B":
            score += 6
        else:
            score += 3

print(score)
    