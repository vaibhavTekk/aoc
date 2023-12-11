import sys, os
sys.path.append(os.path.abspath(os.path.join('../', 'aoc')))

from aoc import get_input

data = get_input(10).replace("7","]").split("\n")

# data = """7-F7-
# .FJ|7
# SJLL7
# |F--J
# LJ.LJ""".replace("7","]").split("\n")

def get_start(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'S':
                return i,j
    return -1,-1

def get_valid_pipes(board,i,j):
    pipes = []
    if board[i-1][j] in '|F]':
        pipes += [[i-1,j]]
    if board[i][j-1] in '-FL':
        pipes += [[i,j-1]]
    if board[i+1][j] in "|JL":
        pipes += [[i+1,j]]
    if board[i][j+1] in "-]J":
        pipes += [[i,j+1]]
    return pipes

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=" ")
        print()

directions = {'J':[[-1,0],[0,-1]],"]":[[+1,0],[0,-1]],'L':[[-1,0],[0,+1]],"F":[[+1,0],[0,+1]],"-":[[0,+1],[0,-1]],"|":[[+1,0],[-1,0]]}
def get_next_pipe(board,row,col):
    if board[row][col] in directions:
        pipes = directions[board[row][col]]
        validPipe = []
        for pipe in pipes:
            rr,cc = pipe[0],pipe[1]
            if not(board[row+rr][col+cc].isdigit() or board[row+rr][col+cc] == "."):
                validPipe = [row+rr,col+cc]
        return validPipe
    return None

board = []
for i in data:
    board.append(list(i))

startrow, startcol = get_start(board)
pipes = get_valid_pipes(board,startrow,startcol)
board[startrow][startcol] = str(0)
count = 1
while pipes:
    newPipes = []
    for pipe in pipes:
        row,col = pipe[0], pipe[1]
        if (get_next_pipe(board,row,col)):
            newPipes.append(get_next_pipe(board,row,col))
            board[row][col] = str(count)
        else:
            end = [row,col]
            board[row][col] = str(count)
    count += 1
    pipes = newPipes

print(board[end[0]][end[1]])
