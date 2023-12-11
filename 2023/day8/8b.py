import sys, os
sys.path.append(os.path.abspath(os.path.join('../', 'aoc')))

from aoc import get_input
import math

data = get_input(8)

# data = """LR

# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)"""

ins, mapArr = data.split("\n\n")[0], data.split("\n\n")[1].split("\n")
mapDict = {}
for i in range(len(mapArr)):
    arr = mapArr[i].replace(")","").replace(" = (",",").replace(" ","").split(",")
    mapDict[arr[0]] = {"L":arr[1],"R":arr[2]}
print(ins,mapDict)

def end(arr):
    for i in arr:
        if i[-1] != "Z":
            return False
    return True

currArr = []
for i in mapDict:
    if i[-1] == 'A':
        currArr += [i]
print("start:",currArr)

countArr = []

def lcm(a,b):
    return int((a*b)/math.gcd(a,b))

for c in currArr:
    curr = c
    i = 0
    count = 0
    while curr[-1] != 'Z':
        if i == len(ins):
            i = 0
        curr = mapDict[curr][ins[i]]
        i += 1
        count += 1
    countArr.append(count)

arrlcm = 1
for i in countArr:
    arrlcm = lcm(arrlcm,i)
print(arrlcm)