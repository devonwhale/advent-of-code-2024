import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

stones = []
for stone in input[0].split():
    stones.append(stone)

operation_cache = { '0': ['1'] }
result_cache = {}
output = 0

def blink(blink_count, stone):
    if blink_count == 75:
        return 1
    if (blink_count, stone) in result_cache:
        return result_cache[(blink_count, stone)]
    
    length = 0
    if stone in operation_cache:
        for next_stone in operation_cache[stone]:
            length += blink(blink_count + 1, next_stone)
        result_cache[(blink_count, stone)] = length
        return length
    
    if len(stone) % 2 == 0:
        first_half, second_half = str(int(stone[:len(stone)//2])), str(int(stone[len(stone)//2:]))
        for next_stone in [first_half, second_half]:
            length += blink(blink_count + 1, next_stone)
        result_cache[(blink_count, stone)] = length
        operation_cache[stone] = [first_half, second_half]
        return length
    
    next_stone = str(int(stone) * 2024)
    length = blink(blink_count + 1, next_stone)
    result_cache[(blink_count, stone)] = length
    operation_cache[stone] = [next_stone]
    return length

output = 0
for inital_stone in stones:
    output += blink(0, inital_stone)

print(output)
