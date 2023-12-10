import numpy
import re

f = open("./input.txt", 'r').readlines()

times = [int(time) for time in re.findall(r"[0-9]+", f[0])]
distances = [int(dis) for dis in re.findall(r"[0-9]+", f[1])]

margins = []
for i in range(len(times)):
    time = times[i]
    record = distances[i]
    margin = 0
    for start in range(time+1):
        distance = start * (time - start)
        if distance > record:
            margin += 1
    margins.append(margin)

print(numpy.prod(margins))

time = int("".join(str(t) for t in times))
record = int("".join(str(d) for d in distances))
margin = 0
for start in range(time+1):
    distance = start * (time - start)
    if distance > record:
        margin += 1

print(margin)