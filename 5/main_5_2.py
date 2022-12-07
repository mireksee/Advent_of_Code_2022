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

    crates = stacks[int(source)-1][-int(how_many):]
    del stacks[int(source)-1][-int(how_many):]

    stacks[int(destination)-1] +=crates

result= '';
for stack in stacks:
    result += stack[-1]

print (result)