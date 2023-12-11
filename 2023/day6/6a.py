import sys, os
sys.path.append(os.path.abspath(os.path.join('../', 'aoc')))

from aoc import get_input
import re

data = get_input(6).splitlines()


# data = """Time:      7  15   30
# Distance:  9  40  200""".split("\n")

map = {}

res = 1
data = [[int(k) for k in re.findall("[0-9]+",i)] for i in data]
for i in range(len(data[0])):
    map[data[0][i]] = data[1][i]

for i in map:
    count = 0
    for k in range(1,i+1):
        # print((i-k)*k)
        if (i - k)*k > map[i]:
            count += 1
    res *= count
    print(i, count)

print(res)