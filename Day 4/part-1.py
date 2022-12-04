# Assignments overlap 
# How many pairs does one fully contian the other? 
# E.g: 2-8 fully contains 3-7.
total = 0

pairsInput = open("./Day 4/input.txt", "r")

for pair in pairsInput:
    elfSections = pair.split(",")

    # 2nd elfs 1st number is bigger than 1st elfs 1st number
    if int(elfSections[1].split("-")[0]) >= int(elfSections[0].split("-")[0]):
        # 2nd elfs 2nd number is smaller than 1st elfs 2nd number
        if int(elfSections[1].split("-")[1]) <= int(elfSections[0].split("-")[1]):
            total += 1
            continue

    # 1st elfs 1st number is bigger than 2nd elfs 1st number
    if int(elfSections[0].split("-")[0]) >= int(elfSections[1].split("-")[0]):
        # 1st elfs second number is smaller than 2nd elfs second number
        if int(elfSections[0].split("-")[1]) <= int(elfSections[1].split("-")[1]):
            total += 1
            continue

print(total)
