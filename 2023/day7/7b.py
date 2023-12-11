import sys, os
sys.path.append(os.path.abspath(os.path.join('../', 'aoc')))

from aoc import get_input
from functools import cmp_to_key

data = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".split("\n")

data = get_input(7).splitlines()

def getRank(hand):
    handMap = {}
    j = 0
    for i in hand:
        if i == 'J':
            j += 1
        else:
            if i not in handMap:
                handMap[i] = 1
            else:
                handMap[i] += 1
    if j == 5:
        handMap['J'] = 5
    elif j > 0:
        max, maxVal = None, float('-inf')
        for i in handMap:
            if handMap[i] >= maxVal:
                max = i
                maxVal = handMap[i]
        handMap[max] += j

    l = len(handMap)
    if l == 1:
        return 7
    elif l == 2:
        for i in handMap:
            if handMap[i] == 4: #four of a kind
                return 6
        return 5 #full house: 3 + 2
    elif l == 3:
        for i in handMap:
            if handMap[i] == 3:
                return 4 #three of a kind
        return 3
    elif l == 4:
        return 2
    elif l == 5:
        return 1

    print(len(handMap))

rank = "AKQT98765432J"

def cmp(hand1, hand2):
    if getRank(hand1[0]) > getRank(hand2[0]):
        return 1
    elif getRank(hand1[0]) == getRank(hand2[0]):
        for i in range(5):
            if hand1[0][i] != hand2[0][i]:
                if (rank.find(hand1[0][i]) < rank.find(hand2[0][i])):
                    return 1
                else:
                    return -1
        return 0
    return -1

arr = []
for i in data:
    hand, val = i.split(" ")
    arr += [[hand,int(val)]]

arr = sorted(arr, key=cmp_to_key(cmp))

res = 0
for i in range(len(arr)):
    print(arr[i], i+1)
    res += (i+1)*arr[i][1]
print(res)

