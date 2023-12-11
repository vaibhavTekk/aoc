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

data = sampleData.split("\n\n")
seedRanges = [int(i) for i in data[0].split(" ")[1:]]
seeds = []
for i in range(0,len(seedRanges),2):
    # print(seedRanges[i],seedRanges[i+1])
    for k in range(seedRanges[i], seedRanges[i]+seedRanges[i+1]):
        seeds.append(k)
# print(seeds, len(seeds))

maps = {}
for i in data[1:]:
    maps[i.split("\n")[0].replace(" map:","")] = [[int(j) for j in k.split(" ")] for k in i.split("\n")[1:]]

def getValueFromMap(map,val):
    for i in map:
        if val >= i[1] and val <= i[1] + i[2]:
            return i[0] + (val - i[1])
    return val

minVal = float("inf")
for i in range(0,len(seeds),2):
    start, length = seeds[i], seeds[i+1]
    vals = [j for j in range(start,start+length)]
    for j in maps:
        for val in vals:
            vals += [getValueFromMap(maps[j],val)]
    minVal = min(min(vals),minVal)
print(minVal)
    