class Region:
    def __init__(self, value):
        self.value = value
        self.locations = []
        self.corners = []

    def expand(self, location, corners):
        self.locations.append(location)
        self.corners += corners

    def cost(self):
        area = len(self.locations)
        sides = len(set(self.corners)) + self.side_adjustment()
        return area * sides
    
    def side_adjustment(self):
        adjustments = []
        for location in self.locations:
            if (location[0] + 1, location[1] + 1) in self.locations and (location[0] + 1, location[1]) not in self.locations and (location[0], location[1] + 1) not in self.locations:
                adjustments.append(location)
            if (location[0] + 1, location[1] - 1) in self.locations and (location[0] + 1, location[1]) not in self.locations and (location[0], location[1] - 1) not in self.locations:
                adjustments.append(location)
            if (location[0] - 1, location[1] + 1) in self.locations and (location[0] - 1, location[1]) not in self.locations and (location[0], location[1] + 1) not in self.locations:
                adjustments.append(location)
            if (location[0] - 1, location[1] - 1) in self.locations and (location[0] - 1, location[1]) not in self.locations and (location[0], location[1] - 1) not in self.locations:
                adjustments.append(location)
        
        return len(set(adjustments))/2


def corner_check(value, transformations, x, y):
    corners = []
    #If there is a corner in the top left, both the above and the left space must be different
    if transformations[(0, -1)] != value and transformations[(-1, 0)] != value:
        corners.append((x, y))
    #If there is a corner in the top right, both the above and the right space must be different
    if transformations[(0, -1)] != value and transformations[(1, 0)] != value:
        corners.append((x + 1, y))
    #If there is a corner in the bottom left, both the below and the left space must be different
    if transformations[(0, 1)] != value and transformations[(-1, 0)] != value:
        corners.append((x, y + 1))
    #If there is a corner in the bottom right, both the below and the right space must be different
    if transformations[(0, 1)] != value and transformations[(1, 0)] != value:
        corners.append((x + 1, y + 1))

    #If there is an external corner in the top left, both the above and the left space must be the same
    if transformations[(0, -1)] == value and transformations[(-1, 0)] == value and input[y - 1][x - 1] != value:
        corners.append((x, y))
    #If there is an external corner in the top right, both the above and the right space must be the same
    if transformations[(0, -1)] == value and transformations[(1, 0)] == value and input[y - 1][x + 1] != value:
        corners.append((x + 1, y))
    #If there is an external corner in the bottom left, both the below and the left space must be the same
    if transformations[(0, 1)] == value and transformations[(-1, 0)] == value and input[y + 1][x - 1] != value:
        corners.append((x, y + 1))
    #If there is an external corner in the bottom right, both the below and the right space must be the same
    if transformations[(0, 1)] == value and transformations[(1, 0)] == value and input[y + 1][x + 1] != value:
        corners.append((x + 1, y + 1))

    return corners

import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

parsed_locations = []
output = 0

max_x = len(input[0])
max_y = len(input)
parsing_y = 0
for line in input:
    parsing_x = 0
    for char in line:
        if (parsing_x, parsing_y) in parsed_locations:
            parsing_x += 1
            continue
        parsed_locations.append((parsing_x, parsing_y))
        region = Region(char)
        transformations = {}
        if parsing_x > 0 and input[parsing_y][parsing_x - 1] not in parsed_locations:
            transformations[(-1, 0)] = input[parsing_y][parsing_x - 1]
        else:
            transformations[(-1, 0)] = '?'
        if parsing_x < max_x - 1 and input[parsing_y][parsing_x + 1] not in parsed_locations:
            transformations[(1, 0)] = input[parsing_y][parsing_x + 1]
        else:
            transformations[(1, 0)] = '?'
        if parsing_y > 0 and input[parsing_y - 1][parsing_x] not in parsed_locations:
            transformations[(0, -1)] = input[parsing_y - 1][parsing_x]
        else:
            transformations[(0, -1)] = '?'
        if parsing_y < max_y - 1 and input[parsing_y + 1][parsing_x] not in parsed_locations:
            transformations[(0, 1)] = input[parsing_y + 1][parsing_x]
        else:
            transformations[(0, 1)] = '?'

        locations_to_check = []
        for transformation in transformations:
            if transformations[transformation] == char:
                locations_to_check.append((parsing_x + transformation[0], parsing_y + transformation[1]))
        corners = corner_check(char, transformations, parsing_x, parsing_y)
        region.expand((parsing_x, parsing_y), corners)

        for location in locations_to_check:
            if location in parsed_locations:
                continue
            parsed_locations.append(location)

            transformations = {}
            if location[0] > 0 and input[location[1]][location[0] - 1] not in parsed_locations:
                transformations[(-1, 0)] = input[location[1]][location[0] - 1]
            else:
                transformations[(-1, 0)] = '?'
            if location[0] < max_x - 1 and input[location[1]][location[0] + 1] not in parsed_locations:
                transformations[(1, 0)] = input[location[1]][location[0] + 1]
            else:
                transformations[(1, 0)] = '?'
            if location[1] > 0 and input[location[1] - 1][location[0]] not in parsed_locations:
                transformations[(0, -1)] = input[location[1] - 1][location[0]]
            else:
                transformations[(0, -1)] = '?'
            if location[1] < max_y - 1 and input[location[1] + 1][location[0]] not in parsed_locations:
                transformations[(0, 1)] = input[location[1] + 1][location[0]]
            else:
                transformations[(0, 1)] = '?'

            additional_locations_to_check = []
            for transformation in transformations:
                if transformations[transformation] == char:
                    additional_locations_to_check.append((location[0] + transformation[0], location[1] + transformation[1]))
            corners = corner_check(char, transformations, location[0], location[1])
            region.expand((location[0], location[1]), corners)
            locations_to_check += additional_locations_to_check

        output += region.cost()

        parsing_x += 1
    parsing_y += 1

print(output)