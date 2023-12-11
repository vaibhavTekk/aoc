import sys, os
sys.path.append(os.path.abspath(os.path.join('../', 'aoc')))

from aoc import get_input

data = get_input(2).splitlines()

sum = 0
for i in range(len(data)):
    groups = data[i].replace(",",";").strip().split(': ')[1].split("; ")
    m = {"red":0,"green":0,"blue":0}
    for g in groups:
        num, col = int(g.split(" ")[0]), g.split(" ")[1]
        m[col] = max(m[col],num)
    power = 1
    for i in m:
        power *= m[i]
    sum += power

print(sum)
