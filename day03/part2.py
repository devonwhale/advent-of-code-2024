import re
import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

output = 0

currently_ignoring = False

for line in input:
    instructions = []
    mul_regex = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
    mul_iterator = mul_regex.finditer(line)
    for match in mul_iterator:
        instructions.append(match.span())

    switch_regex = re.compile(r"do(n't){0,1}\(\)")
    switch_iterator = switch_regex.finditer(line)
    for match in switch_iterator:
        instructions.append(match.span())
    
    instructions.sort()
    for instruction in instructions:
        if line[instruction[0]] == 'm':
            if not currently_ignoring:
                mul = line[instruction[0]:instruction[1]]
                value_one = int(mul.split('(')[1].split(',')[0])
                value_two = int(mul.split('(')[1].split(',')[1][:-1])
                output += value_one * value_two
        elif instruction[1] - instruction[0] == 7:
            currently_ignoring = True
        elif instruction[1] - instruction[0] == 4:
            currently_ignoring = False

print(output)