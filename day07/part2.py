import itertools
import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

output = 0
for line in input:
    target_value = int(line.split(':')[0])
    values = [int(v) for v in line.split(':')[1].split()]
    operations = []
    for operation_sequence in itertools.product('+*|', repeat= len(values) - 1): 
        idx = 1
        equation = [values[0]]
        for op in operation_sequence:
            equation.append(f" {op} {values[idx]} ")
            idx += 1
        operations.append(equation)
    
    for op in operations:
        final_value = op[0]
        idx = 0
        for calculation in op:
            if idx == 0:
                idx += 1
                continue
            if '|' in calculation:
                final_value = int(f"{final_value}{calculation.split()[-1]}")
            else:
                final_value = eval(f"{final_value} {calculation}")
            if final_value > target_value: # We've gone over, no point continuing the calculation
                break
        if final_value == target_value:
            output += target_value
            break


print(output)