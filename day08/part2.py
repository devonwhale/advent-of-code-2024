import math
import itertools

class Antenna:
    def __init__(self, x ,y ,value):
        self.x = x
        self.y = y
        self.value = value

    def relation(self, other):
        return (self.x - other.x, self.y - other.y)
    
    def generate_antinode(self, translation, mult):
        return (self.x + (translation[0] * mult), self.y + (translation[1] * mult))

def validate_potential_antinode(max_x, max_y, potential_antinode):
    return potential_antinode[0] >= 0 and potential_antinode[0] < max_x and potential_antinode[1] >= 0 and potential_antinode[1] < max_y


import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

rows = []
antennae = {}

parsing_y = 0
for line in input:
    parsed_line = list(line)
    rows.append(parsed_line)
    parsing_x = 0
    for char in parsed_line:
        if char != '.':
            if char not in antennae:
                antennae[char] = []
            antennae[char].append(Antenna(parsing_x, parsing_y, char))
        parsing_x += 1
    parsing_y += 1

antinodes = []

max_x, max_y = len(rows[0]), len(rows)

for antenna in antennae:
    for combination in itertools.combinations(antennae[antenna], 2):
        translation = combination[0].relation(combination[1])
        first_node_antinode = combination[0].generate_antinode(translation, 1)
        first_node_anitnode_valid = validate_potential_antinode(max_x, max_y, first_node_antinode)
        first_node_mult = 2
        while first_node_anitnode_valid:
            antinodes.append(first_node_antinode)
            first_node_antinode = combination[0].generate_antinode(translation, first_node_mult)
            first_node_anitnode_valid = validate_potential_antinode(max_x, max_y, first_node_antinode)
            first_node_mult += 1
        antinodes.append((combination[0].x, combination[0].y)) #?
        translation = combination[1].relation(combination[0])
        second_node_antinode = combination[1].generate_antinode(translation, 1)
        second_node_antinode_valid = validate_potential_antinode(max_x, max_y, second_node_antinode)
        second_node_mult = 2
        while second_node_antinode_valid:
            antinodes.append(second_node_antinode)
            second_node_antinode = combination[0].generate_antinode(translation, second_node_mult)
            second_node_antinode_valid = validate_potential_antinode(max_x, max_y, second_node_antinode)
            second_node_mult += 1
        antinodes.append((combination[1].x, combination[1].y)) #?

print(len(set(antinodes)))