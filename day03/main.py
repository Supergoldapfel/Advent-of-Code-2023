f = open("./input.txt", 'r').readlines()
f = [f[i].replace('\n', '') for i in range(len(f))]

input = [list(line) for line in f]
adj = [[-1, -1], [-1, 1], [1, -1], [1, 1], [0, -1], [0, 1], [-1, 0], [1, 0]]
nonSym = ["0","1","2","3","4","5","6","7","8","9","."]

sum = 0
included = []
adjNums = [[[] for x in range(len(input[y]))] for y in range(len(input))]
for y in range(len(input)):
    for x in range(len(input[y])):
        nextToSym = False
        nextToStars = []
        for dir in adj:
            if y+dir[0] in range(len(input)) and x+dir[1] in range(len(input[y])) and input[y+dir[0]][x+dir[1]] not in nonSym:
                nextToSym = True
                if(input[y+dir[0]][x+dir[1]] == "*"):
                    nextToStars.append([y+dir[0],x+dir[1]])
        if nextToSym and input[y][x] in nonSym[:-1] and [y,x] not in included:
            numStart = -1
            numEnd = x
            endFound = False
            for i in range(len(input[y])):
                if i <= x:
                    if input[y][i] in nonSym[:-1] and numStart == -1:
                        numStart = i
                    elif input[y][i] not in nonSym[:-1] and numStart != -1:
                        numStart = -1
                else:
                    if input[y][i] in nonSym[:-1] and not endFound:
                        numEnd = i
                    else:
                        endFound = True
            for i in range(numStart, numEnd+1):
                included.append([y, i])
            partNum = int("".join(input[y][numStart:numEnd+1]))
            sum += partNum
            for starPos in nextToStars:
                adjNums[starPos[0]][starPos[1]].append(partNum)

print(sum)

sum = 0
for y in range(len(adjNums)):
    for x in range(len(adjNums[y])):
        if len(adjNums[y][x]) == 2:
            sum += int(adjNums[y][x][0]) * int(adjNums[y][x][1])

print(sum)