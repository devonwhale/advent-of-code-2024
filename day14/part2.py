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
file_input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

WIDTH = 101
HIEGHT = 103

robots = []
for line in file_input:
    split_line = line.split()
    starting_coords = split_line[0].split('=')[1]
    starting_x, starting_y = int(starting_coords.split(',')[0]), int(starting_coords.split(',')[1])
    movement_values = split_line[1].split('=')[1]
    movement_x, movement_y = int(movement_values.split(',')[0]), int(movement_values.split(',')[1])
    robots.append(Robot(starting_x, starting_y, movement_x, movement_y))

seconds = 1
while True:
    robot_map = {}

    for robot in robots:
        robot.move(1, WIDTH, HIEGHT)
        if robot.current_x not in robot_map:
            robot_map[robot.current_x] = {}
        if robot.current_y not in robot_map[robot.current_x]:
            robot_map[robot.current_x][robot.current_y] = 0
        robot_map[robot.current_x][robot.current_y] += 1

    output = []
    requires_investigation = False
    for i in range(0, WIDTH):
        row = ''
        if i not in robot_map:
            row = '.' * WIDTH
        else:
            for j in range(0, HIEGHT):
                if j in robot_map[i]:
                    row += '#'
                else:
                    row += '.'
        
        if '#######' in row:
            requires_investigation = True
        output.append(row)

    if requires_investigation:
        file = open("output.txt", "a")
        file.write(f'Robots after {seconds} seconds\n')
        for o in output:
            file.write(o + "\n")
        file.close()
        input('Press any key to continue')

    seconds += 1