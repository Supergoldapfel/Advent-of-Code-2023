f = open("./input.txt").readlines()
f = [line.replace("\n", "") for line in f]

histories = [[int(val) for val in line.split(" ")] for line in f]

# part 1
total = 0
for history in histories:
    seq = history.copy()
    last_vals = []
    while True:
        last_vals.append(seq[-1])
        allzero = True
        for el in seq:
            if el != 0:
                allzero = False
        if allzero:
            break
        seq = [seq[i+1]-seq[i] for i in range(len(seq)-1)]
    extrapolated = [0]
    for last_val in list(reversed(last_vals)):
        extrapolated.append(last_val + extrapolated[-1])
    total += extrapolated[-1]

print(total)

# part 2
total = 0
for history in histories:
    seq = history.copy()
    first_vals = []
    while True:
        first_vals.append(seq[0])
        allzero = True
        for el in seq:
            if el != 0:
                allzero = False
        if allzero:
            break
        seq = [seq[i+1]-seq[i] for i in range(len(seq)-1)]
    extrapolated = [0]
    for first_val in list(reversed(first_vals)):
        extrapolated.append(first_val - extrapolated[-1])
    total += extrapolated[-1]

print(total)