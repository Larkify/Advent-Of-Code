# Assignments overlap 
# How many pairs does one fully contian the other? 
# E.g: 2-8 fully contains 3-7.
total = 0

pairsInput = open("./Day 4/input.txt", "r")

for pair in pairsInput:
    elfSections = pair.split(",")

    numbersInElfA = []
    numbersInElfB = []
    for i in range(int(elfSections[0].split("-")[0]), int(elfSections[0].split("-")[1]) + 1):
        numbersInElfA.append(i)

    for i in range(int(elfSections[1].split("-")[0]), int(elfSections[1].split("-")[1]) + 1):
        numbersInElfB.append(i)

    similar = list(set(numbersInElfA).intersection(numbersInElfB))

    if len(similar) != 0:
        total += 1

print(total)
