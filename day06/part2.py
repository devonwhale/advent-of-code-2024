import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

rows = []
guard_direction = (0, -1)
guard = (0, 0, guard_direction)
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
        start_x, start_y = parsed_line.index('^'), line_index
        guard = (start_x, start_y, guard_direction)
    line_index += 1

guard_positions = [guard]

output = 0

row_index = 0
for row in rows:
    char_index = 0
    for char in row:
        if char != '.':
            char_index += 1
            continue
        rows[row_index][char_index] = '#'

        guard_direction = (0, -1)
        guard = (start_x, start_y, guard_direction)
        guard_positions= [guard]

        while guard[0] > 0 and guard[0] < max_x and guard[1] > 0 and guard[1] < max_y:
            new_x = guard[0] + guard_direction[0]
            new_y = guard[1] + guard_direction[1]
            if new_x < 0 or new_x >= max_x or new_y < 0 or new_y >= max_y:
                break

            move_in_current_direction = rows[new_y][new_x]
            while move_in_current_direction == '#':
                guard_direction = direction_dict[guard_direction]
                new_x = guard[0] + guard_direction[0]
                new_y = guard[1] + guard_direction[1]
                move_in_current_direction = rows[new_y][new_x]

            new_guard_position = (guard[0] + guard_direction[0], guard[1] + guard_direction[1], guard_direction)
            new_position_char = rows[new_guard_position[1]][new_guard_position[0]]

            guard = new_guard_position
            if guard in guard_positions:
                output += 1
                break
            guard_positions.append(guard)
            
        rows[row_index][char_index] = '.'
        char_index += 1
    row_index += 1


print(output)
