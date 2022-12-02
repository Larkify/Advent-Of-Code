calorieInput = open("./Day 1/input.txt", "r")

highestScore = 0
existScore = 0

for line in calorieInput:
    if line == "\n":
        if highestScore < existScore:
            highestScore = existScore
        existScore = 0
    else:
        existScore += int(line)

print(highestScore)
        
