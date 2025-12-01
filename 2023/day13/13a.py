import sys, os
sys.path.append(os.path.abspath(os.path.join('../', 'aoc')))

from aoc import get_input

data = get_input(13).split("\n\n")

# data = """#.##..##.
# ..#.##.#.
# ##......#
# ##......#
# ..#.##.#.
# ..##..##.
# #.#.##.#.

# #...##..#
# #....#..#
# ..##..###
# #####.##.
# #####.##.
# ..##..###
# #....#..#""".split("\n\n")

def getRow(row, grid):
    if row < 0 or row >= len(grid.split("\n")):
        return -1
    return grid.split("\n")[row]

def getCol(col, grid):
    if col < 0 or col >= len(grid.split("\n")[0]):
        return -1
    str = ""
    for i in grid.split("\n"):
        str += i[col]
    return str

def get_row_reflection(grid):
    rows = len(grid.split("\n"))
    rowReflection = -1
    j = 0
    flag = True
    while (j < rows // 2):
        if getRow(rows//2-j, grid) != getRow(rows//2+j,grid):
            flag = False
            break
        j += 1
    if flag:
        rowReflection = rows//2
    return rowReflection

def get_col_reflection(grid):
    cols = len(grid.split("\n")[0])
    colReflection = -1
    j = 0
    flag = True
    while (j < cols // 2):
        if getCol(cols//2-j, grid) != getCol(cols//2+j,grid):
            flag = False
            break
        j += 1
    if flag:
        colReflection = cols//2
    return (colReflection)


res = 0
for k in range(len(data)):
    grid = data[k]
    rowReflection = get_row_reflection(grid)
    if rowReflection != -1:
        res += rowReflection * 100
    colReflection = get_col_reflection(grid)
    if colReflection != -1:
        res += colReflection
    print("grid:", k+1, rowReflection,colReflection)


print("val:", res)
