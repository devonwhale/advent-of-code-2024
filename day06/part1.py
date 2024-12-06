import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

rows = []
guard = (0,0)
guard_direction = (0, -1)
max_x = len(input[0])
max_y = len(input)
line_index = 0

direction_dict = {
    (0, -1): (1, 0),
    (1, 0): (0, 1),
    (0, 1): (-1, 0),
    (-1, 0): (0, -1)
}

for line in input:
    parsed_line = list(line)
    rows.append(parsed_line)
    if '^' in parsed_line:
        guard = (parsed_line.index('^'), line_index)
    line_index += 1

guard_positions = [guard]

while guard[0] > 0 and guard[0] < max_x and guard[1] > 0 and guard[1] < max_y:
    new_x = guard[0] + guard_direction[0]
    new_y = guard[1] + guard_direction[1]
    if new_x < 0 or new_x >= max_x or new_y < 0 or new_y >= max_y:
        break

    move_in_current_direction = rows[new_y][new_x]
    if move_in_current_direction == '#':
        guard_direction = direction_dict[guard_direction]
    new_guard_position = (guard[0] + guard_direction[0], guard[1] + guard_direction[1])
    new_position_char = rows[new_guard_position[1]][new_guard_position[0]]

    guard = new_guard_position
    guard_positions.append(guard)

print(len(set(guard_positions)))
