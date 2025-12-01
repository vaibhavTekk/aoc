import sys, os
sys.path.append(os.path.abspath(os.path.join('../', 'aoc')))

from aoc import get_input

data = get_input(14)

# data = """O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#...."""

class Dish:
    def __init__(self,data):
        self.grid = [[i for i in line] for line in data.split("\n")]
    
    def display_grid(self):
        for i in self.grid:
            for k in i:
                print(k,end="")
            print()
    
    def get_col(self,icol):
        col = []
        for i in self.grid:
            col.append(i[icol])
        return col

    def replace_col(self,icol,col):
        for irow in range(len(self.grid)):
            self.grid[irow][icol] = col.pop(0) 

    def tilt(self,arr):
        newArr = arr[::]
        start = 0
        for i in range(len(newArr)):
            if newArr[i] == 'O':
                newArr[start],newArr[i] = newArr[i],newArr[start] #swap
                start += 1
            elif newArr[i] == "#":
                start = i+1
        return newArr

    def calc_val(self):
        res = 0
        for irow in range(len(self.grid)):
            count = 0
            for k in self.grid[irow]:
                if k == "O":
                    count += 1
            res += count * (len(self.grid) - irow)
        return res

dish = Dish(data)
for i in range(len(dish.grid[0])):
    col = dish.tilt(dish.get_col(i))
    dish.replace_col(i,dish.tilt(col))
dish.display_grid()
print(dish.calc_val())