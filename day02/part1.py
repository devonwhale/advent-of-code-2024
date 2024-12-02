import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

output = 0

for line in input:
    values = list(map(lambda x:int(x), line.split()))
    increasing = values[0] - values[1] > 0
    next_value = 1
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
            output += 1
        
print(output)