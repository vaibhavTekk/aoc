import sys, os
sys.path.append(os.path.abspath(os.path.join('../', 'aoc')))

from aoc import get_input

import re

data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

# data = get_input(3,2023,True)

matrix = [[char for char in i] for i in data.split("\n")]
res = 0

def printPaddedMatrix(start, end, i):
        res = ""
        for row in range(i-1,i+2):
            if row >= 0 and row < len(matrix):
                for k in range(start-1,end+1):
                    if k >= 0 and k < len(matrix[0]):
                        res += (matrix[row][k])
        return res

def containsSymbol(string):
    for i in string:
        if i not in '0123456789.':
            return True
    return False

def getInt(start,end,line):
    res = ''
    for i in range(start,end):
        res += matrix[line][i]
    return res

ns = set()

for i in range(len(matrix)):
    line = matrix[i]
    # numbers = re.findall("[0-9]+", line)
    prev = ""
    start = -1
    end = -1
    for j in range(len(line)):
        if line[j].isdigit():
            if not prev.isdigit():
                start = j
                end = j
            else:
                end = j
        else:
            #number ended
            if prev.isdigit():
                num = int(getInt(start,end+1,i))
                padded = (printPaddedMatrix(start,end+1,i))
                print(num,padded,containsSymbol(padded))
                if (containsSymbol(padded)):
                    res += num
        prev = line[j]

    if prev.isdigit():
        num = int(getInt(start,end+1,i))
        padded = (printPaddedMatrix(start,end+1,i))
        print(num,padded,containsSymbol(padded))
        if (not containsSymbol(padded)):
            ns.add(num)


print(ns)                    # res += int(num)       
print(sum(ns))
    # for num in numbers:


# print(res)
        # if i-1 >= 0:
        #     for k in range(start,end):
        #         if k >= 0 and k < len(matrix[0]):
        #             if not (matrix[i-1][k].isdigit() or matrix[i-1][k] == "."):
        #                 flag = True
        # if i+1 < len(matrix):
        #     for k in range(start, end):
        #         if k >= 0 and k < len(matrix[0]):
        #             if not (matrix[i+1][k].isdigit() or matrix[i+1][k] == "."):
        #                 flag = True
        # if start >= 0:
        #     if not (matrix[i][start].isdigit() or matrix[i][start] == "."):
        #         flag = True
        # if end < len(matrix[0]):
        #     if not (matrix[i][start].isdigit() or matrix[i][start] == "."):
        #         flag = True


