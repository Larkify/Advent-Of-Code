file = open("./Day 3/input.txt", "r")

lineNumber = 1
elfGroup = []

for line in file:
    elfGroup.append(line)
    if lineNumber == 3:
        print(elfGroup)
        elfGroup = []
        lineNumber = 1
    else:
        lineNumber += 1