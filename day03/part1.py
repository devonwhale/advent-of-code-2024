import re
import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

output = 0

for line in input:
    parsed_input = re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)

    for mul in parsed_input:
        value_one = int(mul.split('(')[1].split(',')[0])
        value_two = int(mul.split('(')[1].split(',')[1][:-1])
        output += value_one * value_two

print(output)