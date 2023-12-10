import re
import numpy
f = open("./input.txt").read()
instructions = list(f.split("\n\n")[0])
nodes = {}
for line in f.split("\n\n")[1].split("\n"):
    nodes[line.split(" = ")[0]] = [re.findall(r"(?<=\()[A-Z0-9]+", line)[0], re.findall(r"[A-Z0-9]+(?=\))", line)[0]]

# part 1
cur = "AAA"
steps = 0
i = 0
while cur != "ZZZ":
    d = 1 if instructions[i] == "R" else 0
    cur = nodes[cur][d]
    i = (i+1)%len(instructions)
    steps += 1

print(steps)

# part 2 (not working)
# since the approach of part 1 was too slow to just use the same idea for part 2,
# the idea was to find in which interval of steps each start comes to an end
# and then find the common multiple of these, so for the example on the website this
# would be intervals of 2 and 3, and it would take 6 (2*3) steps to be at an end in all positions
# I couldnt get this to work properly tho and I think I'm completely overcomplicating this,
# so I'll come back to this at some other point
# The problem seems to need an approach similar to the one of day 5 part 2, which I also haven't been able to solve yet...
starts = [node for node in list(nodes.keys()) if node[2] == "A"]
for start in starts:
    cur = [start, 0]
    steps = 0
    visited = []
    while cur not in visited:
        visited.append(cur.copy())
        d = 1 if instructions[cur[1]] == "R" else 0
        cur[0] = nodes[cur[0]][d]
        cur[1] = (cur[1]+1)%len(instructions)
        steps += 1
    end_offsets = [e for e in range(len(visited)) if visited[e][0][2] == "Z"]
    print(end_offsets)

