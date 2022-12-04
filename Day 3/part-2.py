rucksackInput = open("./Day 3/input.txt", "r")

priorities = {
    "a": "1",
    "b": "2",
    "c": "3",
    "d": "4",
    "e": "5",
    "f": "6",
    "g": "7",
    "h": "8",
    "i": "9",
    "j": "10",
    "k": "11",
    "l": "12",
    "m": "13",
    "n": "14",
    "o": "15",
    "p": "16",
    "q": "17",
    "r": "18",
    "s": "19",
    "t": "20",
    "u": "21",
    "v": "22",
    "w": "23",
    "x": "24",
    "y": "25",
    "z": "26"
}

totalScore = 0
linesThrough = 1
elfGroups = []

for rucksack in rucksackInput:
    elfGroups.append(rucksack.removesuffix('\n'))
    if linesThrough == 3:
        similar = list(set(elfGroups[0]).intersection(elfGroups[1], elfGroups[2]))
        
        prio = int(priorities[similar[0].lower()])
        if similar[0].isupper():
            prio += 26
    
        totalScore += prio

        elfGroups = []
        linesThrough = 1
    else:
        linesThrough += 1

print(totalScore)