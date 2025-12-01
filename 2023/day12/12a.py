import sys, os
sys.path.append(os.path.abspath(os.path.join('../', 'aoc')))

from aoc import get_input
import re

data = get_input(12).splitlines()

data = """?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1""".split("\n")

def get_hashes(game):
    start = -1
    end = -1
    hashes = []
    for i in range(len(game)):
        if game[i] == '#':
            if i-1 >= 0 and game[i-1] == "#":
                end = i
            else:
                start = i
                end = i 
        elif i-1 >= 0 and game[i-1] == '#':
            hashes += [[game[start:end+1],start,end]]
            start = -1
            end = -1
            
    if game[-1] == '#':
        hashes += [[game[start:end+1],start,end]]
        start = -1
        end = -1

    return hashes

# def modify_game(game):
#     newGame = []
#     start = -1
#     end = -1
#     for i in range(len(game)):
#         if game[i] == '#':
#             if i-1 >= 0 and game[i-1] == "#":
#                 end = i
#             else:
#                 start = i
#                 end = i 
#         elif i-1 >= 0 and game[i-1] == '#':
#             newGame.append(str(end - start + 1))
#             newGame.append(game[i])
#             start = -1
#             end = -1
#         else:
#             newGame.append(game[i])
#     if game[-1] == '#':
#         newGame.append(str(end - start + 1))
#         newGame.append(game[-1])
#     return (newGame)

def modify_game(game):
    start = -1
    end = -1
    i = 0
    while i < (len(game)):
        if game[i] == '#':
            if i-1 >= 0 and game[i-1] == "#":
                end = i
            else:
                start = i
                end = i
            i += 1
        elif i-1 >= 0 and game[i-1] == '#':
            start = -1
            end = -1
            i += 1
        elif game[i] == '?':
            if counts:
                if start - end + 1 < counts[0]:
                    game[i] = '#'
        if start - end + 1 == counts[0]:
            print(counts)
            counts.pop(0)
        
    return game



def stringify(game):
    res = ""
    for i in game:
        res += str(i)
    return res

for i in data:
    game , counts = i.split(" ")
    counts = [int(i) for i in counts.split(",")]
    game = list(game)

    print(stringify(game),counts)
    game = modify_game(game)
    print(game)
    print(stringify(game))