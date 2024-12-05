class Rule:
    def __init__(self, early_page, late_page):
        self.early_page = early_page
        self.late_page = late_page

    def is_applicable_rule(self, update):
        if self.early_page not in update or self.late_page not in update:
            return False
        return True

    def validate_update(self, update):
        if self.early_page not in update or self.late_page not in update:
            return True
        
        index_of_early_page = update.index(self.early_page)
        index_of_late_page = update.index(self.late_page)

        return True if index_of_early_page < index_of_late_page else False
    
    def update_output(self, update):
        index_of_early_page = update.index(self.early_page)

        update.insert(index_of_early_page + 1, self.late_page)
        update.remove(self.late_page) #Only removes the first occurance and we've just moved it further into the list

        return update


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
    applicable_rules = []
    requires_processing = False
    for rule in rules:
        if rule.is_applicable_rule(update):
            applicable_rules.append(rule)
        if not rule.validate_update(update):
            requires_processing = True

    if not requires_processing:
        continue

    last_iter_update = []
    while last_iter_update != update:
        last_iter_update = update.copy()
        for rule in applicable_rules:
            update = rule.update_output(update)

    middle_value = int(update[int((len(update) - 1) / 2)])
    output += middle_value

print(output)