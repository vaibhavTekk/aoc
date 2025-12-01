import sys, os
sys.path.append(os.path.abspath(os.path.join('../', 'aoc')))

from aoc import get_input

data = get_input(1).splitlines()

init_count = 50
pass_count = 0

for line in data:
    dir, ticks = line[0], int(line[1:])
    if dir == 'L':
        init_count = (init_count - ticks) % 100
    else:
        init_count = (init_count + ticks) % 100
    if init_count == 0:
        pass_count += 1
print(pass_count)