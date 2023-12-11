import sys, os
sys.path.append(os.path.abspath(os.path.join('../', 'aoc')))

from aoc import get_input
import math

data = get_input(6).splitlines()


# data = """Time:      7  15   30
# Distance:  9  40  200""".split("\n")

data = [int(i.replace(" ","").split(":")[1]) for i in data]
 
b = -data[0]
c = data[1]

t1 = (-b + math.sqrt(math.pow(b,2) - 4*c))/2
t2 = (-b - math.sqrt(math.pow(b,2) - 4*c))/2

print(math.ceil(t1),math.ceil(t2), int(math.fabs(math.ceil(t1)-math.ceil(t2))))