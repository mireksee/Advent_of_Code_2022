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
for list in lists:
    half = len(list) // 2  # Obliczamy indeks połowy stringa
    first = list[:half]  # Pobieramy pierwszą połowę stringa
    second = list[half:]
    common = (set(first) & set(second)).pop()

    sum += alphabetPriority.index(common) + 1



print(sum)