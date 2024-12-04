class Wordsearch:
    def __init__(self, board):
        self.board = board
        self.max_x = len(board[0])
        self.max_y = len(board)

    def char_search(self, target_char, target_x, target_y):
        directions_to_check = []
        if target_x > 0:
            if target_y > 0:
                directions_to_check.append((-1, -1))
            if target_y < self.max_y - 1:
                directions_to_check.append((-1, 1))
            directions_to_check.append((-1, 0))

        if target_x < self.max_x - 1:
            if target_y > 0:
                directions_to_check.append((1, -1))
            if target_y < self.max_y - 1:
                directions_to_check.append((1, 1))
            directions_to_check.append((1, 0))

        if target_y > 0:
            directions_to_check.append((0, -1))
        if target_y < self.max_y - 1:
            directions_to_check.append((0, 1))
        
        next_locations = []
        for direction in directions_to_check:
            new_x = target_x + direction[0]
            new_y = target_y + direction[1]
            char_to_check = self.board[new_y][new_x]
            if char_to_check == target_char:
                next_locations.append((new_x, new_y, direction))
        
        score = 0
        for location in next_locations:
            if self.direction_check('A', location[0], location[1], location[2]):
                score += 1
        
        return score
    
    def direction_check(self, target_char, current_x, current_y, transformation):
        target_x = current_x + transformation[0]
        target_y = current_y + transformation[1]

        if target_x < 0 or target_x >= self.max_x or target_y < 0 or target_y >= self.max_y:
            return False
        
        if self.board[target_y][target_x] == target_char:
            if target_char == 'S':
                return True
            else:
                return self.direction_check('S', target_x, target_y, transformation)
        else:
            return False


import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

parsed_input = []

for line in input:
    split_line = list(line)
    parsed_input.append(split_line)

wordsearch = Wordsearch(parsed_input)

current_x, current_y = 0, 0
output = 0
for line in parsed_input:
    for char in line:
        if char == 'X':
            output += wordsearch.char_search('M', current_x, current_y)
        current_x += 1
    current_x = 0
    current_y += 1

print(output)