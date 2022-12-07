input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

lists = input.strip().split("\n")

count = 0
for pair in lists:
    elf1, elf2 = pair.split(",")
    elf1_nr1, elf1_nr2 = elf1.split("-")
    elf2_nr1, elf2_nr2 = elf2.split("-")

    if (
        ((int(elf1_nr1) <= int(elf2_nr1)) and (int(elf2_nr2) <= int(elf1_nr2))) or
        ((int(elf2_nr1) <= int(elf1_nr1)) and (int(elf1_nr2) <= int(elf2_nr2)))
    ):
        count +=1

print(count)