class Wordsearch:
    def __init__(self, board):
        self.board = board
        self.max_x = len(board[0])
        self.max_y = len(board)

    def x_check(self, target_x, target_y):
        if target_x == 0 or target_x == self.max_x - 1 or target_y == 0 or target_y == self.max_y - 1:
            return False

        upper_left = self.board[target_y - 1][target_x - 1]        
        upper_right = self.board[target_y - 1][target_x + 1]
        lower_left = self.board[target_y + 1][target_x - 1]        
        lower_right = self.board[target_y + 1][target_x + 1]

        upper_left_to_lower_right = (upper_left == 'M' and lower_right == 'S') or (upper_left == 'S' and lower_right == 'M')        
        lower_left_to_upper_right = (lower_left == 'M' and upper_right == 'S') or (lower_left == 'S' and upper_right == 'M')

        return upper_left_to_lower_right and lower_left_to_upper_right        

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
        if char == 'A':
            if wordsearch.x_check(current_x, current_y):
                output += 1
        current_x += 1
    current_x = 0
    current_y += 1

print(output)