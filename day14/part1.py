class Robot:
    def __init__(self, x, y, movement_x, movement_y):
        self.starting_x = x
        self.starting_y = y
        self.current_x = x
        self.current_y = y
        self.movement_x = movement_x
        self.movement_y = movement_y

    def move(self, seconds, max_x, max_y):
        for i in range(0, seconds):
            target_x = self.current_x + self.movement_x
            while target_x < 0 or target_x >= max_x:
                if target_x < 0:
                    target_x = max_x + target_x
                elif target_x >= max_x:
                    target_x = target_x - max_x
            
            target_y = self.current_y + self.movement_y
            while target_y < 0 or target_y >= max_y:
                if target_y < 0:
                    target_y = max_y + target_y
                elif target_y >= max_y:
                    target_y = target_y - max_y
            
            self.current_x = target_x
            self.current_y = target_y


import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

WIDTH = 101
HIEGHT = 103

robots = []
for line in input:
    split_line = line.split()
    starting_coords = split_line[0].split('=')[1]
    starting_x, starting_y = int(starting_coords.split(',')[0]), int(starting_coords.split(',')[1])
    movement_values = split_line[1].split('=')[1]
    movement_x, movement_y = int(movement_values.split(',')[0]), int(movement_values.split(',')[1])
    robots.append(Robot(starting_x, starting_y, movement_x, movement_y))

quadrants = {
    'top_left': 0,
    'top_right': 0,
    'bottom_left': 0,
    'bottom_right': 0
}

for robot in robots:
    robot.move(100, WIDTH, HIEGHT)
    if robot.current_x == WIDTH/2 - 0.5 or robot.current_y == HIEGHT/2 - 0.5:
        continue

    if robot.current_x < WIDTH/2:
        if robot.current_y < HIEGHT/2:
            quadrants['top_left'] += 1
        else:
            quadrants['bottom_left'] += 1
    else:
        if robot.current_y < HIEGHT/2:
            quadrants['top_right'] += 1
        else:
            quadrants['bottom_right'] += 1

print(quadrants['top_left'] * quadrants['top_right'] * quadrants['bottom_left'] * quadrants['bottom_right'])

