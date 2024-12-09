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
    
    def move(self):
        self.length = 0
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

file_structure = ''
for value in values:
    file_structure += value.full_block()

print(file_structure)

defragged_files = []
print(f"There are {len(values)} values to assess")
v_count = 0
for value in values:
    if v_count % 100 == 0:
        print(v_count)
    v_count += 1
    if value.is_empty():
        while value.length > 0:
            last_block_index = -1
            block_to_move_from = values[last_block_index]
            while block_to_move_from.is_empty() or block_to_move_from.length > value.length or block_to_move_from in defragged_files:
                last_block_index -= 1
                if last_block_index < 0 - len(values):
                    break
                block_to_move_from = values[last_block_index]
            if block_to_move_from.is_empty() or block_to_move_from.length > value.length or block_to_move_from in defragged_files:
                defragged_files.append(Block(value.length))
                break
            print(f"Moving from {block_to_move_from.full_block()}", block_to_move_from.length, value.length)
            length_of_moving_block = block_to_move_from.length
            value_to_move = block_to_move_from.move()
            defragged_files.append(File(length_of_moving_block, value_to_move))
            values[last_block_index] = Block(length_of_moving_block)
            value.length -= length_of_moving_block
    else:
        #print(f"Adding {value.full_block()}")
        defragged_files.append(value)

file_structure = ''
for value in defragged_files:
    file_structure += value.full_block()

print(file_structure)

checksum = 0
index = 0
for file in defragged_files:
    if file.is_empty():
        index += file.length
        continue
    for i in range(0, file.length):
        checksum += index * int(file.id)
        index += 1

print(checksum)