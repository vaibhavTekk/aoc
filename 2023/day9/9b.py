import sys, os
sys.path.append(os.path.abspath(os.path.join('../', 'aoc')))

from aoc import get_input

data = get_input(9).splitlines()

# data = """10 13 16 21 30 45""".split("\n")

def allZeros(vals):
    for i in vals:
        if i != 0:
            return False
    return True

def get_intials(vals):
    initials = [vals[0]]
    currentVals = vals
    while not allZeros(currentVals):
        newVals = []
        for i in range(1,len(currentVals)):
            newVals += [currentVals[i] - currentVals[i-1]]
        currentVals = newVals
        initials.append(newVals[0])
    return initials

res = 0

for i in data:
    vals = [int(val) for val in i.split(" ")]
    initials = get_intials(vals)
    sum = 0
    for k in initials[::-1]:
        sum = k - sum
    res += (sum)
print(res)