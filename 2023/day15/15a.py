import sys, os
sys.path.append(os.path.abspath(os.path.join('../', 'aoc')))

from aoc import get_input

data = get_input(15).split(",")
# data = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7".split(",")
print(data)

def get_hash(currVal, char):
    ascii = ord(char)
    newVal = ((currVal + ascii) * 17) % 256
    return newVal

sum = 0
for i in data:
    hash = 0
    for char in i:
        hash = get_hash(hash,char)
    print(i,hash)
    sum += hash

print(sum)