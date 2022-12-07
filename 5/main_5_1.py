stacks = [
    ['Z','N'],
    ['M','C', 'D'],
    ['P']
]

input = """move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

procedures = input.strip().split("\n")

for procedure in procedures:
    _, how_many, _, source, _, destination = procedure.split(" ")
    for i in range(0, int(how_many)):
        crate = stacks[int(source)-1].pop()
        stacks[int(destination)-1].append(crate)

result= '';
for stack in stacks:
    result += stack[-1]

print (result)