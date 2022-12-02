calorieInput = open("./Day 1/input.txt", "r")

highestScore = 0
twoScore = 0
threeScore = 0
existScore = 0

for line in calorieInput:
    if line == "\n":
        if highestScore < existScore:
            highestScore = existScore
        elif twoScore < existScore:
            twoScore = existScore
        elif threeScore < existScore:
            threeScore = existScore
        existScore = 0
    else:
        existScore += int(line)

print(highestScore + twoScore + threeScore)
        
