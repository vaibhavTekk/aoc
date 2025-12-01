import sys, os
sys.path.append(os.path.abspath(os.path.join('../', 'aoc')))

from aoc import get_input

data = get_input(1).splitlines()
# data = """L68
# L30
# R48
# L5
# R60
# L55
# L1
# L99
# R14
# L82""".splitlines()
init_count = 50
pass_count = 0

for line in data:
    dir, ticks = line[0], int(line[1:])
    inc = 1 if dir == 'R' else -1
    for i in range(ticks):
        init_count = (init_count + inc) % 100
        if init_count == 0:
            pass_count += 1
print(pass_count)