import os
from collections import Counter
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

list1, list2 = [], []

for line in input:
    values = line.split()
    list1.append(int(values[0]))
    list2.append(int(values[1]))

totals = Counter(list2)

output = 0
for item in list1:
    output += item * totals[item]

print(output)