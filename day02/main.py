f = open("./input.txt", 'r').readlines()
f = [f[i].replace('\n', '') for i in range(len(f))]

games = [el.split(": ")[1].split("; ") for el in f]
games = [[r.split(", ") for r in game] for game in games]
games = [[[[int(c.split(" ")[0]), c.split(" ")[1]] for c in r] for r in game] for game in games]

maxReds = 12
maxGreens = 13
maxBlues = 14
score = 0
for gameIndex in range(len(games)):
    game = games[gameIndex]
    valid = True;
    for round in game:
        for val in round:
            amount = val[0]
            color = val[1]
            if color == "red" and amount > maxReds:
                valid = False
            if color == "green" and amount > maxGreens:
                valid = False
            if color == "blue" and amount > maxBlues:
                valid = False
    if valid:
        score += gameIndex+1

print(score)

score = 0
for gameIndex in range(len(games)):
    game = games[gameIndex]
    minReds = 0
    minGreens = 0
    minBlues = 0
    for round in game:
        for val in round:
            amount = val[0]
            color = val[1]
            if color == "red" and amount > minReds:
                minReds = amount
            if color == "green" and amount > minGreens:
                minGreens = amount
            if color == "blue" and amount > minBlues:
                minBlues = amount
    score += minReds*minGreens*minBlues

print(score)