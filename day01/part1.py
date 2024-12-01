import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

list1, list2 = [], []

for line in input:
    values = line.split()
    list1.append(int(values[0]))
    list2.append(int(values[1]))

list1.sort()
list2.sort()

output = 0

index = 0
for item in list1:
    output += abs(item - list2[index])
    index += 1

print(output)