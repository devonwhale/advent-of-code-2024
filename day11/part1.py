import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

stones = []
for stone in input[0].split():
    stones.append(stone)

for i in range(0, 25):
    stone_index = 0
    previously_split = False
    for stone in stones:
        if previously_split:
            previously_split = False
            stone_index += 1
            continue
        elif stone == '0':
            stones[stone_index] = '1'
        elif len(stone) % 2 == 0:
            first_half, second_half = str(int(stone[:len(stone)//2])), str(int(stone[len(stone)//2:]))
            stones[stone_index:stone_index] = [first_half, second_half]
            del stones[stone_index + 2]
            previously_split = True
        else:
            stones[stone_index] = str(int(stone) * 2024)
        stone_index += 1

print(len(stones))