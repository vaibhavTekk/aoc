import sys, os
sys.path.append(os.path.abspath(os.path.join('../', 'aoc')))

from aoc import get_input

data = get_input(2).splitlines()

t = 0
for i in range(len(data)):
    groups = data[i].strip().split(': ')[1].split("; ")
    for g in groups:
        m = {"red":0,"green":0,"blue":0}
        for k in g.split(", "):
            a,b = k.split(" ")
            m[b] = int(a)
        if m["red"] > 12 or m["green"] > 13 or m["blue"] > 14:
            break
    else:
        t += i + 1

print(t)