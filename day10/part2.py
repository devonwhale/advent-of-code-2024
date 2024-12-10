class Node:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

def find_path(map, node):
    if node.value == '9':
        return [node]
    target_value = str(int(node.value) + 1)
    nodes_to_check = []
    if node.x > 0 and map[node.y][node.x - 1].value == target_value:
        nodes_to_check.append(map[node.y][node.x - 1])
    if node.y > 0 and map[node.y - 1][node.x].value == target_value:
        nodes_to_check.append(map[node.y - 1][node.x])
    if node.x < len(map[0]) - 1 and map[node.y][node.x + 1].value == target_value:
        nodes_to_check.append(map[node.y][node.x + 1])
    if node.y < len(map) - 1 and map[node.y + 1][node.x].value == target_value:
        nodes_to_check.append(map[node.y + 1][node.x])
    
    valid_paths = []
    for n in nodes_to_check:
        valid_paths = valid_paths + find_path(map, n)
    return valid_paths

import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

map = []
starting_coordinates = []
parsing_y = 0
for line in input:
    parsing_x = 0
    parsed_line = []
    for char in line:
        parsed_line.append(Node(parsing_x, parsing_y, char))
        if char == '0':
            starting_coordinates.append(parsed_line[-1])
        parsing_x += 1
    map.append(parsed_line)
    parsing_y += 1

output = 0
for node in starting_coordinates:
    max_value_nodes_that_can_be_reached = find_path(map, node)
    output += len(max_value_nodes_that_can_be_reached)
print(output)

