import sys, os
sys.path.append(os.path.abspath(os.path.join('../', 'aoc')))

from aoc import get_input
import math
data = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....""".split("\n")

data = get_input(11).splitlines()

grid = [list(i) for i in data]

def is_row_empty(row):
    for i in row:
        if i != ".":
            return False
    return True

def is_col_empty(grid,col):
    for row in grid:
        if row[col] != '.':
            return False
    return True

def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j],end = '')
        print()

def expand_grid(grid):
    cols = []
    for col in range(len(grid[0])):
        if(is_col_empty(grid,col)):
            cols += [col]

    newcolsGrid = []
    for row in grid:
        newRow = []
        for j in range(len(row)):
            if j in cols:
                newRow += ['.','.']
            else:
                newRow += [row[j]]
        newcolsGrid.append(newRow)

    rows = []
    for row in range(len(grid)):
        if is_row_empty(grid[row]):
            rows += [row]

    newrowsGrid = []
    for i in range(len(newcolsGrid)):
        if i in rows:
            newrowsGrid.append(newcolsGrid[i])
            newrowsGrid.append(newcolsGrid[i])
        else:
            newrowsGrid.append(newcolsGrid[i])

    return newrowsGrid

grid = expand_grid(grid)

id = 1
vals = {}
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == '#':
            grid[row][col] = id
            vals[str(id)]=[row,col]
            id += 1

def get_distance(vals,node1,node2):
    return int(math.fabs(vals[node1][0] - vals[node2][0]) + math.fabs(vals[node1][1] - vals[node2][1]))

distances = []
for i in vals:
    for j in vals:
        if i != j:
            distances += [get_distance(vals,i,j)]

print(int(sum(distances)/2))
