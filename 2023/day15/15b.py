import sys, os
sys.path.append(os.path.abspath(os.path.join('../', 'aoc')))

from aoc import get_input
import re

data = get_input(15).split(",")
# data = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7".split(",")

def get_hash(str):
    currVal = 0
    for i in str:
        ascii = ord(i)
        currVal = ((currVal + ascii) * 17) % 256
    return currVal

class HashMap:
    def __init__(self):
        self.box = [[] for i in range(256)]

    def find_in_box(self,label):
        hash = get_hash(label)
        for i in range(len(self.box[hash])):
            if self.box[hash][i][0] == label:
                return i
        return -1

    def add_to_box(self,label,flen):
        hash = get_hash(label)
        ind = self.find_in_box(label)
        if ind != -1:
            self.box[hash][ind][1] = flen
        else:
            self.box[hash].append([label,flen])

    def remove_from_box(self,label):
        hash = get_hash(label)
        ind = self.find_in_box(label)
        if ind != -1:
            self.box[hash].pop(ind)

    def calc_focusing_power(self):
        res = 0
        for ibox in range(len(self.box)):
            box = self.box[ibox]
            if box != []:
                for ilens in range(len(box)):
                    lens = box[ilens]
                    res += (ibox + 1) * (ilens + 1) * int(lens[1])
        return res
    
    def print(self):
        for i in range(len(self.box)):
            if self.box[i] != []:
                print("box ", i,": ", end = "")
                for k in self.box[i]:
                    print(k[0],k[1], end=",")
                print()

box = HashMap()
for i in data:
    label, flen = i.replace("-","=").split("=")
    hash = get_hash(label)
    if flen == "":
        box.remove_from_box(label)
    else:
        box.add_to_box(label,flen)
box.print()
print(box.calc_focusing_power())