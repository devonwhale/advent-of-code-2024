def validate(values):
    increasing = values[0] - values[1] > 0
    next_value = 1
    valid = False
    for value in values:
        if next_value != len(values):
            increase = value - values[next_value] > 0
            if increase != increasing:
                break
            difference = abs(value - values[next_value])
            if difference < 1 or difference > 3:
                break
            next_value += 1
        else:
            valid = True
    return valid

import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

output = 0

for line in input:
    values = list(map(lambda x:int(x), line.split()))
    valid = validate(values)
    if valid:
        output += 1
    else:
        index = 0
        for position in range(0, len(values)):
            alt_list = values.copy()
            alt_list.pop(index)
            index += 1

            valid = validate(alt_list)
            if valid:
                output += 1
                break
        
print(output)