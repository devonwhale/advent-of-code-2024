class Button:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Machine:
    def __init__(self, a, b, target_x, target_y):
        self.a = a
        self.b = b
        self.target_x = target_x
        self.target_y = target_y

import os
import re
from sympy import Symbol, nsolve
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

machines = []

count = 0
button_a = 0
button_b = 0

button_regex = re.compile(r"\d{1,}")

for line in input:
    match count:
        case 0:
            modifiers = re.findall(button_regex, line)
            button_a = Button(int(modifiers[0]), int(modifiers[1]))
            count += 1
        case 1:
            modifiers = re.findall(button_regex, line)
            button_b = Button(int(modifiers[0]), int(modifiers[1]))
            count += 1
        case 2:
            targets = re.findall(button_regex, line)
            machines.append(Machine(button_a, button_b, int(targets[0]), int(targets[1])))
            count += 1
        case 3:
            count = 0

output = 0
for machine in machines:
    # target_x = ax * am + bx * bm 
    # target_y = ay * am + by * bm

    # (target_x - (bx * bm)) / ax = am
    # (target_y - (ay * am)) / by = bm

    a_multiplier = Symbol('m')
    b_multiplier = Symbol('n')

    x_formula = ((machine.a.x * a_multiplier) + (machine.b.x * b_multiplier)) - machine.target_x
    y_formula = ((machine.a.y * a_multiplier) + (machine.b.y * b_multiplier)) - machine.target_y
    result = nsolve((x_formula, y_formula), (a_multiplier, b_multiplier), (-1, 1))
    if result[0] % 1 == 0 and result[1] % 1 == 0:
        output += (3 * result[0]) + result[1]
    
print(output)
