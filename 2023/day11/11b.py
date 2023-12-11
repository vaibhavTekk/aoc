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

def get_empty_rows_and_cols(grid):
    cols = []
    for col in range(len(grid[0])):
        if(is_col_empty(grid,col)):
            cols += [col]

    rows = []
    for row in range(len(grid)):
        if is_row_empty(grid[row]):
            rows += [row]

    return rows,cols



def get_distance(vals,node1,node2,erows,ecols,exp):
    rowFactor = 0
    y1,y2 = min(vals[node1][0],vals[node2][0]), max(vals[node1][0],vals[node2][0])
    x1,x2 = min(vals[node1][1],vals[node2][1]), max(vals[node1][1],vals[node2][1])
    for i in (erows):
        if i >= y1 and i <= y2:
            rowFactor += 1
    colFactor = 0
    for i in (ecols):
        if i >= x1 and i <= x2:
            colFactor += 1
    return x2 - x1 + rowFactor*exp + y2 - y1 + colFactor*exp

exp = 1000000
erows, ecols = get_empty_rows_and_cols(grid)
id = 0
vals = {}
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == '#':
            vals[id]=[row,col]
            id += 1
distances = []
for i in range(id):
    for j in range(i+1,id):
        distances.append(get_distance(vals,i,j,erows,ecols,exp-1))

print(sum(distances))
