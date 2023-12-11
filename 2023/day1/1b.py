import sys, os
sys.path.append(os.path.abspath(os.path.join('../', 'aoc')))

from aoc import get_input
import re
data = get_input(1).splitlines()

count = 0
strToInt = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}

for i in data:
	digits = re.findall("(?=(one|two|three|four|five|six|seven|eight|nine|[1-9]))", i)
	parsed_digits = [strToInt[num] for num in digits]
	number = str(parsed_digits[0]) + str(parsed_digits[-1])
	#print(line, parsed_digits, number)
	count += int(number)
print(count)

