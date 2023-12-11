import sys, os
sys.path.append(os.path.abspath(os.path.join('../', 'aoc')))

from aoc import get_input
import re

data = get_input(4,2023).splitlines()

sum = 0

for i in range(len(data)):
    card = data[i].replace(" | ",": ").split(": ")
    win, game = set([int(k) for k in re.findall("[0-9]+",card[1])]), [int(k) for k in re.findall("[0-9]+",card[2])]
    count = -1
    for num in game:
        if num in win:
            if count == -1:
                count = 1
            else:
                count *= 2

    if count != -1:
        sum += count
    print(win,game,count)

print(sum)
