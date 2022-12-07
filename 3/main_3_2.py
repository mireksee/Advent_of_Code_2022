input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

lists = input.split("\n")

import string
# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.
alphabetPriority = list(string.ascii_lowercase) + list(string.ascii_uppercase)

sum = 0
current_group = []
for list in lists:
    current_group.append(list)

    if len(current_group) == 3:
        common = (set(current_group[0]) & set(current_group[1]) & set(current_group[2])).pop()
        current_group = []

        sum += alphabetPriority.index(common) + 1



print(sum)