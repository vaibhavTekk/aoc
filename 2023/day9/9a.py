import sys, os
sys.path.append(os.path.abspath(os.path.join('../', 'aoc')))

from aoc import get_input

data = get_input(9).splitlines()

# data = """0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45""".split("\n")

def allZeros(vals):
    for i in vals:
        if i != 0:
            return False
    return True

def find_extrapolated_value(vals):
    finals = [vals[-1]]
    currentVals = vals
    while not allZeros(currentVals):
        newVals = []
        for i in range(1,len(currentVals)):
            newVals += [currentVals[i] - currentVals[i-1]]
        currentVals = newVals
        finals.append(newVals[-1])
    return finals

res = 0

for i in data:
    vals = [int(val) for val in i.split(" ")]
    finals = find_extrapolated_value(vals)
    res += (sum(finals))
print(res)