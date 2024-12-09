class Block:
    def __init__(self, length):
        self.length = length
    
    def is_empty(self):
        return True
    
    def full_block(self):
        return '.' * self.length
        
class File(Block):
    def __init__(self, length, id):
        super().__init__(length)
        self.id = id

    def is_empty(self):
        return False
    
    def full_block(self):
        return self.value * self.length
    
    def full_block(self):
        return str(self.id) * self.length
    
    def move_end(self):
        self.length -= 1
        return self.id

import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

values = []

id = 0
parsing_block = True
for char in input[0]:
    if parsing_block:
        values.append(File(int(char), id))
        parsing_block = False
        id += 1
    else:
        values.append(Block(int(char)))
        parsing_block = True

defragged_files = []
for value in values:
    if value.is_empty():
        for i in range(0, value.length):
            last_block_index = -1
            block_to_move_from = values[last_block_index]
            while block_to_move_from.is_empty():
                last_block_index -= 1
                block_to_move_from = values[last_block_index]
            if block_to_move_from in defragged_files:
                break
            value_to_move = block_to_move_from.move_end()
            defragged_files.append(File(1, value_to_move))
            if block_to_move_from.length == 0:
                values.remove(block_to_move_from)
    else:
        defragged_files.append(value)

checksum = 0
index = 0
for file in defragged_files:
    for i in range(0, file.length):
        checksum += index * int(file.id)
        index += 1

print(checksum)