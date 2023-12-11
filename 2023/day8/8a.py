import sys, os
sys.path.append(os.path.abspath(os.path.join('../', 'aoc')))

from aoc import get_input

sample1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

sample2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

data = get_input(8)

ins, mapArr = data.split("\n\n")[0], data.split("\n\n")[1].split("\n")
mapDict = {}
for i in range(len(mapArr)):
    arr = mapArr[i].replace(")","").replace(" = (",",").replace(" ","").split(",")
    mapDict[arr[0]] = {"L":arr[1],"R":arr[2]}
print(ins,mapDict)

curr = 'AAA'
i = 0
count = 0
print(mapDict)
while curr != 'ZZZ':
    if i == len(ins):
        i = 0
    print(curr, ins[i])
    curr = mapDict[curr][ins[i]]
    i += 1
    count += 1
print(count)