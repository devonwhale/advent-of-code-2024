class Region:
    def __init__(self, value):
        self.value = value
        self.interanl_squares = 0
        self.one_wall_squares = 0
        self.two_wall_squares = 0
        self.three_wall_squares = 0
        self.four_wall_squares = 0

    def expand(self, borders):
        match borders:
            case 4:
                self.interanl_squares += 1
            case 3:
                self.one_wall_squares += 1
            case 2:
                self.two_wall_squares += 1
            case 1:
                self.three_wall_squares += 1
            case _:
                self.four_wall_squares += 1

    def cost(self):
        area = self.interanl_squares + self.one_wall_squares + self.two_wall_squares + self.three_wall_squares + self.four_wall_squares
        perimeter = self.one_wall_squares + (self.two_wall_squares * 2) + (self.three_wall_squares * 3) + (self.four_wall_squares * 4)
        return area * perimeter

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
        transformations = []
        if parsing_x > 0:
            transformations.append((-1, 0))
        if parsing_x < max_x - 1:
            transformations.append((1, 0))
        if parsing_y > 0:
            transformations.append((0, -1))
        if parsing_y < max_y - 1:
            transformations.append((0, 1))

        locations_to_check = []
        for transformation in transformations:
            if input[parsing_y + transformation[1]][parsing_x + transformation[0]] == char:
                locations_to_check.append((parsing_x + transformation[0], parsing_y + transformation[1]))
        region.expand(len(locations_to_check))

        for location in locations_to_check:
            if location in parsed_locations:
                continue
            parsed_locations.append(location)

            transformations = []
            if location[0] > 0:
                transformations.append((-1, 0))
            if location[0] < max_x - 1:
                transformations.append((1, 0))
            if location[1] > 0:
                transformations.append((0, -1))
            if location[1] < max_y - 1:
                transformations.append((0, 1))

            additional_locations_to_check = []
            for transformation in transformations:
                if input[location[1] + transformation[1]][location[0] + transformation[0]] == char:
                    additional_locations_to_check.append((location[0] + transformation[0], location[1] + transformation[1]))
            region.expand(len(additional_locations_to_check))
            locations_to_check += additional_locations_to_check

        output += region.cost()

        parsing_x += 1
    parsing_y += 1

print(output)