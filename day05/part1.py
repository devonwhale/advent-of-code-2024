class Rule:
    def __init__(self, early_page, late_page):
        self.early_page = early_page
        self.late_page = late_page

    def validate_update(self, update):
        if self.early_page not in update or self.late_page not in update:
            return True
        
        index_of_early_page = update.index(self.early_page)
        index_of_late_page = update.index(self.late_page)

        return True if index_of_early_page < index_of_late_page else False

import os
input = open(os.path.join(os.path.dirname(__file__), "input.txt"), 'r').read().splitlines()

rules = []
updates = []
for line in input:
    if '|' in line:
        split_rule = line.split('|')
        rules.append(Rule(split_rule[0], split_rule[1]))
    elif ',' in line:
        updates.append(line.split(','))
    else:
        continue

output = 0
for update in updates:
    valid = True
    middle_value = int(update[int((len(update) - 1) / 2)])
    for rule in rules:
        if not rule.validate_update(update):
            valid = False 
            break
    if valid:
        output += middle_value

print(output)