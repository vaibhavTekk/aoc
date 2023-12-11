import sys, os
sys.path.append(os.path.abspath(os.path.join('../', 'aoc')))

from aoc import get_input
import re

data = get_input(4,2023).splitlines()

# data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
# data = data.split("\n")
# print(data)

# sum = 0

cardCount = [1 for i in range(len(data))]

for i in range(len(data)):
    card = data[i].replace(" | ",": ").split(": ")
    win, game = set([int(k) for k in re.findall("[0-9]+",card[1])]), [int(k) for k in re.findall("[0-9]+",card[2])]
    count = 0
    for num in game:
        if num in win:
            count += 1

    print(i+1,range(i+1,i+count+1))
    for k in range(i+1,i+count+1):
        if k < len(cardCount):
            cardCount[k] += cardCount[i]
        print(i+1,count,cardCount)
print(cardCount,sum(cardCount))
