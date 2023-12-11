from aoc import get_input
import math

data = get_input(5,2023).split("\n\n")

sampleData = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

# data = data.split("\n\n")
seeds = [int(i) for i in data[0].split(" ")[1:]]
print(seeds)
maps = {}
for i in data[1:]:
    maps[i.split("\n")[0].replace(" map:","")] = [[int(j) for j in k.split(" ")] for k in i.split("\n")[1:]]

def getValueFromMap(map,val):
    for i in map:
        if val >= i[1] and val <= i[1] + i[2]:
            return i[0] + (val - i[1])
    return val

res = []
for i in range(len(seeds)):
    val = seeds[i]
    for j in maps:
        val = getValueFromMap(maps[j],val)
    res.append(val)
print(min(res))
    