import sys, os
sys.path.append(os.path.abspath(os.path.join('../', 'aoc')))

from aoc import get_input

data = get_input(1).splitlines()

count = 0
for i in data:
    numberStr = "";
    for index in range(len(i)):
        if i[index].isdigit():
            numberStr += i[index]
            break
    for index in range(len(i)-1,-1,-1):
        if i[index].isdigit():
            numberStr += i[index]
            break
    count += int(numberStr)
print(count)
