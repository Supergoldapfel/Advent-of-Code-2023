f = open("./input.txt", 'r').readlines()
f = [f[i].replace('\n', '') for i in range(len(f))]

'''symbols = []
for line in f:
    lineSymbols = []
    for symbol in line:
        if symbol.isnumeric():
            lineSymbols.append(symbol)
    symbols.append(lineSymbols)

caliVals = []
for l in symbols:
    caliVals.append(int(l[0]+l[-1]))

print(sum(caliVals))'''

words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
symbols = []
for line in f:
    lineSymbols = []
    for s in range(len(line)):
        symbol = line[s]
        if symbol.isnumeric():
            lineSymbols.append(symbol)
        else:
            for w in range(len(words)):
                word = words[w]
                if len(line)-s >= len(word) and line[s:s+len(word)] == word:
                    lineSymbols.append(str(w+1))
    symbols.append(lineSymbols)

caliVals = []
for l in symbols:
    caliVals.append(int(l[0]+l[-1]))

print(sum(caliVals))